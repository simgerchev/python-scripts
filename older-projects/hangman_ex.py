# create a greeting
# create your word list 
# randomly choose a word
# ask the user to guess the word 
# bonus make the program take the input from the user and make it lowercase 
# check if the letter is in the word 

'''
some imports
'''
import random
from typing import List

'''
a class where I write all the function and logic for the "hangman" game
'''
class main:

    '''
    _greeting - a message presented at the beginning
    _wordList - the words that are going to be saved
    _randWord - the random word thats going to be taken from the wordlist
    _charList - the letters of the word are going to be splitted into single array keys
    '''
    _greeting: str
    _wordlist: List[str] = []
    _randWord: str
    _charList: List[str] = []
    _encryptedList: List[str] = []
    
    '''
    generating the wordlist with input
    '''
    def generateWordList(self):
        i: int
        wordListInput: List[str] = []
        
        i = 3 

        wordListInput = input(f"Give me {i} words: ")
        self._wordlist = wordListInput.split()
        
        while len(self._wordlist) < i or len(self._wordlist) > i:
            wordListInput = input(f"You didn't give me {i} words: ")
            self._wordlist = wordListInput.split()
        '''
        <<OUTPUT>> 
        if len(self._wordlist) == i:
            print(f"<<Success>>")
            for word in self._wordlist:
                print(word)
        '''
        return self._wordlist
    
    def generateACharList(self):
        self._charList = list(self._randWord)
        self._encryptedList = list(self._randWord)

        return self._charList, self._encryptedList
    
    def encryptACharList(self):
        for encryptedChar in range(len(self._encryptedList)):
            self._encryptedList[encryptedChar] = '_'
        return self._encryptedList
        
    def checkAChar(self):
        guess:str 
        index:int
        gameWon:bool = False
        i:int = 0
        while gameWon == False:
            guess = input("Which letter?")
            if guess in self._charList:
                index = self._charList.index(guess)
                self._encryptedList[index] = guess
                print(self._encryptedList)      
                i += 1
                if guess in self._encryptedList:
                    index = self._charList.index(guess)
                    self._charList[index] = " "
                if i == len(self._encryptedList):
                    gameWon = True
                    ("Nice Game :)")
            else:
                print("Try one more time ;)")
                
    def selectAWord(self):
        randNumber = random.randint(0, len(self._wordlist) - 1)
        self._randWord = self._wordlist[randNumber]
        return self._randWord
    
    '''
    here are going to be saved the getter and setter functions 
    '''
    def getAWord(self):
        print(self._randWord)

    def getCharList(self):
        print(self._charList)

    def getEncryptedList(self):
        print(self._encryptedList)


'''
here the class is going to be instantiated and calling the functions
'''
main = main()
main.generateWordList()
main.selectAWord()
main.getAWord()
main.generateACharList()
main.encryptACharList()
main.getEncryptedList()
main.checkAChar()