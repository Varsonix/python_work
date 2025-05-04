prompt = f"\nPlease enter a topping to add to your pizza."
prompt += f"(Type 'quit' any time when you're finished)"


toppings_list = []
while True:
    topping = input(prompt)

    if topping == 'quit':
        print(f"Very well, here is your topping selection: \n{toppings_list}")
        break

    prompt = f"{topping} has been added. What else would you like?"
    toppings_list.append(topping)

