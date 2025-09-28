#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    for ch in word:
        if letter == ch:
            inWord = True
        else:
            inWord = False
    """Returns boolean if letter is anywhere in the given word"""
    return False

def inSpot(letter, word, spot):
    correctLetter = word[spot]
    if letter == correctLetter:
        inSpot = True
    else:
        inSpot = False
    """Returns boolean response if letter is in the given spot in the word."""
    return False

def rateGuess(myGuess, word):
    feedback = ""
    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot) == True:
            feedback = feedback + myLetter.upper()
        elif inWord
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""


def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    print(todayWord)

    #User should get 6 guesses to guess

    #Ask user for their guess
    #Give feedback using on their word:





if __name__ == '__main__':
  main()
