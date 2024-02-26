"""

This module goes into file "example_csv.csv" and adds all the numbers in position 2.

"""


import csv

file_area = "example_csv.csv"
total = 0

with open(file_area, "r") as file_data:
    data_reader = csv.reader(file_data)
    for element in data_reader:
        total = total + int(element[2])

print(f"Your total = {total}")