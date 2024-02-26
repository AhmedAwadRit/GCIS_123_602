file_path = "data.txt"

with open(file_path) as file_data:
    data = file_data.readline()
    while True:
        d = next(data)
        if d is not None:
            print(d.strip())
        else:
            break

## YOU DONT NEED THIS CODE IT'S JUST YK WHY NOT ##