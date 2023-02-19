msg = ['Hello','Goodbye','How are you ?']
sended_msg = []
def show_message(messages):
    for message in messages:
        print(message)
def sent_message(message,sended_message):
    while msg:
        sending_message = msg.pop()
        print(f'Sending your message')
        sended_msg.append(sending_message)

show_message(msg)
sent_message(msg,sended_msg)

print(msg)
print(sended_msg)