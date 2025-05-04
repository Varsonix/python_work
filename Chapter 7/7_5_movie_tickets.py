# prompt = f"Please enter your age "
# prompt += f"\nEnter 'quit' at any time to end the program. "

# This is how I originally wrote it.
# while True:
#     age = input(prompt)

#     if age == 'quit':
#         break
#     else:
#         age = int(age)
#         if age < 3:
#             price = 0
#         elif age < 12:
#             price = 10
#         else:
#             price = 15

#     print(f"Your ticket price: {price}")

# Here's an advanced way that utilizes try / except

prompt = "Enter your age (or type 'quit' to exit): "

while True:
    user_input = input(prompt)

    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    try:
        age = int(user_input) # Convert input to integer

        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        
        print(f"Your ticket price: ${price}.00")
    
    # Handle the situation of someone typing something that isn't a number
    except ValueError:
        print("Invalid input! Please enter a valid number "
              "or type 'quit' to exit: ")