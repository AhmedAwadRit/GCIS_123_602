"""
The following is an example of a docString that should be included in all your modules and all your activities
This program draws several text figures, including a diamond, an X, and a rocket ship.
(Version 1 with functions for structure.)
Question 1: Use functions to show structure and eliminate redundancy in your solution
For your code please create a module called version2.py
Question 2: can you draw the flow of the function's execution 
"""

def draw_diamond():
    print("   /\\")
    print("  /  \\")
    print(" /    \\")
    print(" \\    /")
    print("  \\  /")
    print("   \\/")
    print()

def draw_x():
    print(" \\    /")
    print("  \\  /")
    print("   \\/")
    print("   /\\")
    print("  /  \\")
    print(" /    \\")
    print()
 
def draw_rocket():
    print("   /\\")
    print("  /  \\")
    print(" /    \\")
    print("+------+")
    print("|      |")
    print("|      |")
    print("+------+")
    print("| Dubai|")
    print("| Arab |")
    print("| UAE  |")
    print("+------+")
    print("|      |")
    print("|      |")
    print("+------+")
    print("   /\\")
    print("  /  \\")
    print(" /    \\")
 
def main():
      draw_diamond()
      draw_x()
      draw_rocket()

main()