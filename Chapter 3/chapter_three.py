bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[0].title())

message = f"My first bicycle was a {bicycles[0].title()}."

print(message)


names = ['Cory', 'Ray', 'Jordan', 'Chris']
print("---")
print(f"Greetings, {names[0]}!")
print(f"Greetings, {names[1]}!")
print(f"Greetings, {names[2]}!")
print(f"Greetings, {names[3]}!")

names[2] = 'Nerd'
print(names[2])

print(names)
# Adding something to the end of the list
print("Add Mark to end of list")
names.append('Mark')
print(names)

# Inserting something at a specific point
print("Insert Jeff at index 2")
names.insert(2, 'Jeff')
print(names)

del names[0]
print ("Delete 1st index")
print (names)

# Using pop to push out the last item of a list and put it in a new one
print("---")
print("Popping last index out into new array")
print(names)
popped_names = names.pop()
print(names)
print(popped_names)


motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)

print(f"{too_expensive.title()} is too expensive for me.")

print(f"The last motorcylce I owned was a {last_owned.title()}")
print(f"The first motorcylce I owned was a {first_owned.title()}")


# Exercise: Guest List
print('-----')
guest_list = ['Paul Stevens', 'Eric Matthes', 'Michael Douglas']

for guest in guest_list:
    print(f"{guest.title()}, Would you like to come to dinner?")

print('-----')
print(f"Oh no, {guest_list[2].title()} can't make it.")
guest_list.remove('Michael Douglas')
guest_list.append('Jeff Goldblum')
print('-----')

for guest in guest_list:
    print(f"{guest.title()}, Would you like to come to dinner?")

print('-----\nMore tables have opened up, we will add 3 more people!\n-----')

guest_list.insert(0, 'Jeff Bridges')
guest_list.insert(2, 'Steve Carell')
guest_list.append('John Goodman')

for guest in guest_list:
    print(f"{guest.title()}, Would you like to come to dinner?")

print('-----\nThe tables wont arrive on time! We can only invite two guests now.\n-----')

print(f"I'm sorry, {guest_list.pop().title()} I won't be able to invite you.")
print(f"I'm sorry, {guest_list.pop().title()} I won't be able to invite you.")
print(f"I'm sorry, {guest_list.pop().title()} I won't be able to invite you.")
print(f"I'm sorry, {guest_list.pop().title()} I won't be able to invite you.")

for guest in guest_list:
    print(f"{guest.title()}, You'll still be able to come though!")

del guest_list[1]
del guest_list[0]
print(guest_list)
print('Program End')

# Organizing Data
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print('Sorting List...')
cars.sort()
print(cars)
print('Sorting Reverse...')
cars.sort(reverse=True)
print(cars)


# Temporary Sorting
new_cars = ['toyota', 'audi', 'chevrolet', 'vauxhall']
print(new_cars)
print("Temporarily Sorting...")
print(sorted(new_cars))
print("Sort Complete... Reverting...")
print(new_cars)
new_cars.reverse()
print(new_cars)
new_cars_length = len(new_cars)
print(new_cars_length)


# Exercise 3-8
print("Exercise\n-----")
places = ['Japan', 'Australia', 'New Zealand', 'Scotland', 'Britain']

print(f"Original Order\n{places}")
print(f"Temporarily sorted...\n{sorted(places)}")
print(f"Original Order\n{places}")
print(f"Temporarily reversing sort...\n{sorted(places, reverse=True)}")
print(f"Original Order\n{places}")
places.reverse()
print(f"Permanently Reversing Sort\n{places}")
places.reverse()
print(f"Permanently reversing sort again...\n{places}")
places.sort()
print(f"Permanently Sorting...\n{places}")
places.sort(reverse=True)
print(f"Permanently reverse sorting from previous position...\n{places}")
number_of_places = len(places)
print(f"Number of places:\t{number_of_places}")

print(places[-1])