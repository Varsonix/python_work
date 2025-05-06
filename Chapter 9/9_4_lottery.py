from random import randint, choice
import statistics
import matplotlib.pyplot as plt


def lottery(your_number):
    """ For testing: The winning ticket is 10 """
    data_set = [] # Track each amount of plays per round

    while len(data_set) <= 1000:
        times_played = 0 # Reset the counter
        roll = 0 # Not relevant but putting it here

        while your_number != roll:
            roll = randint(1, 20)
            times_played += 1
        
        data_set.append(times_played)
    
    print(f"{data_set}") # Test 
    print(f"Average: {statistics.mean(data_set)}")
    print(f"Median: {statistics.median(data_set)}")
    print(f"St. Dev: {statistics.stdev(data_set)}")

    # Playing around with Historgrams / matplotlib.pyplot
    plt.hist(data_set, bins=10, edgecolor="black")
    plt.xlabel("Attempts to Win")
    plt.ylabel("Frequency")
    plt.title("Lottery Attempts Distribution")
    plt.show()

lottery(14)
