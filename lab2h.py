# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use while loops.
# Usage: ./lab2h.py

# TO DO 1: 
# Creat variable timer.
# The value of timer should initially be 10.
# Use a while loop to create program that counts down from 10 with timer to 1.
# When you reach 1 end the loop and print blast off!
# Initialize the timer
timer = 10

# Countdown using a while loop
while timer > 0:
    print(timer)
    timer -= 1  # Decrease the timer by 1

# Print the final message
print("Blast off!")
