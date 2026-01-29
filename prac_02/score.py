"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def determine_score_result(score):
    """Determine the result for the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    """Main function to handle user and random scores."""
    # User score
    user_score = float(input("Enter score: "))
    user_result = determine_score_result(user_score)
    print(f"User score {user_score} is {user_result}")
    if user_result == "Excellent":
        print("You get a prize!")

    # Random score
    random_score = random.randint(0, 100)
    random_result = determine_score_result(random_score)
    print(f"Random: {random_score} = {random_result}")


main()