# CS 122 fall 2023 project 5
# Author: Bardia Ahmadi Dafchahi
# Credits:
# Description: Create a simple guessing game


def get_word():
    """
    Prompts the user to enter a word

    Returns:
        guess_word (str)
    """
    guess_word = input("Enter a guess word (blank to quit): ").lower()
    return guess_word


def get_letter():
    """
    Prompts the user for a guess letter

    Return:
        the letter and if more than one character: returns ""
    """
    letter = input("Enter a guess letter (blank to quit): ").lower()
    if len(letter) > 1:
        letter = ""
        print("\t>Only enter a single letter")
    return letter


def check_letter(guess_word, matched, unmatched, letter):
    """
    Checks the inputted letter for matching any letter in the guess_word

    Args:
        guess_word (str): The guess word
        matched (str): the letters guessed so far that match the letters in the guess word
        unmatched (str): the letters guessed so far that didn't match the letters in the guess word
        letter (str): the guess letter to check

    Return:
        a tuple of matched and unmatched that either one can be empty but not both
    """
    guesses = matched + unmatched
    if not letter:
        return matched, unmatched
    outcome = ""
    if letter in guesses:  # to check for if already guessed
        outcome += "already guessed and "
    if letter in guess_word:  # found or not (found)
        if not outcome:
            matched += letter
    else:
        if not outcome:
            unmatched += letter
        outcome += "not "
    outcome += "found"

    print(f"\t> {letter} " + outcome)
    print(f"\t> Guesses so far: {matched + unmatched}")
    return matched, unmatched


def isdone(guess_word, matched):
    """
    Checks if all the letters are guessed

    Args:
        guess_word (str): the guess word
        matched (str): the string of the letters guessed

    Returns:
        True if all letters guessed and False else
    """
    for i in guess_word:
        if not (i in matched):
            return False
    return True


def start():
    """
    Main function

    Returns:
        None
    """
    guess_word = get_word()
    if not guess_word:
        return None
    matched_init = ""
    unmatched_init = ""
    counter = 0
    # Things to check for: blank, guessed, found, done
    while True:
        letter = get_letter()
        matched, unmatched = check_letter(guess_word, matched_init, unmatched_init, letter)
        if not letter:
            break
        matched_init, unmatched_init = matched, unmatched
        counter += 1
        if isdone(guess_word, matched_init):  # to check if all letters have been guessed (done)
            print(f"\t> All letters found")
            print("")
            print("*** Results ***")
            print(f"Word:\t\t{guess_word}")
            print(f"Matched:\t{matched_init}")
            print(f"Unmatched:\t{unmatched_init}")
            print(f"Guesses:\t{counter}")
            break


start()
