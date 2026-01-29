MIN_LENGTH = 12


def main():
    password = get_password()
    print_password_stars(password)


def get_password():
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print("Password too short")
        password = input("Enter password: ")
    return password


def print_password_stars(password):
    print('*' * len(password))


main()