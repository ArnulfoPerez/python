"""Hangman game"""
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

STRING00 = 'Welcome to the game, Hangman!'
STRING01 = 'I am thinking of a word that is '
STRING02 = ' letters long.'
STRING03 = '-------------'
STRING04 = 'You have '
STRING05 = ' guesses left.'
STRING06 = 'Available letters: '
STRING07 = 'abcdefghijklmnopqrstuvwxyz'
STRING08 = 'Please guess a letter: '
STRING09 = 'Good guess: '
STRING10 = "Oops! You've already guessed that letter: "
STRING11 = 'Oops! That letter is not in my word: '
STRING12 = 'Congratulations, you won!'
STRING13 = 'Sorry, you ran out of guesses. The word was '
MAXIMUM = 8

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    _word_list = line.split()
    print("  ", len(_word_list), "words loaded.")
    return _word_list

def chooseWord(word_list):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(word_list)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secret_word, letters_guessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secret_word:
        if not letter in letters_guessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    acc = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            acc += letter + ' '
        else:
            acc += '_ '
    return acc


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for guess in lettersGuessed:
        letters = letters.replace(guess, '')
    return letters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    def print_divider(message):
        """ prints marker between plays """
        _divider = STRING03
        print(_divider)
        print(message)
    class Game:
        'Common base class for hangman game'
        
        _prompt = STRING08
        _good = STRING09
        _repeat = STRING10
        _fail = STRING11
        _success = STRING12
        _game_over = STRING13
        
        def __init__(self, secret_word):
            self._secret_word = secret_word
            self._letters_guessed = ''
            self._length = len(secret_word)
            self._letters = STRING07
            self._guesses = MAXIMUM
            
        def print_status(self, message, guess):
            """ prints the status of the guess """
            self._letters_guessed = self._letters_guessed + guess
            self._letters = self._letters.replace(guess, '')
            self._print_message(message)
            
        def _print_message(self, message):
            """ prints current guess """
            print(message + 
                  getGuessedWord(self._secret_word, self._letters_guessed))
            
        def get_guess(self):
            """ prompt user for guess """
            print(STRING04+str(self._guesses)+STRING05)
            print(STRING06 + self._letters)
            raw = input(Game._prompt)
            return raw.lower()
        
        def play(self):
            """ play a session of hangman"""
            print(STRING00)
            print_divider(STRING01+str(self._length)+STRING02)    
            while True:
                guess = self.get_guess()
                if guess in self._letters_guessed:
                    self._print_message(Game._repeat)
                elif guess in self._secret_word:
                    self.print_status(Game._good, guess)
                    if isWordGuessed(self._secret_word, self._letters_guessed):
                        print_divider(Game._success)
                        break
                else:
                    self.print_status(Game._fail, guess)
                    self._guesses -= 1
                    if self._guesses == 0:
                        print_divider(Game._game_over + self._secret_word)
                        break
                print_divider("")
        
    game = Game(secretWord)
    game.play()


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

hangman(chooseWord(wordlist).lower())
