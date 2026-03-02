"""
Wimbledon Champions Data Analysis
Estimate: 45 minutes
Actual:   60 minutes
"""


def load_data(filename):
    """Load Wimbledon data from CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
    return [line.strip().split(',') for line in lines[1:]]  # Skip header


def get_champions(data):
    """Return dictionary of champions and their win counts."""
    champions = {}
    for row in data:
        name = row[2]  # Champion name column
        champions[name] = champions.get(name, 0) + 1
    return champions


def get_countries(data):
    """Return sorted set of champion countries."""
    countries = {row[1] for row in data}  # Country column
    return sorted(countries)


def display_results(champions, countries):
    """Display processed data in required format."""
    print("Wimbledon Champions:")
    for name, count in sorted(champions.items()):
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(', '.join(countries))


def main():
    """Main program workflow."""
    data = load_data('wimbledon.csv')
    champions = get_champions(data)
    countries = get_countries(data)
    display_results(champions, countries)


if __name__ == "__main__":
    main()