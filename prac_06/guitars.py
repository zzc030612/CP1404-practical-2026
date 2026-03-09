from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My Guitars!")

    name = input("Enter guitar name: ")
    while name != "":
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        guitar_add = Guitar(name, year, cost)
        guitars.append(guitar_add)
        print(f"{guitar_add}, added")
        name = input("Enter guitar name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1992, 16035.40))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} (vintage)")
            else:
                print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")
    else:
        print("\nNo guitars :( Quick, go and buy one!")


main()