"""
I am going to make a complete game of Hangman. A random word will be taken from a list
the user will be able to give a letter or solve.
    - We will have 3 lives.
    - If the letter is not part of the word, one life is lost, if it is part of the word, the hyphens will be replaced by that letter.
    - If the word is not correct, the game is over.
"""

import random as rd


list=["code", "python","github","learning"] #.....
rWord= rd.choice(list).upper()

yourWord="" 
game="playing"
lives=3

while game=="playing":

    print()
    
    for letter in rWord:
        if letter in yourWord:
            print(letter, end="") # I use the "end= "" " to avoid the line break. 
        else:
            print("_",end="")
    print()
    print() 

    print("You have a total of: {} lives".format(lives)) 

    yourLetter=input("Enter a letter or solve: ").upper()
    yourWord+=yourLetter.upper()

    ## CONDITIONS ##
    isletter= len(yourLetter)<=1
    issolve= len(yourLetter)>1

    if lives<=0: 
        game="Over"
        print("You have no lives. The game is over")

    elif isletter is True and yourLetter not in rWord:
        lives-=1
        print("WRONG. You lose a life")

    elif issolve is True and yourLetter!=rWord:
        game="Over"
        print("Wrong word. Your word: {}. | the word: {}".format(yourWord,rWord))
        print()
        print("The game is OVER")

    elif yourLetter==rWord:
        game="Over"
        print()
        print(rWord)
        print()
        print("You WON the game. Thank's for playing!")