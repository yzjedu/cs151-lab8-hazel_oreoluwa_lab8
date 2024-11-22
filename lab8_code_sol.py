import random

# Purpose: To prompt the user to input the number of times they want to roll the dice and ensure it's a positive integer.
# Parameters: prompt (string) - The prompt message to display for user input.
# Return: The validated number of rolls as an integer.
def read_rolls(prompt):
    rolls = input(prompt)
    while not rolls.isdigit() or int(rolls) < 0:
        rolls = input(prompt)
    return int(rolls)

# Purpose: To simulate rolling two six-sided dice and return the sum.
# Parameters: None
# Return: The sum of two random integers between 1 and 6.
def roll_two_dices():
    return random.randint(1, 6) + random.randint(1, 6)

# Purpose: To simulate rolling two dice a given number of times and track how often each sum (from 2 to 12) occurs.
# Parameters: num_rolls (int) - The number of times to roll the dice.
# Return: A list where each index represents a sum (2 to 12), and each value represents the frequency of that sum.
def roll_distribution(num_rolls):
    # Initialize a list with 11 zeros to store counts of sums (2 to 12)
    sums_count = [0] * 11

    # Roll dice num_rolls times and count occurrences of each sum
    for i in range(num_rolls):
        dice_sum = roll_two_dices()
        sums_count[dice_sum - 2] += 1  # Map sum 2-12 to index 0-10

    return sums_count

# Purpose: To display the distribution of dice sums using asterisks.
# Parameters: sums_count (list) - A list where each index represents a sum (2 to 12), and each value represents the frequency of that sum.
# Return: None
def display_distribution(sums_count):
    # Display the results with asterisks
    for i in range(2, 13):  # Sums range from 2 to 12
        count = sums_count[i - 2]
        print(f"Sum of {i:02}: {'*' * count}")

# Purpose: Main function to control the flow of the program.
# Parameters: None
# Return: None
def main():
    print('\n\nThis program prints the normal distribution of rolling two dices\n')
    num_rolls = read_rolls("How many times would you like to roll the dice? ")
    sums_count = roll_distribution(num_rolls)
    print()
    print(f'The list is: {sums_count} \n')
    display_distribution(sums_count)
    print('\nThank you for using this program\n\n')

main()