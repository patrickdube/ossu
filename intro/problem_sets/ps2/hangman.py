# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    has_won_flag = True
    for letter in secret_word:
        if letter not in letters_guessed:
            has_won_flag = False
    return has_won_flag


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_progress = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word_progress += letter
        else:
            word_progress += "*"
    return word_progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all_letters = string.ascii_lowercase
    available_letters = ""
    for letter in all_letters:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters


def ask_user_guess(with_help):
    valid_guess = False
    valid_letters = string.ascii_letters
    guess = input("Enter your letter: ")

    if with_help:
        valid_letters += "!"

    while not valid_guess:
        valid_guess = True
        if len(guess) > 1:
            print("Invalid letter or command.")
            valid_guess = False
        elif (guess not in valid_letters) or guess == "":
            print("Invalid letter or command.")
            valid_guess = False
        if valid_guess:
            break
        guess = input("Enter a valid letter: ")

    return guess


def get_consonants():
    consonants = []
    for letter in string.ascii_letters:
        if letter not in "aeiouAEIOU":
            consonants.append(letter)
    return consonants


def user_help(secret_word, available_letters):
    choose_from = ""
    for letter in secret_word:
        if letter in available_letters:
            choose_from += letter
    randomIndex = random.randint(0, len(choose_from) - 1)
    revealed_letter = choose_from[randomIndex]

    return revealed_letter


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_guesses = 10
    letters_guessed = []
    consonants = get_consonants()
    vowels = "aeiouAEIOU"

    print("The secret word has ", len(secret_word), " letters.")

    while num_guesses > 0:
        print("--------------------------------------")
        print("You have", num_guesses, "guesses.")
        print("Following are the available letters: ", get_available_letters(letters_guessed))

        guess = ask_user_guess(with_help)

        if guess != "!":
            letters_guessed.append(guess)

        elif guess == "!":
            if num_guesses >= 3:
                revealed_letter = user_help(secret_word, get_available_letters(letters_guessed))
                letters_guessed.append(revealed_letter)
                num_guesses -= 3
                print(f"The revealed letter is {revealed_letter}.\n {get_word_progress(secret_word, letters_guessed)}")
            else:
                print("You do not have enough guesses for this command.")

        if guess not in secret_word and guess != "!":
            print(f"Your guess {guess} is not in the secret word.\n {get_word_progress(secret_word, letters_guessed)}")
            if guess in consonants:
                num_guesses -= 1
            elif guess in vowels:
                num_guesses -= 2
        elif guess in secret_word and guess != "!":
            print(f"Your guess {guess} is in the secret word.\n {get_word_progress(secret_word, letters_guessed)}")

        if has_player_won(secret_word, letters_guessed):
            total_score = (num_guesses + (4 * len(set(secret_word))) + (3 * len(secret_word)))
            print("--------------------------------------")
            print(f"You have won! The word was {secret_word}.\n Your final score is: {total_score}.")
            break

    if num_guesses <= 0:
        print("--------------------------------------")
        print(f"You have lost! The word was {secret_word}.")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
