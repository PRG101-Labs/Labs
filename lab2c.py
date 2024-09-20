
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2
#
# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
# The final result should be:
# ---- is longer then ----
# If they are equal then print:
# ---- and ---- are equal.
# Get input from the user
str1 = input("Please enter the first sentence: ")
str2 = input("Please enter the second sentence: ")

# Compare the lengths of the two strings
if len(str1) > len(str2):
    print(f"{str1} is longer than {str2}!")
elif len(str1) < len(str2):
    print(f"{str2} is longer than {str1}!")
else:
    print(f"{str1} and {str2} are of equal length!")

