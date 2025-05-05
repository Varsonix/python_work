messages = [
    'Hello there.',
    'I am a message',
    'Messages are cool!',
    'We should be saving the game mode',
    'To the header file',
    'for how many times',
    'I have referenced it',
]
sent_messages = []

def show_messages(messages):
    for message in messages:
        print(f"{message}")

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)


send_messages(messages, sent_messages)

print(f"\n{messages}")
print(f"\n{sent_messages}")
