# Making a list to house sandwich orders

sandwich_orders = ['BLT', 'Bologne', 'Bacon Cheeseburger', 'Pastrami']
completed_orders = []

# Loop so long as sandwich_orders contains entries
while sandwich_orders:
    # We want to save the variable because we're going to use it later
    current_order = sandwich_orders.pop()
    print(f"Order Completed: {current_order}")

    completed_orders.append(current_order)

# Once everythings done, we can print the complted orders
print(completed_orders)