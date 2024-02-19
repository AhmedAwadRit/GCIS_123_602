""" Create a function that will take two inputs and compute the addition of both of them """

def add():
    """
    
    This function will take two inputs ('x' and 'y') then add and display the addition in 'sum'

    add()
    
    """
    x = int(input("What is your first number: "))
    y = int(input("What is your second number: "))
    sum = x+y
    print(f"{x} + {y} = {sum}")

def main():
    add()

## MAIN ##

main()