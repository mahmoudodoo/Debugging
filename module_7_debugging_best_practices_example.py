
# module_7_debugging_best_practices_example.py
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def debug_example():
    logging.info("Starting debug example function")
    # Intentionally faulty code for demonstration purposes
    try:
        result = 10 / 0
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero")
    logging.info("Completed debug example function")

if __name__ == "__main__":
    debug_example()
