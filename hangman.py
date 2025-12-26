import random
import string

words = ["mymy", "sigh", "github", "love", "code", "flower"]
def get_valid_word(words):
    word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()


    while len(word_letters) > 0:
        print("You have used letters " +" ".join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Word is: " + " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
        elif user_letter in used_letters:
            print(f"You already guessed {user_letter}")
        else:
            print("Invalid guess")
    # if used_letters == word:
    #     print("You Won🎉🎉")

hangman()