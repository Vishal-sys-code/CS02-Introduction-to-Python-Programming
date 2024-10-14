def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: File not found."
    except IOError:
        return "Error: Could not read file."
    
# Test case
print(read_file("nonexistent_file.txt"))  # Output: Error: File not found.