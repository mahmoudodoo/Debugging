
# module_5_advanced_debugging_example.py
# This script includes scenarios ideal for applying advanced debugging techniques covered in this module

import threading
import time

# A simple function to demonstrate multi-threading debugging
def worker(delay, run_event):
    while run_event.is_set():
        print(f"Working...{threading.current_thread().name}")
        time.sleep(delay)

# Setting up threading
run_event = threading.Event()
run_event.set()
worker_thread = threading.Thread(target=worker, args=(1, run_event))

print("Starting thread")
worker_thread.start()

# Simulating work before stopping the thread
time.sleep(5)

# Stopping the thread
print("Stopping thread")
run_event.clear()
worker_thread.join()
print("Thread stopped")
