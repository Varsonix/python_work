print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except (ZeroDivisionError, ValueError) as e:
        if isinstance(e, ValueError):
            print("You did not enter a number.")
        elif isinstance(e, ZeroDivisionError):
            print("You cannot divide by Zero.")
    else:
        print(answer)