# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Practice using if and else statments.
# Usage: ./lab2b.py

# TO DO 1:
# Follow the instructions given in the README.md file.
num = input("Please enter a 4-digit integer: ")

# Check if the input is a valid 4-digit integer
if num.isdigit() and len(num) == 4:
    if int(num) == 1984:
        print("George Orwell")
    else:
        print("Not quite right!")
else:
    print("Invalid input! Please enter a 4-digit integer.")
