def process_numbers(numbers):
    results = []
    for number in numbers:
        try:
            result = 100 / number
        except ZeroDivisionError:
            results.append("Error: Division by zero.")
        except TypeError:
            results.append("Error: Invalid type.")
        else:
            results.append(result)
    return results

# Test case
print(process_numbers([10, 0, 'a', 5]))  
# Output: [10.0, 'Error: Division by zero.', 'Error: Invalid type.', 20.0]