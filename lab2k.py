# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: use for loop.
# Usage: ./lab2k.py

# TO DO 1: 
#Follow the instructions given in the README.md file.
fruits = ["apple", "banana", "cherry", "date"]

# Use a for loop to iterate over the list
#for fruit in fruits:
#    print(fruit)

#for loop is commonly used with range functions. Here's another example using the range function to print numbers from 0  to 5.

#for i in range(5):
#    print(i)
# Initialize a variable to hold the sum of even numbers
total_sum = 0

# Use a for loop to iterate over the range from 1 to 100 (inclusive)
for num in range(1, 101):
    # Check if the current number is even
    if num % 2 == 0:
        # Add the even number to the total sum
        #print(num)
        total_sum += num

# Print the final sum
print("The sum of all even numbers from 1 to 100 is:", total_sum)
