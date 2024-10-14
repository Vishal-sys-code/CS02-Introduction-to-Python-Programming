import random

def random_examples():
    # 1. Generate a random float between 0.0 and 1.0
    rand_float = random.random()
    print(f"Random float: {rand_float}")

    # 2. Generate a random integer between 1 and 10
    rand_int = random.randint(1, 10)
    print(f"Random integer (1-10): {rand_int}")

    # 3. Generate a random integer using randrange
    rand_range = random.randrange(1, 20, 2)  # Odd numbers between 1 and 19
    print(f"Random odd integer (1-19): {rand_range}")

    # 4. Randomly select an element from a list
    choices = ['apple', 'banana', 'cherry', 'date']
    rand_choice = random.choice(choices)
    print(f"Random choice from list: {rand_choice}")

    # 5. Shuffle a list
    random.shuffle(choices)
    print(f"Shuffled list: {choices}")

    # 6. Sample 2 unique elements from a list
    sample = random.sample(choices, 2)
    print(f"Sampled elements: {sample}")

# Run the example
random_examples()