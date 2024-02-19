"""

This module don't work. It's purpose was to explain the reason of using "break"

"""

number = 8
while number > 0:
    if number == 5:
        number = number - 1
        break
    print(number)
    number - number - 1

number = int(input("What is your number: "))
sum = 10

while True:
    number = int(input("What is your number: "))
    if number < 0:
        break

sum = sum + number
print("end")