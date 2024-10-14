def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Please provide numbers."
    else:
        return f"The result is: {result}"

# Test cases
print(safe_divide(10, 2))  # Output: The result is: 5.0
print(safe_divide(10, 0))  # Output: Error: Division by zero is not allowed.
print(safe_divide(10, 'a'))  # Output: Error: Please provide numbers.