"""

This module defines a function that takes two parameters. The product is then displayed.

"""

def mult(first_value,second_value):
    """
    
    This function will take parameters and display the multiplication of the values in those two parameters in 'product'
    
    mult(first_value,second_value)

    """

    product = first_value*second_value
    print(f"{first_value} * {second_value} = {product}")

def main():
    # The inputs of the two variables #
    uno = int(input("What is your first number: "))
    dos = int(input("What is your second number: "))
    # The multiplication function #
    mult(uno,dos)

# Main #
main()


    