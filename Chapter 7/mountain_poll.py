responses = {}
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")

    # Store the response in the dictionary.
    # So this one was confusing so I'm going to expand on it:
    # responses[name] = response is kind of like saying
    # responses = {'jordan': 'Mt. Everest'}
    # you can just set those freely, it doesn't have to already exist.
    # Just like alien['color'] = 'green' is saying:
    # alien = {'color' = 'green'} if you were defining the dict.
    # God that's confusing at first...
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")