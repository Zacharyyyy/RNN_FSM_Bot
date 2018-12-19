import os
from bottle import route, run, request, abort, static_file

from fsm import TocMachine


#VERIFY_TOKEN = "1234567890987654321"
VERIFY_TOKEN = os.environ['VERIFY_TOKEN']
PORT = os.environ['PORT']


machine = TocMachine(states=['0', '1', '2', '3'], initial='0',
auto_transitions = False,
show_conditions = True,
transitions = [
{ 'trigger': 'advance', 'source': '0', 'dest': '0', 'conditions': 'zero_to_zero' },
{ 'trigger': 'advance', 'source': '0', 'dest': '1', 'conditions': 'zero_to_one' },
{ 'trigger': 'advance', 'source': '0', 'dest': '2', 'conditions': 'zero_to_two' },
{ 'trigger': 'advance', 'source': '0', 'dest': '3', 'conditions': 'zero_to_three' },

{ 'trigger': 'advance', 'source': '1', 'dest': '0', 'conditions': 'one_to_zero' },
{ 'trigger': 'advance', 'source': '1', 'dest': '1', 'conditions': 'one_to_one' },
{ 'trigger': 'advance', 'source': '1', 'dest': '2', 'conditions': 'one_to_two' },
{ 'trigger': 'advance', 'source': '1', 'dest': '3', 'conditions': 'one_to_three' },

{ 'trigger': 'advance', 'source': '2', 'dest': '0', 'conditions': 'two_to_zero' },
{ 'trigger': 'advance', 'source': '2', 'dest': '1', 'conditions': 'two_to_one' },
{ 'trigger': 'advance', 'source': '2', 'dest': '2', 'conditions': 'two_to_two' },
{ 'trigger': 'advance', 'source': '2', 'dest': '3', 'conditions': 'two_to_three' },

{ 'trigger': 'advance', 'source': '3', 'dest': '0', 'conditions': 'three_to_zero' },
{ 'trigger': 'advance', 'source': '3', 'dest': '1', 'conditions': 'three_to_one' },
{ 'trigger': 'advance', 'source': '3', 'dest': '2', 'conditions': 'three_to_two' },
{ 'trigger': 'advance', 'source': '3', 'dest': '3', 'conditions': 'three_to_three' },
] )

@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
        body = request.json
        print('\nFSM STATE: ' + machine.state)
        print('REQUEST BODY: ')
        print(body)
        if body['object'] == "page":
                event = body['entry'][0]['messaging'][0]
                text = ""
                if event['message'].get("text"):
                        text += event['message']['text']
                        text = text.lower()
                        print("***************", text)
                        texts = text.split(" ")
                        i = 0
                        while i < len(texts):
                                print("--------------", texts)
                                machine.advance(texts[i], event)
                                i += 1
                        done = "donnnne"
                        machine.advance(done, event)
                        text = ""
                return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="0.0.0.0", port=PORT, debug=True, reloader=True)