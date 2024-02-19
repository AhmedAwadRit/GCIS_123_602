"""

This module explains how we can add several for loops in each other

"""


#hash = "#" * 10

#for m in range(1, 6):
#    print(hash)


### OR
    
for row in range(0,5):
    for column in range(0,10):
        print("#", end="")
    print("")