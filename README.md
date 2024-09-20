﻿# PRG101-Lab2
# Submission Details

In this lab you will create eleven simple scripts. Write the scripts in Jupyter Lab notebook. 
Please note that you must complete the lab during the class hours and show your progress to the professor to receive the marks for the lab.

## INVESTIGATION 1: USING IF-ELSE AND input() FUNCTION
An IF statement is a decision statement that executes or does not execute a section of code based on whether the condition is True or False.
In investigation 1 you will learn how to take input from user, and compare it with other values.

### lab2a.py
#### Simple if statement
- Fill in the required fields in the comment section.
- Create a variable x, and set its value as a number inputted from the user. 
- Use the `type()` function to check the type of `x`.
- You will notice that the type of `x` is `str`.
- Convert `x` to integer.
- Write an if-statement to evaluate the expression if x is greater than or equal to 6.
- If the expressions evaluates to TRUE, print: `"x is greater then 6!"
- Next write another if statement combining both relational and Boolean operator to evaluate the expression if x is greater than or equal to 4 and x is less than 12.
- Print the appropriate message to user if the expression evaluates to TRUE.

### lab2b.py
#### Using if-else statement
- Fill in the required fields in the comment section.
- Use the input() function and ask the user to enter a 4 digit integer. Save this value in the variable `num`.
- The program should print out "George Orwell" if the number is exactly 1984, and otherwise prints “Not quite right!”. Use `if`, and `else` statement.


### lab2c.py
#### String comparison
- Fill in the required fields in the comment section.
- The script should include 2 variables `str1` and `str2`.
- The value of `str1` and `str2` should both be a sentence inputted by the user.
- Use `if`, `elif`, and `else` statements and the `len()` function to figure out which variable has the most characters.
- The final result should be: "--- is longer then ----!"
- If they are equal then it should result in: "--- and --- are of equal length!"

## INVESTIGATION 2: USING COMMAND LINE ARGUMENTS
So far you have been using the input() function to get user input. We can also provide input from command line as an argument after your script name on the command line. 
In this section, you will learn how to pass an argument to your Python script, but this time, the argument will be passed when you execute your Python script from the terminal. In fact, your script name is also an argument to python interpreter. You can provide additional arguments. 

In order to access command line arguments in Python, we will need to use a special python object called `sys.argv` from the `sys module`. We can use the python keyword import to load the `sys module` so that we can access it in our python script. `sys.argv` is a list object which is used to hold everything given at the command line, including the command itself.

The `sys module` is one of the built-in modules that comes with the Python interpreter. By issuing the import sys statement at the top of a python script, it will load the code written by another person. Each 'library' (or 'module') that gets loaded will give us extra functionality and objects to our python script.

### lab2d.py
- Fill in the required fields in the comment section.
- Import the sys module.
- Next add the following lines in your script.
- Then add the following lines to your script.

``` Python
print(sys.version) # prints the version of the python currently in use.
print(sys.platform) # prints the name of operating system.
print(sys.argv) # prints the list of all arguments given at the command line when running our python script from terminal.
print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.
```
- Run your script using the command `python ./lab2d.py`
- Observe the output. How many arguments were passed to python this time?  Only one, which is your script name. You will see the path to your script file in the output of  print(sys.argv).
- Add the following lines to your script.
  
```Python
print(sys.argv[0]) # prints the first argument, it is always the name of script.
print(sys.argv[1]) # prints the second argument .
print(sys.argv[2]) # prints the third argument.
print(len(sys.argv)) # tells us the number of command line arguments the user provides from terminal.
```
- Now run the script using the following command: `python lab2d.py maija Maija`.
- What do you observe? What did you learn?  This time we provided three arguments. The name of script is the first argument, second argument is maija and third argument is Maija.


### lab2e.py
- Fill in the required fields in the comment section.
- Copy the contents of lab2d.py into lab2e.py file.
- Remove the unnecessary lines which print version, platform and list of arguments.
- For this script, we are interested in how many arguments are provided after the script name. This is important because your script needs the arguments to receive data from user.
- Let’s assume that our script requires exactly two arguments.
- Modify the script, use an if-elif statement to check how many arguments are passed.
- The script should print a message if zero arguments were passed, or if not exactly 2 arguments are provided when running the script. The script should print the EXACT OUTPUT as shown.

  **Sample Run 1:**
  ```
  python ./lab2e.py
  output: This script requires exactly two arguments. No arguments were provided!
  ```
  **Sample Run 2:**
  ```
   python  ./lab2e.py maija Maija
   output: Hello user, good job, your provided two arguments!
  ```
   **Sample Run 3:**
  ```
  python ./lab2e.py 1 2 3
  output: This script requires exactly two arguments. You provided three arguments.
  ```
  
### lab2f.py
- Fill in the required fields in the comment section.
- Create a variable called name.
- Create another variable called age.
- The script should assign the string sys.argv[1] (first argument) to the variable "name"
- The script should assign the string sys.argv[2] (second argument) to the variable "age".
- The script should use if-elif structure and should print the EXACT OUTPUT as shown below.

**Sample Run 1:**
``` 
python ./lab2f.py Maija 20 PRG101
output: Hi Maija, you are 20 years old and the script received 3 arguments.
```  
**Sample Run 2:**
```
python ./lab2f.py Maija 20 PRG101 Seneca
output: Hi Maija, you are 20 years old and the script received 4 arguments.
```  
**Sample Run 3:**
```
python ./lab2f.py
output: The script requires at least 2 arguments.
```

## INVESTIGATION 3: USING NESTED CONDITIONS
- Using nested conditions are helpfull im multiple situations in python.
- Nested conditions are using statments like if and else multipule times on top of each other.
- These can be used when you have to narrow down specifics or doing more complex conditions.
- In investigation 3 you will learn how to use nested conditions and will practice using them.
- example:
- Add the following lines to your script.
``` Python
x=3
if x < 6:
    if x >2: # this if is nested in the above if
        print("x is less than 6 and x is greater than 2.")
