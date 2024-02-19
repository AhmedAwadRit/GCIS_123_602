"""

This module explains how we can use (+=) to explain x = x+y

"""

num = 1
total = 0
while num <= 10:
    total += num
    num += 1
print(total)