file_path = "data.txt" ## Relative Path

# file_data = open(file_path) ## Connect to the file
# data = file_data.read() ## Read the content of the file
# print(data)
# file_data.close() ## Close the file

with open(file_path) as file_data: ## Same as file_data = open(file_path), automatically closes
    data = file_data.read()
    print(data)

