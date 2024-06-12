#abstract class = a class which contains one or more abstract methods
#                 Prevents a user from creating an object of that class
#                 compels a user to override abstract methods in a child class

from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    
    @abstractclassmethod 
    def go(self):
        pass

    @abstractclassmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car!")

    def stop(self):
        print('This car is stoped!')

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle!")

    def stop(self):
        print('This motorcycle is stoped!')

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()