"""

This module takes input from the user, then adds it into the file "example.txt"

"""


file_path = "example.txt"

with open(file_path, "a") as file_data:
    user_input = input("What do you want to write: ")
    file_data.write(f"{user_input}\n")