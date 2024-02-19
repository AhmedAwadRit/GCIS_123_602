"""

This module defines a function (is_Arm_num) and runs it through to check if the inputted value is an armstrong number, then returning if it's true or not

"""


def is_Arm_num(num):
    
    sum = 0
    saved_num = num

    while num > 0:
        last_digit = num % 10
        sum += last_digit**3
        num = num // 10
    
    return saved_num == sum

def main():
    num = int(input("What is your number: "))
    check = is_Arm_num(num)
    print(check)

if __name__ == "__main__":
    main()