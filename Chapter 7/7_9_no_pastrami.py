sandwich_orders = [
    'blt', 'pastrami', 'bacon sandwich', 'cheeseburger',
    'pastrami', 'cheese', 'pastrami', 'tomato',
    'pastrami', 'tomato', 'potato', 'bread',
]
finished_sandwiches = []

print("The deli has run out of pastrami.")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    if current_sandwich == 'pastrami':
        print(f"Not making: {current_sandwich}")
        continue

    print(f"Currently making: {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print("\nCompleted Sandwiches:")
print(f"{finished_sandwiches}")