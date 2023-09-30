import numpy as np
import pandas as pd

# Define the word database using a pandas DataFrame
word_data = pd.DataFrame({
    'Word': ["apple", "banana", "cat", "dog", "elephant", "flower", "grape", "house", "ice cream", "jacket"],
    'Difficulty': ["Easy"] * 10,
    'Meaning': ["A fruit", "A fruit", "A domestic animal", "A domestic animal", "A large mammal", "A plant", "A fruit", "A building", "A frozen dessert", "A type of clothing"],
    'Hint': ["It's red or green", "It's yellow", "It says 'meow'", "It says 'woof'", "Has a trunk", "Blooms in gardens", "Used to make wine", "Where you live", "Great on a hot day", "Wear it in cold weather"]
})

# Add more words for different difficulty levels
medium_words = pd.DataFrame({
    'Word': ["computer", "umbrella", "mountain", "television", "keyboard", "guitar", "rainbow", "elephant", "balloon", "hamburger"],
    'Difficulty': ["Medium"] * 10,
    'Meaning': ["An electronic device", "Keeps you dry", "A large landform", "Entertainment device", "Input device", "Musical instrument", "Colorful arch", "A large mammal", "Floats in the sky", "A type of sandwich"],
    'Hint': ["Used for work", "Shields from rain", "Climb it", "Watch shows on it", "Typing tool", "Strings and frets", "After rain", "Has a trunk", "Inflates with gas", "Beef patty in a bun"]
})

hard_words = pd.DataFrame({
    'Word': ["university", "extraterrestrial", "antidisestablishmentarianism", "xylophone", "serendipity", "floccinaucinihilipilification", "pneumonoultramicroscopicsilicovolcanoconiosis", "hippopotomonstrosesquipedaliophobia", "supercalifragilisticexpialidocious", "photosynthesis"],
    'Difficulty': ["Hard"] * 10,
    'Meaning': ["Higher education institution", "Alien", "Opposition to church-state separation", "Musical instrument", "Happy accident", "Estimating as worthless", "A lung disease", "Fear of long words", "Longest word in Mary Poppins", "Process of making food from light"],
    'Hint': ["Learn and research here", "Not from Earth", "Big word for church-state", "Sounds with wooden bars", "Unexpected luck", "Saying something is useless", "Very long lung disease", "Scared of long words", "Song from a movie", "Plants do it with sunlight"]
})

# Concatenate the dataframes to create the word database
word_database = pd.concat([word_data, medium_words, hard_words])

# Function to spin the Word Wheel
def spin_word_wheel():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return np.random.choice(list(alphabet))

# Function to play the game
import numpy as np
import pandas as pd

# ... (rest of your code)

# Function to play the game
def play_game(difficulty):
    words_to_guess = word_database[word_database['Difficulty'] == difficulty]
    score = 0

    for _, row in words_to_guess.iterrows():
        word = row['Word']
        meaning = row['Meaning']
        hint = row['Hint']
        guesses_left = len(word)
        guessed_letters = []

        print(f"Guess this {len(word)}-letter word: {'*' * len(word)}")
        print(f"Meaning: {meaning}")
        print(f"Hint: {hint}")

        while guesses_left > 0:
            print(f"Guesses left: {guesses_left}")
            print(f"Guessed letters: {' '.join(guessed_letters)}")

            guess = input("Enter a letter or the entire word: ").lower()

            if guess == 'exit':
                return  # Exit the current game

            if len(guess) == 1:
                if guess in guessed_letters:
                    print("You already guessed that letter.")
                elif guess in word:
                    print("Correct!")
                    guessed_letters.append(guess)
                    word_display = ''.join([letter if letter in guessed_letters else '*' for letter in word])
                    print(f"Word: {word_display}")

                    if '*' not in word_display:
                        score += 1
                        print("Word completed!")
                        break
                else:
                    print("Incorrect guess.")
                    guesses_left -= 1
            elif guess == word:
                print("Correct!")
                score += 1
                break
            else:
                print("Incorrect guess.")
                guesses_left -= 1

        if guesses_left == 0:
            print(f"Out of guesses! The word was: {word}")

    print(f"Game over! Your score for {difficulty} level: {score}/{len(words_to_guess)}")

# Get player's name
player_name = input("Enter your name: ")

# Main game loop
while True:
    print(f"Welcome, {player_name}, to LexiGuess: The Word Explorer!")
    print("Select a difficulty level: Easy, Medium, Hard")
    print("Type 'exit' to quit.")

    choice = input("Enter your choice: ").capitalize()

    if choice == 'Exit':
        print(f"Thanks for playing, {player_name}!")
        break
    elif choice in ["Easy", "Medium", "Hard"]:
        play_game(choice)
    else:
        print("Invalid choice. Please select a valid difficulty level or type 'exit' to quit.")
