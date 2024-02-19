"""

This module helps introduce intervals in if statements

"""


def f(x):
    if x >=25:
        total = x**2
    elif x > 2:
        total = x * (x - 4 + 3*x**2)
    else:
        total = -2*x**2
    print(f"f{x} = {total}")

def main():
    x = int(input("What is your number: "))
    f(x)

if __name__ == "__main__":
    main()