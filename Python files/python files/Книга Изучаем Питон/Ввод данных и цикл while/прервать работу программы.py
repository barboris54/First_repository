prompt = 'Tell me something and I will repeat it back to you'
prompt += 'Enter your message'
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
