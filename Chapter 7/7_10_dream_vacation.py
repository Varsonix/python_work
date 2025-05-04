responses = {}
polling_active = True

while polling_active:
    #Prompt for name and response
    name = input("\nWhat is your name? ")
    response = input("Where would your dream vacation be? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")

for name, response in responses.items():
    # This isn't the way they write it out, but this is for my brain to read.
    print(
        f"Name: {name}\n"
        f"Response: {response}\n"
    )