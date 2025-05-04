available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = [print("\nFinished making your pizza!")]

if not requested_toppings:
    print("\nAre you sure you want a plain pizza?")
    print("How about you try again with some toppings?\n")
else:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print(f"Adding {requested_topping}")
        else:
            print(f"Sorry, we don't have {requested_topping}")
    print("\nFinished making your pizza!\n")


