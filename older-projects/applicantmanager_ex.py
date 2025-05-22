'''
SD2 Task1 
Application where you can save and sort all the applicants
'''

"""
Imports
"""
import random
import itertools

'''
A class used to represent the Applicants
'''
class Applicant:
    #object for the auto incrementing of the id we have in the class
    idObj:object = itertools.count()

    _id:int = None
    _firstName:str = None
    _secondName:str = None
    _gender:str = None
    _city:str = None
    _age:int = None
    _address:str = None
    _birthday:list = None
    _certificate:bool = None
    _expectedSalary:float = None

    def __init__(self):
        self._id = next(Applicant.idObj)
        self._firstName = input("First Name:")
        self._secondName = input("Second Name:")
        self._gender = input("Gender:")
        self._city = input("City:")
        self._age = int(input("Age:")) 
        self._address = input("Address:")
        self._birthday = [int(input("Day")), int(input("Month")), int(input("Year"))]
        self._certificate = bool(input("Certificate:"))
    
    """
    Getter and setter methods section
    """
    def getId(self):
        return self._id
    def getFirstName(self):
        return self._firstName
    def getSecondName(self):
        return self._secondName
    def getGender(self):
        return self._gender
    def getCity(self):
        return self._city
    def getAge(self):
        return self._age
    def getAddress(self):
        return self._address
    def getBirthday(self):
        return self._birthday
    def getCertificate(self):
        return self._certificate
    #--
    def setFirstName(self, firstName: str):
        self._firstName = firstName
    def setSecondName(self, secondName: str):
        self._secondName = secondName
    def setGender(self, gender):
        self._gender = gender
    def setCity(self, city):
        self._city = city 
    def setAge(self, age: int):
        self._age = age
    def setAddress(self, address: str):
        self._address = address
    def setBirthday(self, birthday: list):
        self._birthday = birthday 
    def setCertificate(self, certificate: bool):
        self._certificate = certificate

'''
A class used to represent the Database the Applicants will be saved in
'''
class Database:
    _applicantList: list[Applicant] = None

    def __init__(self, applicantList: list[Applicant] = None):
        if applicantList is None:
            applicantList = []
        self._applicantList = applicantList

    def findApplicant(self, applicantId: int):
        for applicant in self._applicantList:
            if int(applicantId) == int(applicant.getId()):
                print(str(F"/First Name: applicant.getFirstName()) /Second Name:str(applicant.getSecondName()) /Gender:str(applicant.getGender()) /City:str(applicant.getCity()) /Age:str(applicant.getAge()) /Address:str(applicant.getAddress()) /Birthday:str(applicant.getBirthday()) /Certificate:str(applicant.getCertificate())")
            else: 
                print(str(applicantId) + ' ' + str(applicant.getId()))
                 
    def deleteApplicant(self, applicantId: int):
        for applicant in self._applicantList:
            if applicant.getId() == applicantId:
                pass       
    def changeApplicantData():
        pass
    def printApplicants(self):
        #applicantIndex: int = 0
        for applicant in self._applicantList:
            #applicantIndex += 1
            #applicant._id = applicantIndex
            print(F"/ID: {str(applicant.getId())} /First Name: {applicant.getFirstName()} /Second Name: {applicant.getSecondName()}")
            
    '''
    Getter and setter methods section
    '''
    #--


def play():  
    database = Database()
    applicantList = database._applicantList
    #applicantDummy1 = Applicant("Tom", "Tomson", "Male", "Tomcity", 22, "Tomsonstr.", [12, 12, 2000], True)
    #applicantDummy2 = Applicant("Maria", "Marinson", "Female", "Mariacity", 24, "Mariestr.", [12, 12, 2000], False)
    applicant = None

    while applicant == None:
        def mainMenu():
            opt = int(input("What do you want: 1. Add Applicant 2. Print all Applicants 3. Delete Applicant 4. Get more Information about a Particular Applicant"))
            return opt

        opt = mainMenu()
        #add applicant
        if opt == 1:
            applicant = Applicant()
            applicantList.append(applicant)
            print(applicant.getFirstName())
            applicant = None

        #print all applicants
        if opt == 2:
            database.printApplicants()
        
        #delete applicant
        if opt == 3:
            database.printApplicants()
            print("Which applicant do you want to delete?")
        
        if opt == 4: 
            database.printApplicants()
            database.findApplicant(input("What's the id?"))


    
play()   
