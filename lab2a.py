# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file
a=input("enter a number: ")
#print(type(a))
x= int(a)
#print(type(x))
#if x>=6:
 #   print("x is greater then 6!")
#x is greater than or equal to 4 and x is less than 12.


if x >= 4 and x < 12:
    print("x is between 4 and 12 (inclusive of 4 and exclusive of 12).")
else:
    print("x is not in the range.")


