"# Reads the entire file into memory
with open('large_file.txt', 'r') as file:
    data = file.read().splitlines()
    for line in data:
        print(line)"
