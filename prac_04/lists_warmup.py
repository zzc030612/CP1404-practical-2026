# Initial list
numbers = [3, 1, 4, 1, 5, 9, 2]

# Predictions for the expressions
# 1. numbers[0] -> 3 (first element of the list)
# 2. numbers[-1] -> 2 (last element of the list)
# 3. numbers[3] -> 1 (fourth element of the list, index starts at 0)
# 4. numbers[:-1] -> [3, 1, 4, 1, 5, 9] (all elements except the last one)
# 5. numbers[3:4] -> [1] (slice from index 3 to 4, not including 4)
# 6. 5 in numbers -> True (5 is in the list)
# 7. 7 in numbers -> False (7 is not in the list)
# 8. "3" in numbers -> False ("3" is a string, not an integer)
# 9. numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] (concatenates the lists)

# Testing predictions in the Python console:
print(numbers[0])       # Output: 3
print(numbers[-1])      # Output: 2
print(numbers[3])       # Output: 1
print(numbers[:-1])     # Output: [3, 1, 4, 1, 5, 9]
print(numbers[3:4])     # Output: [1]
print(5 in numbers)     # Output: True
print(7 in numbers)     # Output: False
print("3" in numbers)   # Output: False
print(numbers + [6, 5, 3])  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# 1. Change the first element of numbers to "ten" (string)
numbers[0] = "ten"
print(numbers)

# 2. Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

# 3. Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4. Print whether 9 is an element of numbers
print(9 in numbers)