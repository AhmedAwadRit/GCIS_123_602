file_path = "data.txt" ## Relative Path
file_data = open(file_path) ## Connect to the file
data = file_data.read() ## Read the content of the file
print(data)
file_data.close() ## Close the file

