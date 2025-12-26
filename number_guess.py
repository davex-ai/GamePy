import random
print("=" * 40)
print("Welcome to the Number Guessing Game🎉🎉")
print("=" * 40)
try:
    length = int(input("Set your length: "))

    def guess(x):
        return random.randint(1, x)

    answer = guess(length)
    tries = 0

    choice = 0
    try:
        choice = int(input(f"Guess the Number between 1 - {length}: "))
    except ValueError:
        print("Enter an integer value")

    while choice != answer:
        if choice > length:
            choice = int(input(f"{choice} is out of range \nTry Again, 1 - {length}: "))
            tries +=1
        elif choice > answer:
            choice = int(input("TOO BIG\nTry Again: "))
            tries +=1
        elif choice < answer:
           choice = int(input("TO SMALL\nTry Again: "))
           tries += 1

    print(f"Correct!! It took you {tries} tries")
except KeyboardInterrupt:
    print("\nPrograms was Interrupted")
except ValueError:
    print("Enter an integer value")