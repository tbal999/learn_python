"""
Functions are the bread and butter (imo) of coding. They allow you to package a process into one easy to read part.
Whenever you are coding and you notice yourelf repeating a piece of code... that code can become a function.
It's good practise to analyse your code whilst you are developing, always trying to break things up into functions as you go.

There are first order functions & higher order functions. We're just going to discuss first order here.

Functions can include input(s) and output(s). They can have neither. They can also have one or the other.

Basically there can be 4 types functions, they are:

Function with no arguments and no return value.
Function with no arguments and a return value.
Function with arguments and no return value.
Function with arguments and a return value.

Demonstrations:
"""

def bark1(): #No input, just prints something
    print("The hound barked!")

def bark2(dog): #Takes in input 'dog' which is a string.
    print(f'The {dog} barked!')

def bark3(): #No input, and returns a string.
    return "The hound barked!"

#Below are examples of multiple inputs and outputs

def addTogether(a, b):
    return a+b

def add5toboth(a, b):
    return a+5, b+5


"""
Below is a recursive function that calculates the fibonacci sequence. 
We'll get into recursion later but just want to show you the power of functions.
This sequence requires four inputs
The first two numbers in the sequence are 0 and 1. (the first and second number)
It also takes in two more inputs, max and epoch.

prev = the first number
now = the second number
max = the maximum number of items that will be printed on one line.
epoch = the maximum number of times we will start on a new line.
"""
def fibonacci(prev, now, max, epoch):
    max -= 1                     #First deduct from the max counter
    if max <= 0:                 #If max is less than or equal to zero
        print(f'{now+prev},', end='\n') #Print the two numbers added together
        max = 10                        #reset max to 10 so it iterates through it again.
        epoch -= 1                      #decrease epoch by 1.
    else:                        #If max is greater than 10 i.e still going through the numbers
        print(f'{now+prev},', end='') #print out the numbers on the same line
    if epoch <= 0:                     #If epoch is equal/less than 0 we want to quit from this recursion
        return
    fibonacci(now, now+prev, max, epoch)    #Otherwise call the function again with new numbers.

def main():
    bark1()

    bark2("hound")

    print(bark3())

    print(addTogether(5,5))

    print(add5toboth(2,3)) #This will result in a tuple which is a type of data structure

    fibonacci(0, 1, 10, 7) #Calls the fibonacci function starting with the numbers 0 and 1, and will print 7 lines of 10 numbers each line.

if __name__ == "__main__": #By the way this is the standard method toward creating your 'entry point' for your program. 
    main()
    # LEARN MORE ABOUT THIS HERE - https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
