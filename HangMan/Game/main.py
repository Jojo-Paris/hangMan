from game import *
from time import sleep


def writeMain():

    print("\nWelcome to the HangMan Game!\n")
    sleep(3)
    print('''
        
        In this game a random word will be chosen by the CPU
        
        As the player, You will have 8 chances to guess before the head will be connected to the POST!

        GOOD LUCK!
        
    ''')
    sleep(3)


if __name__=="__main__":

    Flag = True

    newGame = Hangman()
    
    writeMain()

    newGame.printAll()
    #print(newGame.getCPUWord())

    while Flag:

        if not newGame.checkWinner() and newGame.getWrongGuess() < 8:
            
            userGuess = str(input('\nWhat is your guess? '))
            if len(userGuess) > 1 or len(userGuess) < 0: print("You can only guess one singular character at a time")
            else:
                sleep(1)

                newGame.checkGuess(userGuess)

                sleep(.5)

                newGame.printAll()
        
        else:

            if newGame.checkWinner():
                print(f'\nYOU HAVE COMPLETED THE HANGMAN GAME AND SUCCESSFULLY FOUND THE WORD: {newGame.getCPUWord()} with only {newGame.getWrongGuess()} wrong Guesses!')
                check = str(input('Would You like to play again:: Yes or No '))
                sleep(1)
                if check.lower() == 'no':
                    Flag = False
                else:
                    newGame = Hangman()
                    newGame.printAll()
                    #print(newGame.getCPUWord())
            else:

                print(f"\nDOO DOO DOOOOOOO.... YOU have run out of guesses...The word was {newGame.getCPUWord()}")
                check = str(input('Would You like to play again:: Yes or No '))
                sleep(1)
                if check.lower() == 'no':
                    Flag = False
                else:
                    newGame = Hangman()
                    newGame.printAll()
                    #print(newGame.getCPUWord())

    exit()