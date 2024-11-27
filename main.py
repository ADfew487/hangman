import random
from game.mechanics import play_hangman

if __name__ == "__main__":
    print("Добро пожаловать в игру 'Виселица'!")
    words = ["python", "developer", "algorithm", "function", "variable"]
    secret_word = random.choice(words)
    play_hangman(secret_word)
