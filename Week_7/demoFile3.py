file_path = "data.txt" ## Relative Path

with open(file_path) as file_data:
    for line in file_data:
        print(line.strip())
        print("---------")
