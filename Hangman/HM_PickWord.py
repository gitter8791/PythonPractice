#buil hanging man game. part 1.
'''
This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a random word from a list of words 
from the SOWPODS dictionary. Download this file and save it in the same directory as your Python code. 
This file is Peter Norvig’s compilation of the dictionary of words used in professional Scrabble tournaments. 
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.
'''

import random

def f_pick_random_word():
    lWordList =[]
    with open("Resource\sowpods.txt", "r") as e_open_file:
        for sSingleWord in e_open_file.readlines():
            lWordList.append(sSingleWord.strip())
    sWordOfChoice = random.choice(lWordList)
    return (sWordOfChoice)

def main():
    pass

    print (f_pick_random_word())

if __name__ == '__main__':
    main()
