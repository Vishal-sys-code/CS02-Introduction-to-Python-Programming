def read_integer():
    while True:
        try:
            value = int(input("Please enter an integer: "))
            return value
        except ValueError:
            print("That's not an integer! Please try again.")
        finally:
            print("Attempted to read an integer.")

# Uncomment the following line to test in an interactive environment
# print(read_integer())