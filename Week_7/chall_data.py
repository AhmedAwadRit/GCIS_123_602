"""

This module takes a file called "chall_data.csv" and runs it through the function that prints the GPA in the csv file

"""


import csv

def Print_Gpa(file_area):
    """
    This function opens a csv file and prints the elements found in them.
    
    """
    with open(file_area, "r") as file_data:
        data = csv.reader(file_data)
        for element in data:
            print(element[3])

def main():
    Print_Gpa("chall_data.csv")

main()