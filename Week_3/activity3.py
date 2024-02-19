"""

This module defines a functon that calculates the area of a circle, then displays the value.

"""

from math import pi

def calc_area(radius_of_circle):
    """
    
    This function has one parameter (radius_of_circle). The value of the parameter is used to find the area of a circle (area)

    calc_area(radius_of_circle)
    
    """
    area = pi * radius_of_circle ** 2
    rounded_area = round(area, 2)
    print(f"Area = {rounded_area}")

def main():

    rad = int(input("What is the radius of the circle: "))
    calc_area(rad)

### MAIN ###
    
main()