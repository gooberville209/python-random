import random

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

if __name__ == "__main__":
    min_value = int(input("Enter the minimum value: "))
    max_value = int(input("Enter the maximum value: "))

    random_num = generate_random_number(min_value, max_value)
    print(f"Random number between {min_value} and {max_value}: {random_num}")
