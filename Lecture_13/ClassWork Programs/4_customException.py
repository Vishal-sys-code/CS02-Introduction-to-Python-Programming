class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Error: Number cannot be negative.")
    return f"The number is: {number}"

# Test cases
try:
    print(check_positive(10))  # Output: The number is: 10
    print(check_positive(-5))  # Raises custom exception
except NegativeNumberError as e:
    print(e)  # Output: Error: Number cannot be negative.