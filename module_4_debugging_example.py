
# module_4_debugging_example.py
# A simple Python script with an intentional logical error for debugging practice in VSCode

def find_max(numbers):
    max_number = numbers[0]  # Assume first number is the max
    for number in numbers[1:]:
        if number > max_number:
            max_number = number  # Update max_number if current number is greater
    return max_number

# Intentional error: 'numbers_list' includes a string which should cause a comparison error during execution
numbers_list = [10, 65, 22, '11', 3]
print("The maximum number is:", find_max(numbers_list))
