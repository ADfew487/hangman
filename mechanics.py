def display_word(secret_word, guessed_letters):
    """Показывает текущее состояние слова с учетом угаданных букв."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

def play_hangman(secret_word):
    """Основной игровой цикл 'Виселицы'."""
    guessed_letters = set()
    attempts = 7  # Максимальное количество ошибок
    print("\n Угадайте слово!")

    while attempts > 0:
        print("\n Слово:", display_word(secret_word, guessed_letters))
        print(f"Осталось попыток: {attempts}")
        guess = input("Введите букву: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Пожалуйста, введите одну букву.")
            continue

        if guess in guessed_letters:
            print("Вы уже пробовали эту букву.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Правильно! Буква '{guess}' есть в слове.")
        else:
            attempts -= 1
            print(f"Ошибка! Буквы '{guess}' нет в слове.")
        
        if all(letter in guessed_letters for letter in secret_word):
            print("\n Поздравляем, вы угадали слово:", secret_word)
            break
    else:
        print("\n Вы проиграли. Слово было:", secret_word)
