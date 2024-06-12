#Python Object Oriented Program
class Car:

    wheels = 4 #class variable(default variable = mutable)        
    #attributes = what an object is or has
    def __init__(self, make, model, year, color):
        self.make = make    #instance variable
        self.model = model  #instance variable
        self.year = year    #instance variable
        self.color = color  #instance variable

    #method
    def drive(self):
        print("This "+self.model+" is driving!")
    
    def stop(self):
        print("This "+self.model+" is stopped")




