from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, text):
        return text.lower() == 'go to state1'

    def is_going_to_state2(self, text):
        return text.lower() == 'go to state2'
	
    def is_going_to_state3(self, text):
        return text.lower() == 'go to state3'

    def state3_to_user(self, text):
        return text.lower() == 'state3 to user'

    def state3_to_state1(self, text):
        return text.lower() == 'state3 to stae1'

    def on_enter_state1(self, event):
        print("I'm entering state1")
        print('CURRENT STATE: ' + machine.state)
        #self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")
        print('CURRENT STATE: ' + machine.state)
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
	'state3'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
	{
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
	{
	    'trigger': 'advance',
	    'source': 'state3',
	    'dest': 'user',
	    'conditions': 'state3_to_user'
	},
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2'
            ],
            'dest': 'user'
        },
	{
		'trigger': 'two_to_on', 'source': 'state2', 'dest': 'state1'
	}
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


if __name__ == "__main__":
    #self.machine.add_transition(trigger='wake_up', source='asleep', dest='hanging out')
    #machine.add_transition('advance', 'state3', 'state1', conditions = 'state3_to_state1')
    machine.get_graph().draw('my_state_diagram.png', prog='dot')
    while True:
        text = input('input: ')
        print('---')
        print('LAST STATE: ' + machine.state)

        machine.advance(text)
        print('FINAL STATE: ' + machine.state)
        print('---')
