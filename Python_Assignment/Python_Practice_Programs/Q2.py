# #### Define a class Person and its two child classes: Male and Female.
# All classes have a method "get_gender" which can print "Male" for Male class and "Female" for Female Class.
# <br>Bonus: Make class Person an abstract class and make get_gender an abstract method in the same class. The two child classes must inherit and implement get_gender. i.e., When trying to initialize an object of class Person, the program must throw an error. Hint: Use ABC library (comes natively with Python3)

#Importing Libraries
from abc import ABC, abstractmethod

#defining the parent class using abstract method
class Person(ABC):
    
    @abstractmethod
    def get_gender(self):
        pass
    
#defining child classes
class Female(Person):
 
    # overriding abstract method
    def get_gender(self):
        print("Female")

class Male(Person):
 
    # overriding abstract method
    def get_gender(self):
        print("Male")
        
class ThirdGender(Person):
 
    # overriding abstract method
    def get_gender(self):
        print("Third Gender")
        
# Driver code
F = Female()
F.get_gender()
 
M = Male()
M.get_gender()

T = ThirdGender()
T.get_gender()
