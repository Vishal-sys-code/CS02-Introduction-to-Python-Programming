# Threads in Python

Threads in Python are a way to achieve concurrency, allowing multiple operations to run simultaneously within a single process. This is particularly useful for I/O-bound tasks, such as network requests or file operations, where waiting for external resources can lead to idle time. However, Python's Global Interpreter Lock (GIL) can limit the effectiveness of threads for CPU-bound tasks.

## Definition of Threads

A thread is a lightweight process that can run concurrently with other threads within the same application. Each thread shares the same memory space but maintains its own stack and local variables. This allows threads to communicate with each other easily, but it also introduces potential issues, like race conditions and deadlocks.

### Key Points

- **Concurrency vs. Parallelism**: Concurrency allows multiple tasks to make progress at the same time, while parallelism means executing multiple tasks simultaneously.
- **Global Interpreter Lock (GIL)**: In CPython (the most common Python implementation), the GIL prevents multiple native threads from executing Python bytecodes simultaneously, which can be a bottleneck for CPU-bound programs.

## Basic Threading Example

You can use the `threading` module in Python to create and manage threads. Here’s a simple example demonstrating how to create and start threads:

```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)  # Simulate a time-consuming task

def print_letters():
    for letter in 'abcde':
        print(f"Letter: {letter}")
        time.sleep(1)  # Simulate a time-consuming task

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Done!")
```