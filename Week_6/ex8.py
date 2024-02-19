"""

This module checks if the inputted number is an armstrong number or not

"""


num = int(input("What is your number: "))
sum = 0
saved_num = num

while num > 0:
    last_digit = num % 10
    sum += last_digit**3
    num = num // 10

if saved_num == sum:
    print("Your number is an armstrong number.")
else:
    print("Your number is not an armstrong number")

