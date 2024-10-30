[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jNVIvueR)
# CS151 Lab 8

### 🔴🔴 *DO NOT* Start to code before the instructor Approve your algorithm, and test cases 🔴🔴

- **Grade: EMRN**
- **Due: Before Next Lab**

## `Problem`
Dr. Zee is interested in understanding the probability and distribution of rolling dice. 
- Create a program to display the distribution of rolls of two dice.

## `Purpose`
This lab gives you practice with: 

  * Lists
  * Functions
  * Loops 
  * Random numbers

## `Details`
Write a program to simulate rolling a pair of 6-sided dice based on how many times a user requests the dice to be rolled. 
- Ask the user how many rolls to do (one roll means one pair of dice are rolled). 
- Every time a pair is rolled, get the sum of the 2 numbers from that roll.
  - The sums of the rolls will vary from 2 to 12 (do you understand why?). 
  - You should use a list to keep count of each possible sum (from 2 to 12).
- After gathering the data, create a chart like the one below to display the distribution of rolls at the end of the program. 
  - For example: if a 2 was rolled twice, there should be two "*" after "Sum of 2". 
  - Actual results will vary, but you should follow the same style.


### `Output`

In the output below, the `[2, 8, 11, 11, 15, 15, 17, 9, 7, 4, 1] ` is outputting the number of rolls per potential total. 
- Your values will likely be different.

The output should be similar to the following in style:
```
Rolling 100 pairs of dice                                                                                             
[2, 8, 11, 11, 15, 15, 17, 9, 7, 4, 1]                                                                                
Sum of 02 **
Sum of 03 ********
Sum of 04 ***********
Sum of 05 ***********
Sum of 06 ***************
Sum of 07 ***************
Sum of 08 *****************
Sum of 09 *********
Sum of 10 *******
Sum of 11 ****
Sum of 12 *   
```

### `Programming Tips`

* You can use methods from the `random` module such as `random.randint` to simulation a die roll. 
  * Look up how to use this function if you don't remember.
* You should make sure the user enters a valid value for number of rolls. 
  * Make them try again until they enter a valid value.
* The only user input should be the number of rolls. 
  * Don't ask the user to do something for every die roll.
* You must use functions in your program.
  * All code must be in a function other than imports. 
    * Use a **_main_** function to coordinate the program flow.

## `Design`
You should use iterative development to build your solution:
- **Start Small**: *Think about what task you should solve*. And, for each task do the simplest part first
  - For example: 
    - Begin by writing a function that rolls one die and test it.
    - Extend it to roll two dice and calculate the sum.
- **Incremental Development**: Gradually add more functionality, such as counting the sums and generating the chart.
  - Test each part before moving on to the next.
- **Printing the Asterisk Chart**: For each possible sum, print the corresponding number of asterisks.
  - For sums below 10, use `f'{i + 2:02}'` to add a leading zero.
  - This format ensures the sum is always printed as a two-digit number.
### Function design: 
  Use the guidlines for creating a function
  -  **In algorithm**
  ```
  
  # Purpose:  [what problem does the function solve?]
  # Name: [The proposed name of the function]
  # Parameters: [list with purpose in the same order they appear in the function header]
  # Return: [return value, it's type, and what it represents]
  # Algorithm:
  ```
  - **In Code**
  ```
  # Purpose:  [what problem does the function solve?]
  # Parameters: [list with purpose in the same order they appear in the function header]
  # Return: [return value, it's type, and what it represents]
  ```

## `Steps:`
1. Make sure you understand the problem
2. Write your algorithm in `algorithm.md`. Get your lab instructor's approval. 
   - Use functions. `Take turns driving`
   - You can draw the flow chart on `flowchart.drawio.svg` file: 
3. Write your code in `main.py` to match your algorithm. 
   - Writing each piece and then testing it before moving on is a great way to do iterative development. 
   - To succeed on this lab it is crucial that you get each piece working before moving on to the next. `Take turns driving`
4. Write comments in your code to make it clear what it is doing. 
   - Don't forget function comments (purpose, parameters, return) above every function.


## `What to Submit in GitHub:`

1. Completed `main.py` file  
2. `algorithm.md`
   1. Must contain image of your flow chart
3. Encrypt your files using the `keys` and `process_reflection.py`
   1. `RD1.md` -> Reflection for Drive 1
   2. `RD2.md` -> Reflection for Drive 2
   3. If you use a different key, it is considered unsubmitted

**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get?
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working with your partner?

**Make sure the file in your PyCharm and Github is the same (i.e. Commit and Push)**