# Refactor this later (I messed it up, don't know enough yet)
def can_i_vote(input_names, input_ages):
    for age in input_ages:
        if age >= 18:
            print("You're old enough to vote!")
            print("Have you registered to vote yet?\n")
        else:
            print("Sorry, you are too young to vote.")
            print("Please rgister to vote as soon as you turn 18.\n")

ages_list = list(range(1,55))
names_list = list(f"Human, Age: {age}" for age in ages_list)

can_i_vote(names_list, ages_list)