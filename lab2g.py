# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.
rate1=.10
rate2=.25
rate1_single_limit= 32000
rate1_married_limit= 64000

income= float(input("Please enter your income in thousands: "))
status= input("Enter your status as single or married:")
tax1=0.0
tax2=0.0
if status=="single":
    if income<=rate1_single_limit:
        tax1=rate1*income
    else:
        tax1= rate1* rate1_single_limit
        tax2=rate2*(income-rate1_single_limit)  
else:
    if income<=rate1_married_limit:
        tax1=rate1*income
    else:
        tax1= rate1* rate1_married_limit
        tax2=rate2*(income-rate1_married_limit)
totalTax= tax1+tax2
print("The tax is", totalTax)


