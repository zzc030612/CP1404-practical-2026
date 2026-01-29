"""
Program to calculate the total price for a number of items, applying a discount if the total is over $100.
"""

num_items = int(input("Number of items: "))

while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

total_price = 0
for i in range(num_items):
    price = float(input(f"Price of item {i + 1}: "))
    total_price += price

if total_price > 100:
    total_price *= 0.9  # Apply 10% discount

print(f"Total price for {num_items} items is ${total_price:.2f}")