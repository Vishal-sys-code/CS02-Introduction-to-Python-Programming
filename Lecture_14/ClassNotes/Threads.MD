# **Threads**

Threads in Python are a way to achieve concurrency, allowing multiple operations to run simultaneously within a single process. This is particularly useful for I/O-bound tasks, such as network requests or file operations, where waiting for external resources can lead to idle time. However, Python's Global Interpreter Lock (GIL) can limit the effectiveness of threads for CPU-bound tasks.

A flow of execution, like a seperate order of instructions. However each thread takes a turn running to achieve concurrency.

The GIL (locks) allows only one thread to hold the control of the python interpreter at anyone time.

**CPU Bound:** Program/task spends most of its time watching for intervals events(CPU intensive) use multiprocessing
**I/O Bound:** Program/task spends its time wasting for external events(user input, webscraping) use multithreading.

## **Definition of Threads**

A thread is a lightweight process that can run concurrently with other threads within the same application. Each thread shares the same memory space but maintains its own stack and local variables. This allows threads to communicate with each other easily, but it also introduces potential issues, like race conditions and deadlocks.

### **Key Points**

- **Concurrency vs. Parallelism**: Concurrency allows multiple tasks to make progress at the same time, while parallelism means executing multiple tasks simultaneously.
- **Global Interpreter Lock (GIL)**: In CPython (the most common Python implementation), the GIL prevents multiple native threads from executing Python bytecodes simultaneously, which can be a bottleneck for CPU-bound programs.

## **Basic Threading Example**

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

## **Explanation of the Code**
* **Importing Modules:** We import the threading module to work with threads and time to simulate delays.
* **Defining Functions:** Two functions, print_numbers and print_letters, are defined. Each prints a sequence of numbers or letters with a delay to mimic a time-consuming operation.
* **Creating Threads:** We create two threads, `thread1` and `thread2`, specifying the target function for each.
* **Starting Threads:** The `start()` method is called on both threads, which begins their execution.
* **Joining Threads:** The `join()` method is called to wait for both threads to complete before printing "Done!".

## **Thread Safety**
When using threads, it's important to ensure thread safety, especially when threads access shared data. You can use locks to prevent race conditions:

```py
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        with lock:  # Ensure only one thread can access this block at a time
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")
```

## **Summary**
Threads in Python provide a way to achieve concurrency, especially for I/O-bound tasks. Using the threading module, you can create, start, and manage threads easily. However, be mindful of thread safety when accessing shared data to avoid race conditions.