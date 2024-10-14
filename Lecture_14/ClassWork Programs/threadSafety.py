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