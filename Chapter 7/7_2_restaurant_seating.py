num_guests = input("Greetings! How many will be dining tonight: ")
num_guests = int(num_guests)

if num_guests >= 8:
    print(f"I'm terribly sorry. You'll have to wait for a while due to the number of guests")
else:
    print(f"Good news! A table is ready for your party now!")