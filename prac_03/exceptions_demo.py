"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   - A ValueError will occur if the user enters something that cannot be converted to an integer, such as a string or a float.

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError will occur if the user enters 0 as the denominator, because division by zero is not allowed.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, we can add a check to ensure the denominator is not zero before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:  # Check and prompt user until denominator is not zero
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")