```


### lab2g.py
![image][def]

- Fill in required fields in comment section.
- Create a program calculating tax with the image above
- The script should include a variable `income`.
- The value of income should be a number (preferably in the thousands) inputted by the user.
- The script should also include a variable `status`.
- The value of status will either be "single" or "married" entered by the user.
- Use nested `if`, `elif`, and `else` statements to create a working model of the image above.
- Also use relational operators to compare `income` and `status` with the threshold values given in your slides.
- Test your program with multiple different numbers.


## INVESTIGATION 4: USING LOOPS
Loops are used in all programming languages for multiple situations. Loops use an expression and will repeat the code under the expression untill the expression is True. In investigation 4 you will learn about the 2 types of loops; `while loop and for loop`.

**while Loop**
In Python, a while loop is used to execute a block of statements repeatedly until a given condition/expression is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed. while loops may use the same type of expression/condition found in IF statements. While the expression is evaluated to True, the code - indented under the while loop will be repeated. When the expression becomes False the loop will stop repeating the indented - code.
All the statements are indented by the same number of character spaces after a programming construct are considered to be part of a single block of code.

```
while expression:
    statement(s)

```
- Create a temporary python file for practicing with the following example and copy this code block.
- A while loop is used commonly in scenarios where you would like to repeat certain statements until an event is True or False. While loop is also called event-controlled loop. Below is a WHILE loop which will run five times. Each time the loop is run, it will add one to the integer count object, increasing the value of the count object. The variable count is iteration variable and it values changes in each iteration.
  
  ``` Python
  count = 0  # iteration variable, while loop requires a relevant variable which is used in the loop expression
  while count != 5: # expression (evaluates to True or False)
      print(count)   # Loop body
      count = count + 1  # Loop body, count is incremented,  or else the loop will continue forever
  print('loop has ended')  # This statement is not part of loop body. This statement will be executed once the loop condition becomes false.
  ```
- Try to change the value of count to 1 and then run the program to see how many times the loop runs.
- Also try to change the expression from `count < 5 ` and then run the program to see how many times the loop runs.
- Next change the expression `count <= 5` and then run the program to see how many times the loop runs.
- What did you observe in all of the above examples when you change the value of loop variable or the expression. It is important that you are well aware of initial value of loop variable and the condition in the loop expression to know exactly how many times the loop will be executed.
- Search on internet about "What is off by 1 error in loops"?

In this next exercise you will write a simple while loop that executes a block of code 10 times.

### lab2h.py
- Fill in required fields in the comments section.
- The script should include a variable `timer`.
- The value of `timer` initially should be 10.
- Use a while loop to create a program that counts down from 10 using `timer`.
- At the end it should print `blast off!`.
- The program should generate the following output:
  ``` Python
  10
  9
  8
  7
  6
  5
  4
  3
  2
  1
  Blast off!
  ```

In python, we often use while loop to see if the user entered the required value. We keep asking the user for a value until the user enters the correct value. this is a scenario driven by an event rather than driven by a counter, becasue you do not know how many times the user will enter the incorrect value before the user enters the correct value. See the example below:

```Python
guess = 5
number = int(input("Guess what number less than 10 I am thinking off?"))
while number != guess:  # loop condition 
  print("incorrect guess, try again...)
  number = int(input("Guess what number less than 10 I am thinking off?")) # keep taking input from user until the user enters the correct guess.
print("You got it right!") # this statement will be executed when loop has terminated which will only happen when the user enters the number 5.

```
Now attempt this example yourself.

### lab2i.py
- Fill in required fields in the comments section.
- The script should include a variable `pin`.
- The value of `pin` should be a 4 digit code entered by the user.
- Use a while loop to create a program that wont end until the user enters the correct pin 1234.
- The result should be like this:
```
Please type in your PIN: 0000
Incorrect...try again

Please type in your PIN: 199

Incorrect...try again

Please type in your PIN: 1234
Correct PIN, You can enter!
```
Keep practicing, attempt this next exercise now!

### lab2j.py
In this exercise, you will practice using break and continue statements in a loop. This script will handle the user input, check for invalid numbers, continue if the number is negative, and exit the loop when zero is entered.
- Next write a program that repeatedly prompts the user to input a number and performs the following actions based on the input:
    -  Negative Number: If the user inputs a negative number, the program prints "Invalid number." and prompts for a new input. Use continue statement
    -  Zero: If the user inputs zero, the program prints "Exiting..." and terminates. Use break statement
    - Non-Negative Number: For any other non-negative number:
        -  The program calculates the square root of the number and prints the square root as output.
    - The program continues to prompt the user for input until the user enters zero.
- The result should be: 
``` Python
Please type in a number: 32

Please type in a number: 9
3.0

Please type in a number: 1
1.0

Please type in a number: -9
Invalid number.

Please type in a number: 0
Exiting ...
```

**for Loop:**
A for loop is used for iterating over a sequence (that could be either a list, a tuple, a dictionary, a set, or a string).
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
A very common example of for loop found in all text books is:

``` Python
fruits = ["apple", "banana", "cherry", "date"]

# Use a for loop to iterate over the list
for fruit in fruits:
    print(fruit)
```
for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.

``` Python
for i in range(5):
    print(i)
```
The range(5) function generates a sequence of numbers from 0 to 4 (inclusive of 0, exclusive of 5).


### lab2k.py
Write a Python program that calculates the sum of all even numbers from 1 to 100 (inclusive).
- Use a for loop to iterate over the range of numbers from 1 to 100.
- Inside the loop, check if the current number is even.
- If the number is even, add it to a running total.
- After the loop, print the final sum.

## Lab 2 Sign-Off
- Submit your ipyn (Jupyter Lab notebook) file which shows your code, explanation and output for all the questions.



[def]: https://github.com/user-attachments/assets/4aba63ec-2b16-40a4-83ec-71e90f91c69a
[def2]: image.png