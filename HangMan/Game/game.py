import random

class Hangman():

    with open('List.txt', 'r', encoding='utf-8') as f:
        _wordList = [line.strip() for line in f]
           
    def __init__(self):
        self._CPUGuess = random.choice(self._wordList)
        self._UserList = ['_'] * len(self._CPUGuess)
        self._UserGuessList = ''
        self._wrongGuesses = 0

    def getCPUWord(self):
        return self._CPUGuess
    
    def wrongGuess(self, var):
        print(f'The letter {var} is not in this word. Try Again')
        self._wrongGuesses += 1

    def checkGuess(self, var):

        if var in self._UserGuessList: 
            print('Word Already Guessed: Try Again!')
            return

        self._UserGuessList += var

        Flag = False

        for i in range(len(self._CPUGuess)):

            if self._CPUGuess[i] == var:
                self._UserList[i] = var
                Flag = True
                
            
        if not Flag: self.wrongGuess(var)
        else: print(f'The letter {var} is in this word! Great Job!')


    def checkWinner(self):
        if ''.join(self._UserList) == self._CPUGuess:
            return True
        
        return False

    def getUserList(self):
        return '    '.join(self._UserList)
    
    def getWrongGuess(self):
        return self._wrongGuesses
    
    def printAll(self):
        print('\nCurrent List: The word is {} characters...'.format(len(self._UserList)))
        print(f'\n{self.getUserList()}   Guess Count: {self.getWrongGuess()}   Current Characters Guessed: {self._UserGuessList}\n')