from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
        def zero_to_zero(self, text, event):
                if text in ('donnnne','boy','pen','burger','pencils','am','she','this','reading','writing','reads','ears','drinks') :
                        print(text, ", in 0 to 0")
                        return True
                else:
                        return False
        def zero_to_one(self, text, event):
                if text in ('book','pencil','is','he','the','using','drinking','write','drink','has'):
                        print(text, ", in 0 to 1")
                        return True
                else:
                        return False
        def zero_to_two(self, text, event):
                if text in ('girl','boys','girls','it','that','not','a','an','read','use'):
                        print(text, ", in 0 to 2")
                        return True
                else:
                        return False
        def zero_to_three(self, text, event):
                if text in ('cup','computer','phone','apple','books','pens','burgers','cups','computers','phones','apples','are','i','they','these','those','with','eating','eat','have','writes','uses'):
                        print(text, ", in 0 to 3")
                        return True
                else:
                        return False
        def one_to_zero(self, text, event):
                if text in ('book','pen','boys','girls','books','pencils','pens','computers','phones','are','i','these','a','an','writing','drink','reads'):
                        print(text, ", in 1 to 0")
                        return True
                else:
                        return False
        def one_to_one(self, text, event):
                if text in ('donnnne','burgers','apples','she','those','with','writes','ears','uses'):
                        print(text, ", in 1 to 1")
                        return True
                else:
                        return False
        def one_to_two(self, text, event):
                if text in ('girl','cup','apple','cups','they','the','eating','using','drinking','use'):
                        print(text, ", in 1 to 2")
                        return True
                else:
                        return False
        def one_to_three(self, text, event):
                if text in ('boy','pencil','burger','computer','phone','is','am','he','it','this','that','not','reading','read','write','eat','have','drinks','has'):
                        print(text, ", in 1 to 3")
                        return True
                else:
                        return False
        def two_to_zero(self, text, event):
                if text in ('boys','girls','books','pencils','pens','burgers','computers','phones','i','it','they','not','a','with','reading','reads','writes'):
                        print(text, ", in 2 to 0")
                        return True
                else:
                        return False
        def two_to_one(self, text, event):
                if text in ('girl','cups','am','she','the','eating','drinking','write','eat','uses','has'):
                        print(text, ", in 2 to 1")
                        return True
                else:
                        return False
        def two_to_two(self, text, event):
                if text in ('donnnne','that','these','those','read','drinks'):
                        print(text, ", in 2 to 2")
                        return True
                else:
                        return False
        def two_to_three(self, text, event):
                if text in ('boy','book','pencil','pen','burger','cup','computer','phone','apple','apples','is','are','he','this','an','writing','using','use','drink','have','ears'):
                        print(text, ", in 2 to 3")
                        return True
                else:
                        return False
        def three_to_zero(self, text, event):
                if text in ('boy','book','burger','are','am','i','these','those','with','reading','write','drink','ears','drinks'):
                        print(text, ", in 3 to 0")
                        return True
                else:
                        return False
        def three_to_one(self, text, event):
                if text in ('girl','pencil','pen','phone','it','that','the','writing','eating','using','writes'):
                        print(text, ", in 3 to 1")
                        return True
                else:
                        return False
        def three_to_two(self, text, event):
                if text in ('computer','boys','girls','pencils','cups','phones','apples','is','this','a','an','eat'):
                        print(text, ", in 3 to 2")
                        return True
                else:
                        return False
        def three_to_three(self, text, event):
                if text in ('donnnne','cup','apple','books','pens','burgers','computers','he','she','they','not','drinking','read','use','have','reads','uses','has'):
                        print(text, ", in 3 to 3")
                        return True
                else:
                        return False
        
        def on_enter_0(self, text, event):
                if text == "donnnne":
                        sender_id = event['sender']['id']
                        send_text_message(sender_id, "fail")
                        #self.go_back("","")
                        self.set_state('0')
                if text != "":
                        print("0!!!!!!!!!!!!!!!!!!!!IP:", event['sender']['id'])
                        sender_id = event['sender']['id']
                        send_text_message(sender_id, text)

        def on_enter_1(self, text, event):
                if text == "donnnne":
                        sender_id = event['sender']['id']
                        send_text_message(sender_id, "fail")
                        #self.go_back("","")
                        self.set_state('0')
                if text != "":
                        print("1!!!!!!!!!!!!!!!!!!!!IP:", event['sender']['id'])
                        sender_id = event['sender']['id']
                        send_text_message(sender_id, text)
        def on_enter_2(self, text, event):
                if text == "donnnne":
                        sender_id = event['sender']['id']
                        send_text_message(sender_id, "accpet")
                        #self.go_back("","")
                        self.set_state('0')
                if text != "":
                        print("2!!!!!!!!!!!!!!!!!!!!IP:", event['sender']['id'])
                        sender_id = event['sender']['id']
                        send_text_message(sender_id, text)

        def on_enter_3(self, text, event):
                if text == "donnnne":
                        sender_id = event['sender']['id']
                        send_text_message(sender_id, "accept")
                        #self.go_back("","")
                        self.set_state('0')
                if text != "":
                        print("3!!!!!!!!!!!!!!!!!!!!IP:", event['sender']['id'])
                        sender_id = event['sender']['id']
                        send_text_message(sender_id, text)
        