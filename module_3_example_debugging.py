
# example_debugging.py
import logging
import pdb

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_product(numbers):
    pdb.set_trace()  # Breakpoint for debugging with pdb
    product = 1
    for number in numbers:
        product *= number
        logging.debug(f"Product after multiplying {number}: {product}")  # Debugging with logging
    return product

numbers_list = [2, 3, '4', 5]  # Intentional bug: '4' is a string
print(calculate_product(numbers_list))
