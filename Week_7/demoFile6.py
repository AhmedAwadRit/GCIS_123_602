file_path = "data.txt"

with open(file_path, "w") as file_data: ### "w" means overwrite
    file_data.write("Ramadan is soon")

with open(file_path, "a") as file_data: ### "a" means just write
    file_data.write("\nRamadan is very soon")
