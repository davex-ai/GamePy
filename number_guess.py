import random

def guess(x):
    return random.randint(1, x)

answer = guess(100)
tries = 0
print("=" * 40)
print("Welcome to the Number Guessing Game🎉🎉")
print("=" * 40)
choice = int(input("Guess the Number between 1 - 100: "))
while choice != answer:
    if choice > answer:
        choice = int(input("TOO BIG\nTry Again: "))
        tries +=1
    elif choice < answer:
       choice = int(input("TO SMALL\nTry Again: "))
       tries += 1
    else:
        print("Invalid Input")
if choice == answer:
    print(f"Correct!! It took you {tries} tries")