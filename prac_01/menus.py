"""
CP1404/CP5632 - Practical
Menu-driven program
"""

# Get the user's name
name = input("Enter name: ")

# Display menu
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

# Get initial choice
choice = input(">>> ").upper()

# Menu-driven loop
while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice")

    # Display menu and get choice again
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ").upper()

# Display finished message
print("Finished.")