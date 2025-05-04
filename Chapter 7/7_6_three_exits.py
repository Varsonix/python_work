#Can you do 3 while loops in a single file? Let's fine out

# Loop 1 > Simple conditional
current_number = 0

while current_number < 10:
    print(f"Current Number: {current_number}")
    current_number += 1

# Loop 2 > Variable switch (True/False)

switch_lever = True
number = 0

while switch_lever:
    
    number += 1

    print(f"{number} for switch_lever")

    if number == 10:
        switch_lever = False


prompt = f"\n Please type something (or 'quit' to exit): "

while True:
    user_input = input(prompt)

    if user_input.lower() == 'quit':
        break

    print (f"{user_input} is what you typed. Go again: ")