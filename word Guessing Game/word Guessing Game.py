import random

# List of words to guess from
words = ["dsa", "java development", "python", "software engineering", "english", "machine learning", "dbms"]

# Choose a random word from the list
secret_word = random.choice(words)

# Create a list to store the guessed letters
guessed_letters = ["_"] * len(secret_word)

# Initialize the number of guesses
guesses = 0

print("Welcome to the word guessing game!")
print("I'm thinking of a word that has", len(secret_word), "letters.")

while True:
    # Print the current state of the guessed word
    print(" ".join(guessed_letters))

    # Ask the user for their guess
    user_guess = input("Enter a letter: ")

    # Increment the number of guesses
    guesses += 1

    # Check if the user's guess is in the secret word
    if user_guess in secret_word:
        # Reveal the correct letter in the guessed word
        for i in range(len(secret_word)):                                          
            if secret_word[i] == user_guess:
                guessed_letters[i] = user_guess
    else:
        print("Sorry, that letter is not in the word.")

    # Check if the user has guessed the entire word
    if "_" not in guessed_letters:
        print("Congratulations! You guessed the word in", guesses, "attempts.")
        break










