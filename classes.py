"""
Classes are a template to create an object. An object is just a fancy term for a thing that can be defined clearly.
You build them from the ground up to do something.

For example, dogs and cats are animals.
You could, in a limited sense, define an animal. So you could create an animal object, so you could design a class to build animal objects.

For this example, I'm going to make a very simple animal class that creates an animal object that has a name, and a hunger i.e how hungry it is.
When you create the animal, you need to type in a name for it, and an integer for hunger.
Depending on the hunger, it takes so many times to feed the animal before they are happy.
Let's see how this works.
"""

class Animal: #This is the animal class
    #You can pre-define variables to be certain things when it's created
    hungry = True #The animal, by default, will be hungry when you create it.

    def __init__(self, name, hunger): #This is the standard way to 'instantiate' the class when you create it (provide it your own variables to pre-set it when it's created)
        self.hunger = hunger
        self.name = name

    #If you want the class to interact with the input of the function, include the 'self' variable. This is a hidden variable that will work within the function.
    def feed(self, food): #In this case, food is an integer. 
        self.hunger -= food #Deduct the food value from the hunger value
        if self.hunger < 0: #If hunger is below 0 
            self.hungry = False #Change the hungry variable to false.

    def check(self): #Functions within classes are called 'methods'. They're like bolt-on functions to a class which it has access to.
        if self.hungry:
            print(f'The {self.name} is still hungry!!!')
        else:
            print(f'The {self.name} is not hungry :)')
            
if __name__ == "__main__":
    #Here we create two animal objects using the Animal class.
    dog = Animal("dog", 50)
    cat = Animal("cat", 20)

    dog.check() #Both animals will, by default, be hungry.
    cat.check()

    dog.feed(5) #50 minus 5 is above 0... 
    dog.check() #The dog will still be hungry.

    
    cat.feed(30) #20 - 30 is negative.
    cat.check() #So the cat will not be hungry anymore.
"""
WHY BUILD CLASSES? WHAT'S THE POINT?
They let you solve problems. That's it really.
Much better answer is here: https://stackoverflow.com/questions/1993638/classes-whats-the-point
"""
