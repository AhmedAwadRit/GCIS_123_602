
"""

This module explains "continue" by passing through the loop when 'number' = 5

"""

number = 8

while number > 0:
    if number == 5:
        number = number - 1
        continue
    print(number)
    number = number - 1