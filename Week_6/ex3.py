"""

This module writes a for loop which produces the output of a number squared.
It also introduces the concept of (end= ""), which adds whatever you want at the end of the print.

"""


# Write a for loop that produces the following output:
# 1 4 9 16 25 36 49 64 81 100


for num in range(1,11):
    v = num**2
    print(v, end=" ")
