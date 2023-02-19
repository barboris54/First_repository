msg = ['Hello','Goodbye','How are you ?']
sended_msg = []
def show_message(messages):
    for message in messages:
        print(message)
def sent_message(message,sended_message):
    for message in msg:
        sended_msg.append(message)
        print(f'Sending your message')

show_message(msg)
sent_message(msg,sended_msg)

print(sended_msg,msg)