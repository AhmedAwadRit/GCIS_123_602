"""
The following is an example of a docString that should be included in all your modules and all your activities
This program draws several text figures, including a diamond, an X, and a rocket ship.
(Version 1 with functions for structure.)
Question 1: Use functions to show structure and eliminate redundancy in your solution
For your code please create a module called version2.py
Question 2: can you draw the flow of the function's execution 
"""

### DEFINITIONS ###

def v():
    print(" \\    /")
    print("  \\  /")
    print("   \\/")

def down_v():
    print("   /\\")
    print("  /  \\")
    print(" /    \\")

def square():
    print("+------+")
    print("|      |")
    print("|      |")
    print("+------+")
    
### SHAPES ###

def draw_diamond():
    down_v()
    v()
    print()
    print(" DIAMOND \n\n")

def draw_x():
    v()
    down_v()
    print()
    print("THE LETTER 'X' \n\n")
 
def draw_rocket():
    down_v()
    square()
    print("| Dubai|")
    print("| Arab |")
    print("| UAE  |")
    square()
    down_v()
    print()
    print(" A ROCKET \n\n")
 
def main():
      draw_diamond()
      draw_x()
      draw_rocket()

### MAIN ###

main()