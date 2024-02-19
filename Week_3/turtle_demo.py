"""

This module imports 'Screen' and 'Turtle' from the turtle library, and defines functions in order to draw a square

"""

from turtle import Screen, Turtle

page = Screen()
cursor = Turtle()

page.title("Square")
page.bgcolor("thistle2")
cursor.pencolor("turquoise3")
cursor.shape("arrow")
cursor.pensize(6)
cursor.shapesize(3)

### DEFINITIONS ###

def movefront():
    """
    This function moves the pen (turtle) forwards by 100 pixels

    forward()
    
    """
    cursor.fd(100)

def rotateclock():
    """
    
    This function rotates the pen (turtle) clockwise by 90 degrees

    """
    cursor.right(90)

def square():
    """
    
    This function draws a square using turtle

    """
    movefront()
    rotateclock()
    movefront()
    rotateclock()
    movefront()
    rotateclock()
    movefront()

def main():
    square()
    page.exitonclick()

### MAIN ###
    
main()
    

