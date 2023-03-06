# Bagels

import random

NUM_DIGITS = 3
MAX_GUESSES = 5


def main():
    print('''Bagels, a deductive logic game.

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues: 
When I say: That means:

 Pico   -->     One digit is correct but in the wrong position.
 Fermi  -->     One digit is correct and in the right position.
 Bagels -->     No digit is correct.

 For example, if the secret number was 123 and your guess was 325, the
 clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # Main game loop
        # Store the secret three digit number
        secret_number = get_secret_number()
        print('I have tought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        number_of_guesses = 1
        while number_of_guesses <= MAX_GUESSES:
            guess = ''
            # Keeps looping until the guess is right
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(number_of_guesses))
                guess = input('Enter your guess: ')

            clues = get_clues(guess, secret_number)
            print(clues)
            number_of_guesses += 1

            if guess == secret_number:
                break  # If guess is correct break out of this loop
            if number_of_guesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answeer was {}.'.format(secret_number))

        # Ask the user to they want to continue or not
        print('Do you want to play again [Y/N]')
        if not input('>').lower().startswith('y'):
            break
    print('Thanks for playing.')


def get_secret_number():
    numbers = list('0123456789')  # Create a lsit of random numbers
    random.shuffle(numbers)  # Shuffles into random numbers

    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number


def get_clues(guess, secret_number):
    if guess == secret_number:
        return 'You gusse it right'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            # A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secret_number:
            # A correct digit in wrong place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # No correct digits
    else:
        # Sort the clues into alphabetical order so their original order dosent give information away
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()
