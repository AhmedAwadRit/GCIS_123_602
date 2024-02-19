"""

This module helps introduce what quotations and (\n, \t) and how \ can be used to stop a quotation from giving an error and printing.

"""


def space():
    print("")

one = 'She said "I don\'t like boroccoli."'
one_2 = "She said \"I don't like broccoli.\""

two = "A\tB\tC\tD\tE"

three = "This/is\\a/test\."

four = "This \nis a new string \nwith newlines in \nthe middle"

five = 'She\tsaid "I \ \ndon\'t \tlike \ \nbroccoli.'

print(one)
print(one_2)
space()
print(two)
space()
print(three)
space()
print(four)
space()
print(five)