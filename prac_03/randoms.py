import random

print(random.randint(5, 20))  # line 1
"""
14,14,13,6,11,19
The smallest number is 6 and the biggest number is 19.
"""

print(random.randrange(3, 10, 2))  # line 2
"""
9,5,5,3,9,5
The smallest number is 3 and the largest number is 9.
line 2 cannot product number 4. 
"""

print(random.uniform(2.5, 5.5))  # line 3
"""
3.4402960838667216, 2.860975322065884, 3.6309076884606712, 3.029305271873044, 4.341341464503236, 3.8677190200680767
The smallest number is 2.860975322065884 and the largest number is 4.341341464503236
"""

print(random.randint(0, 100))
"""
37,19,65,17,40,31
The smallest number is 17 and the largest number is 65
"""