
- Purpose:  rolls dice and adds up the sum
- Name: dice_roll_calculation
- Parameters: none
- Return: sum
- Algorithm:
   1. Generate a random integer between 1 and 6, set as dice roll 1 
   2. Generate a random integer between 1 and 6, set as dice roll 2 
   3. Dice roll sum = dice roll 1 + dice roll 2

* Purpose: keeps track of rolls in list
* Name: track_rolls
* Parameters: number_of_rolls
* Return: list
* Algorithm:
    1. count = 0
    2. Set track_rolls_list to have 12 0's
    2. While count < number of rolls
       5. call dice_roll_calculation
       6. add 1 to list index corresponding with sum
       6. add 1 to count


* Purpose: error checks
* Name: valid_input
* Parameters: amount
* Return: amount
* Algorithm:
    6. while not amount.isdigit or amount < 1
    7. re-prompt user to enter a valid amount



* Purpose: simulating rolling 2 dice repeatedly and keeping track of sums.
* Name: main
* Parameters: none
* Return: none
* Algorithm:
    1. Display welcome message / purpose
    2. Prompt user to enter number of pairs of dice they would to roll
    3. Call valid_input
    4. Call track rolls
    7. output list and pairs of dice rolled
    8. for sum in list:
       9. output "Sum of" index of (sum + 2) "*" multiplied by sum
    10. output thank you message

1. Run Main
   

