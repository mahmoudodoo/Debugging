
# module_1_example.py
import pdb

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        pdb.set_trace()  # Intentional breakpoint for debugging
        total += num
    return total

numbers_list = [1, 2, "3", 4]  # Intentional bug: string in a list of integers
print(calculate_sum(numbers_list))
