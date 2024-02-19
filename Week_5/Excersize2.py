"""

This module helps show how to conduct >, >= in if statements.
It also introduces the idea of (__name__ == "__main__") to prevent the incorrect output of main in another file

"""


def temp(x):
    if x > 80:
        print("It is a very hot day!")
    elif x >= 40:
        print("It is a beautiful day outside")
    else:
        print("It is a cold day")

def main():
    x = int(input("What is the temperature: "))
    temp(x)

if __name__ == "__main__":
    main()