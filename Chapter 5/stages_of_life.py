import random

### Original Code

# Start with age
#person_age = 5

# Head into if elseif chain
# if person_age < 2:
#     print("Baby")
# elif person_age >= 2 and person_age < 4:
#     print("Toddler")
# elif person_age >= 4 and person_age < 13:
#     print("Kid")
# elif person_age >= 13 and person_age < 20:
#     print("Teenager")
# elif person_age >= 20 and person_age < 65:
#     print("Adult")
# else:
#     print("Elder")


# Now that we have the baseline for the project. Let's start pumping it up

# Let's create a huge array with random ages between 1 and 103
humans = [random.randint(1, 103) for _ in range(100)]

# Let's create a method to utilize this newly made list/array
def stage_of_life(list_of_humans):
    # Let's create an output array (So we're not flooding the terminal)
    human_stages_list = []
    # Let's refactor our previous if/elif/else chain into this
    for human_age in list_of_humans:
        if human_age < 2:
            human_stages_list.append("Baby")
            #print("Baby")
        elif human_age >= 2 and human_age < 4:
            #print("Toddler")
            human_stages_list.append("Toddler")
        elif human_age >= 4 and human_age < 13:
            #print("Kid")
            human_stages_list.append("Kid")
        elif human_age >= 13 and human_age < 20:
            #print("Teenager")
            human_stages_list.append("Teenager")
        elif human_age >= 20 and human_age < 65:
            #print("Adult")
            human_stages_list.append("Adult")
        else:
            #print("Elder")
            human_stages_list.append("Elder")
    # Once completed, let's print out the finished list
    # Can you return the list instead?
    return human_stages_list

#Let's call the method and see how we did!
list_of_humans = stage_of_life(humans)

# We could do something stupid, and probably highly inefficient
# Let's sort out all the human types into separate lists and count them.
def human_sorter(list_of_human_types):
    # This is the part that I KNOW we can refactor through a single list
    # Or even better, just utilizing the list we were passed
    baby_list = []
    toddler_list = []
    kid_list = []
    teen_list = []
    adult_list = []
    elder_list = []

    for human in list_of_human_types:
        if human == "Baby":
            baby_list.append(human)
        elif human == "Toddler":
            toddler_list.append(human)
        elif human == "Kid":
            kid_list.append(human)
        elif human == "Teenager":
            teen_list.append(human)
        elif human == "Adult":
            adult_list.append(human)
        else:
            elder_list.append(human)
    # First, let's just test our lists, to see if they even got values
    print(f"Babies: {len(baby_list)}")
    print(f"Toddlers: {len(toddler_list)}")
    print(f"Kids: {len(kid_list)}")
    print(f"Teenagers: {len(teen_list)}")
    print(f"Adults: {len(adult_list)}")
    print(f"Elders: {len(elder_list)}")

# human_sorter(list_of_humans)

# I'm going to leave this method for historical purposes
# However, I figured out a better way to handle this

def human_type_counter(list_of_human_types):
    print(
        f"Human Babies: {list_of_human_types.count('Baby')}\n"
        f"Human Toddlers: {list_of_human_types.count('Toddler')}\n"
        f"Human Kids: {list_of_human_types.count('Kid')}\n"
        f"Human Teenagers: {list_of_human_types.count('Teenager')}\n"
        f"Human Adults: {list_of_human_types.count('Adult')}\n"
        f"Human Elders: {list_of_human_types.count('Elder')}"
    )


human_type_counter(list_of_humans)


# including this AI Suggestion when asking about PEP 8 Compliance

def human_type_counter_ai_suggested(list_of_human_types):
    categories = ["Baby", "Toddler", "Kid", "Teenager", "Adult", "Elder"]
    print(
        "\n".join(
            f"Human {cat}s: {list_of_human_types.count(cat)}"
            for cat in categories
        )
    )