"""
CP1404/CP5632 - Practical
For loop
"""

# a. Counting in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b. Counting down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c. Print n stars on one line
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()

# d. Print n lines of increasing stars
for i in range(1, n + 1):
    print('*' * i)