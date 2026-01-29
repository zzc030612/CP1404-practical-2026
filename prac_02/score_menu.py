def main():
    score = get_valid_score()
    choice = ""
    while choice != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_result(score))
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Goodbye!")
        else:
            print("Invalid choice")


def print_menu():
    print("\nMenu:\n(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")


def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print("*" * int(score))


main()