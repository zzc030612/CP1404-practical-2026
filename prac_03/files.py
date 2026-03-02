# Task 1: Ask the user for their name and write it to a file called 'name.txt'
name = input("Enter your name: ")
file = open("name.txt", "w")  # Open the file in write mode
file.write(name)  # Write the name to the file
file.close()  # Close the file

# Task 2: Read the name from 'name.txt' and print a greeting
file = open("name.txt", "r")  # Open the file in read mode
name = file.read().strip()  # Read the name from the file and use strip() to remove possible line breaks
file.close()  # Close the file
print(f"Hi {name}!")  # Print the greeting with the name from the file

# Task 3: Open 'numbers.txt', read the first two numbers and print their sum
with open("numbers.txt", "r") as file:  # Use 'with' to automatically handle closing the file
    first_number = int(file.readline())  # Read the first line and convert it to an integer
    second_number = int(file.readline())  # Read the second line and convert it to an integer
    result = first_number + second_number  # Add the two numbers together
print(result)  # Print output

# Task 4: Open 'numbers.txt' and calculate the total of all the numbers
total = 0
with open("numbers.txt", "r") as file:  # Use 'with' to open the file
    for line in file:  # Iterate through each line in the file
        total += int(line)   # Convert the numbers in each line to integers and accumulate them
print(total)  # Print output summation