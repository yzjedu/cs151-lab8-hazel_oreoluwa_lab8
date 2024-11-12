- [LAB-8 Feedback](#lab-8-feedback)
    - [Test Cases](#test-cases)
    - [Blind Test: Running the code](#blind-test-running-the-code)
    - [Open Test: Looking at the code](#open-test-looking-at-the-code)
    - [Documents for Participation Grade](#documents-for-participation-grade)
    - [Comments on the grading](#comments-on-the-grading)
    - [Grade:](#grade)
    - [Participation Grade:](#participation-grade)

# LAB-8 Feedback

### Test Cases

| Test Case | in: number of rolls   | out: result from roll |
|-----------|-----------------------|----------------|
| 1         | 100                   | Rolling 100 pairs of dice <br> List of distribution e.g. [2, 8, 11, 11, 15, 15, 17, 9, 7, 4, 1] <br> The chart matching the list           |
| 2         | 200                   | Rolling 200 pairs of dice <br> List of distribution e.g. [2, 8, 11, 11, 15, 15, 17, 9, 7, 4, 1] <br> The chart matching the list           |
| 3         | 300                   | Rolling 300 pairs of dice <br> List of distribution e.g. [2, 8, 11, 11, 15, 15, 17, 9, 7, 4, 1] <br> The chart matching the list          |



### Blind Test: Running the code

| Result   | Description                                                                                              |
|----------|----------------------------------------------------------------------------------------------------------|
| **YES-** | States purpose of program at start                                      |
| **YES-** | Asks the user for number of rolls (try 100, 200, 250, each should work)                                  |
| **YES-** | Asks the user to try again for a number of rolls less than 100 (try 99 and 10)                           |
| **YES-** | Outputs the list of values generated                                                                     |
| **YES-** | Outputs the sums of 2-12                                                                                |
| **YES-** | The sums of 2-12 are followed by number of asterisks that match that value (see README for a visual)     |
| **YES-** | The values output add up to the number of rolls requested (easiest to test with input of 100 rolls)      |

### Open Test: Looking at the code

| Result   | Description                                                                                              |
|----------|----------------------------------------------------------------------------------------------------------|
| **YES-** | The algorithm matches the code                                           |
| **YES-** | Purpose of the program is clearly stated |  
| **YES-** | The `randint` or equivalent function chooses random numbers between 1-6                                 |
| **YES-** | The `randint` or equivalent function is run twice                                                       |
| **YES-** | After `randint` is called twice, the values are added together                                          |
| **YES-** | The number of rolls to do is passed as an argument to function that does rolling                        |
| **YES-** | There is a function for outputting results                                                              |
| **YES-** | There is a function for looping through and doing all of the die rolls                                  |


### Documents for Participation Grade

|Result         |Type            |
|---------------|----------------|
|**-NO** | Reflection 1   |
|**YES-** | Reflection 2   |
|**YES-** | Algorithm      |

### Comments on the grading
- 
- 
- 

### Grade: E

### Participation Grade: S
N for Oro
 - If participation grade is unsatisfactory check the `NO` in the documents sections
