#Inheritance = derive what parent's code to child codes
class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")
    
    def sleep(self):
        print("This animal is sleep")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running!")

class Fish(Animal):
    def swim(self):
        print("This fish is swimming!")

class Hawk(Animal):
    def fly(self):
        print("This hawk is flying!")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive)
#fish.sleep()
#hawk.eat()

rabbit.run()
fish.swim()
hawk.fly()



#Override
class Organism:
    alive = True

class Human(Organism):
    def eat(self):
        print("This man is eating!")

class Japanese(Human):
    #override eat() from Human()
    def eat(self):
        print("This Japanese is eating ramen")

japanese = Japanese()

japanese.eat()


