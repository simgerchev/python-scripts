'''
imports
'''
import random

'''
class representing the whole game
game is in test mode so all the generated ships are shown 
one day gotta take care of the erros you get if you dont write an int but for now the game is pretty much complete
'''
class Main: 
    '''
    _generatedField: list - the list that stores all the 'ships'
    _generatedFieldCopy: list - the list that acts as an 'overlay' so you cannot see where the ships are 
    '''
    _generatedField: list = []
    _generatedFieldCopy: list = []
    
    '''
    in case we need a constructor
    '''
    def __init__(self):
        pass

    '''
    generates an empty 'ocean'
    rowAmount: int - how many rows does the field have
    columnAmount: int - how many columns does the field have
    '''
    def generateField(self):
        self.rowAmount: int = int(input("Enter Amount of Rows: "))
        self.columnAmount: int = int(input("Enter Amount of Items on a Row: "))
        
        if isinstance(self.rowAmount, int) and isinstance(self.columnAmount, int):
            if(self.rowAmount and isinstance(self.rowAmount, int)):
                self._generatedField = [[None]] * self.rowAmount 
                self._generatedFieldCopy = [[None]] * self.rowAmount
            if(self.columnAmount and isinstance(self.columnAmount, int)): 
                    for i in range(0, self.rowAmount):  
                        self._generatedField[i] = ['~'] * self.columnAmount
                        self._generatedFieldCopy[i] = ['~'] * self.columnAmount
            print(*self._generatedField, sep = "\n")
        else: 
            print("Not an integer.")
            
        return self._generatedField, self._generatedFieldCopy
        
    '''
    generetes ships that are marked as '𓊝' in the 'ocean' 
    index: int - index that counts the iterations of the loop
    generatedRow: int - where the random row position of the ship is saved
    generatedColumn: int - where the random column position of the ship is saved
    directionChoice: list - list where the two possible directions are saved
    generatedShipDirection: str - a var where one of the directions is saved 
    shipAmount: int - input var where you baiscally can say how many ships you want but it's not so precise since somehow the ships can overlap
    maxSymbols: int - max length of a ship
    iterationIndex: int - counts the parts of a ship, is used to extend the ship so it has more than one part
    '''
    def generateShip(self):
        directionChoice: list = ['genRow', 'genColumn']
        shipAmount: int = int(input('Amount of Ships: '))
        generatedRow: int
        generatedColumn: int 
        shipLength: int 
        generatedShipDirection: str
        iterationIndex: int = 0      
        maxSymbols: int = 5
        index = 0 

        if shipAmount < self.rowAmount * self.columnAmount:
            while shipAmount > index:
                '''
                    (-5) so i make sure that the ships dont come out of the bondary for now
                    not a permanent solution i promis :D 
                '''
                generatedRow = random.randint(0, self.rowAmount - 5)
                generatedColumn = random.randint(0, self.columnAmount - 5)
                
                generatedShipDirection = random.choice(directionChoice)
            
                if generatedShipDirection == 'genRow':
                    iterationIndex = 0
                    shipLength = random.randint(0, maxSymbols)
                    while iterationIndex < shipLength: 
                        self._generatedField[generatedRow + iterationIndex][generatedColumn] = '𓊝'
                        iterationIndex += 1
                if generatedShipDirection == 'genColumn':
                    iterationIndex = 0
                    shipLength = random.randint(0, maxSymbols)
                    while iterationIndex < shipLength:
                        self._generatedField[generatedRow][generatedColumn + iterationIndex] = '𓊝' 
                        iterationIndex += 1

                index += 1
        else: 
            print('Too many ships.')
                
        return self._generatedField
    

    
    '''
    checks if there's a ship or not 
    shipsCounted: int - the amount of ships in the 'ocean' 
    success: int - the amount of found ships 
    '''
    def getVariableCont(self):
        shipsCounted: int = 0 
        success: int = -1
        
        '''
        code for counting the ships
        '''
        for indexRow in range(self.rowAmount):
            shipsCounted = shipsCounted + self._generatedField[indexRow].count('𓊝')
            
        while success < shipsCounted:
            print(*self._generatedField, sep = "\n")
            
            rowIndexValue:int = int(input("Input Row Number: ")) - 1
            columnIndexValue:int = int(input("Input Column Number: ")) - 1
            
            if rowIndexValue < self.rowAmount and columnIndexValue < self.columnAmount:
                if self._generatedField[rowIndexValue][columnIndexValue] == '𓊝':
                    if self._generatedFieldCopy[rowIndexValue][columnIndexValue] != '𓊝':
                        self._generatedFieldCopy[rowIndexValue][columnIndexValue] = '𓊝'
                        print(*self._generatedField, sep = "\n")
                        success += 1
                        print("That's right!")
                    else: 
                        print("That's wrong.")
                elif self._generatedField[rowIndexValue][columnIndexValue] == '~':
                    print("That's wrong.")
            else: 
                print("There are not so many rows/columns.")
    
    '''
    getter and setter functions used for debugging or testing purposes mostly
    '''
    def getField(self):
        return self._generatedField
    def getCopy(self): 
        return self._generatedFieldCopy
    def getIndex(self): 
        return self.listIndex

'''
func where the game can be started
'''
def play():
    main = Main()
    main.generateField()
    main.generateShip()
    main.getVariableCont()


play()

