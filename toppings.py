requested_topping = ['mushrooms', 'extra cheese']
final_toppings = []

if 'mushrooms' in requested_topping:
    print("Adding mushrooms.")
    final_toppings.append('mushrooms')
if 'pepperoni' in requested_topping:
    print("Adding pepperoni.")
    final_toppings.append('pepperoni')
if 'extra cheese' in requested_topping:
    print("Adding extra cheese.")
    final_toppings.append('extra cheese')

print("\nFinished making your pizza!")
print("\nToppings Used:")
print(final_toppings)