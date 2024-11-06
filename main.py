# Programmers: Hazel Osborne, Oreoluwa Adebusoye
# Course: CS151, Zelalem Yalew
# Due Date: 11/06
# Programming Assignment: Lab 08
# Problem Statement: Display the distribution of rolls of two dice
# Data In: User number of rolls
# Data Out: Sum of rolls
# Credits: None


import random

# Purpose: Rolls two dice and returns their sum
# Name: dice_roll_calculation
# Parameters: none
# Return: sum of two dice
def dice_roll_calculation():
    dice_roll_1 = random.randint(1, 6)
    dice_roll_2 = random.randint(1, 6)
    dice_roll_sum = dice_roll_1 + dice_roll_2
    return dice_roll_sum


# Purpose: Tracks rolls in a list
# Name: track_rolls
# Parameters: number_of_rolls (int)
# Return: a list containing the count of sums from 2 to 12
def track_rolls(number_of_rolls):
    count = 0
    # Initialize list with 11 zeros (for sums 2 to 12)
    track_rolls_list = [0] * 11

    # Track the number of times each sum appears
    while count < number_of_rolls:
        dice_sum = dice_roll_calculation()  # Get sum of two dice
        track_rolls_list[dice_sum - 2] += 1  # Increment corresponding sum index
        count += 1

    return track_rolls_list


# Purpose: Error checks and ensures valid input
# Name: valid_input
# Parameters: amount (user input as string)
# Return: valid amount (integer)
def valid_input(amount):
    while not amount.isdigit() or int(amount) < 1:
        amount = input("Please enter a valid positive number: ")
    return int(amount)


# Purpose: Simulate rolling 2 dice repeatedly and keep track of sums
# Name: main
# Parameters: none
# Return: none
def main():
    # Display welcome message
    print("Welcome to the Dice Roll Simulator!")

    # Prompt the user for the number of rolls
    user_input = input("How many times would you like to roll your dice? ")
    number_of_rolls = valid_input(user_input)

    # Call track_rolls to simulate dice rolls and store the counts
    roll_results = track_rolls(number_of_rolls)

    # Output the list of roll counts for each sum
    print(f"\nRolling {number_of_rolls} pairs of dice.")
    print(roll_results)  # Show the list of counts for each sum

    # Display the distribution of sums in a formatted way
    for i in range(11):  # Loop through sums (2 to 12)
        sum_value = i + 2  # Since sums range from 2 to 12
        print(f"Sum of {sum_value:02}: {'*' * roll_results[i]}")


    # Display thank you message
    print("\nThank you for using the Dice Roll Simulator!")

main()