### Algorithm for Dice Roll Simulation Program

---

## Tasks

- Read the number of totla rolls 
- Determin the sum of rolling two dice
- Generate the distribution form each sum
- Display the distribution
- main function to run the entire program

### Algorithm for `read_rolls(prompt)`

- **Purpose**: To prompt the user to input the number of times they want to roll the dice and ensure the input is a positive integer.
- **Name**: `read_rolls`
- **Parameters**: 
  - `prompt` (string): A message displayed to the user for input.
- **Return**: The validated number of rolls as an integer.
- **Algorithm**:
  1. Display the `prompt` message and get the user's input as `rolls`.
  2. While `rolls` is not a positive integer:
     1. Display the `prompt` message again to ask the user for valid input.
  3. Convert `rolls` to an integer and return it.

---

### Algorithm for `roll_two_dices()`

- **Purpose**: To simulate rolling two six-sided dice and return the sum.
- **Name**: `roll_two_dices`
- **Parameters**: None
- **Return**: An integer representing the sum of two random dice rolls.
- **Algorithm**:
  
  1. Generate two random integers between 1 and 6, add them and return the sum.

---

### Algorithm for `roll_distribution(num_rolls)`

- **Purpose**: To simulate rolling two dice a given number of times and keep track of how often each possible sum (from 2 to 12) occurs.
- **Name**: `roll_distribution`
- **Parameters**: `num_rolls` (int): The number of times to roll the dice.
- **Return**: A list where each index represents a sum (2 to 12), and each value represents the frequency of that sum.
- **Algorithm**:
  1. Initialize a list `sums_count` with 11 zeros to store counts of sums from 2 to 12.
  2. For each roll in `num_rolls`:
     1. Call `roll_two_dices` to get the sum of the dice.
     2. Map the sum (2-12) to the appropriate index in `sums_count` by subtracting 2, and increment the count at that index.
  3. Return `sums_count`.

---

### Algorithm for `display_distribution(sums_count)`

- **Purpose**: To display the distribution of dice sums using asterisks, where each line shows a sum and the corresponding count.
- **Name**: `display_distribution`
- **Parameters**: `sums_count` (list): A list where each index represents a sum (2 to 12), and each value represents the frequency of that sum.
- **Return**: None
- **Algorithm**:
  1. For each sum value from 2 to 12:
     1. Access the corresponding count from `sums_count` by subtracting 2 from the sum to get the index.
     2. Display the sum with leading zero if necessary, followed by a number of asterisks equal to the count.

---

### Algorithm for `main()`

- **Purpose**: To control the flow of the program: greet the user, read the number of rolls, calculate the distribution, display the distribution, and output a closing message.
- **Name**: `main`
- **Parameters**: None
- **Return**: None
- **Algorithm**:
  1. Display an introductory message explaining the program’s purpose.
  2. Call `read_rolls` with a prompt to get the number of rolls from the user and store it in `num_rolls`.
  3. Call `roll_distribution` with `num_rolls` to get the distribution of sums and store it in `sums_count`.
  4. Call `display_distribution` with `sums_count` to display the distribution of dice sums.
  5. Display a thank you message indicating the program has ended.