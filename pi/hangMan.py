import random

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']


def pick_a_word():
    return random.choice(words)


def play():
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done')
            break
        if lives_remaining == 0:
            print('You are Hung!')
            print('The word was: ' + word)
            break


def get_guess(word):
    return 'a'


def process_guess(guess, word):
    global lives_remaining
    lives_remaining = lives_remaining - 1
    return False
