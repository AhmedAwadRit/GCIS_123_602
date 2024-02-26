import csv

file_path = "data.csv"

with open(file_path, "r") as file_data:
    data_reader = csv.reader(file_data)
    print(list(data_reader)) ### List is added to convert so we can read

with open(file_path, "r") as file_data:
    data_reader = csv.reader(file_data)
    for element in data_reader: ### Will loop untill all the elements are printed
        print(element)
    
with open(file_path, "r") as file_data:
    data_reader = csv.reader(file_data)
    for element in data_reader:
        print(element[0]) ### '[0]' means print whatever is in value 0, first thing in a list is 0
