'''
imports
some of them are not used
'''
import sys,time,random

'''
main class where everything is written
_saveUserInput: int - a variable where the user input is saved
_generatedPcInput: int - a variable where the pc 'input is saved'
_startSymbols: list - a variable where all the ascii symbols are saved
'''
class Main: 
    _savedUserInput: int
    _generatedPcInput: int 
    _startSymbols: list = [''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', 
'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

    '''
    function for getting the actual user input
    '''
    def genUserInput(self): 
        self._savedUserInput = int(input('__' + '(1): ' + self._startSymbols[0] + '__' +  '(2): ' +  self._startSymbols[1] + '__' +  '(3): ' +  self._startSymbols[2] + 'Which one do you choose? '))
        print(self._startSymbols[self._savedUserInput - 1])
        return self._savedUserInput

    '''
    function for generating the actual pc input
    '''
    def genPcInput(self): 
        self._generatedPcInput = random.randint(1, 3)
        print(self._startSymbols[self._generatedPcInput - 1])
        return self._generatedPcInput

    '''
    function which compares both pc and user 'inputs' and defines who the winner is
    '''
    def compareInputs(self):
        if self._savedUserInput == 1 and self._generatedPcInput == 3 or self._savedUserInput == 2 and self._generatedPcInput == 1 or self._savedUserInput == 3 and self._generatedPcInput == 2:
            print("User Won")
        elif self._generatedPcInput == 1 and self._savedUserInput == 3 or self._generatedPcInput == 2 and self._savedUserInput == 1 or self._generatedPcInput == 3 and self._savedUserInput == 2:
            print("Pc Won")
        else:
            print("Draw")
    '''
    some getter and setter methods for testing purposes
    '''
    def getUserInput(self):
        return self._savedUserInput
    
    def getPcInput(self):
        return self._generatedPcInput
    
'''
a script where everything is 'played'
'''
def play():
    main = Main()
    main.genUserInput()
    main.genPcInput()
    main.compareInputs()

play()
