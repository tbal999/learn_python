"""
Variables are values that can change which you can assign and control.
They are very useful and a key aspect of programming - let's learn them.
Here are four:
"""

dog = "woof" #This is a variable called 'dog'. The data stored within this variable is a string, and the string is 'woof'.
cat = "meow" #This is a variable called 'cat'. The data stored within this variable is also a string, and the string is 'meow'.
one = 1 #This is a variable called one, it stores an integer of '1'.
pi = 3.141 #This is a variable called pi, it stores a float value of of '3.141'.

#Ignore this bit for now - continue below to the main entry point \/
def addone():    
    #this is a local variable                 
    dog = "woof"                           
    dog += " another woof!"               
    print(dog)   #This will just print 'woof another woof!'

    #and this is a global variable
    global cat #you declare a variable as global like this
    cat += " and this is the same cat!"
    print(cat)   #This will print 'meow i am a cat... and this is the same cat!'   
    #This is because we have already declared the cat variable on row 8, then we added 'i am a cat...' on row 58 in the entry point, and THEN called this function from row 78.

if __name__ == "__main__":
    """
    In python, you don't need to store the type of variable. It will automatically infer what type the variable is.
    Sometimes you may need to convert a variable to get the intended result you are looking for.
    INDENTATON is very important in python as well.
    Notice how all the text / code after the colon (on row 25) is indented by one tab. 
    If it wasn't, it wouldn't work!
    Here's more info about python indentation - https://www.w3schools.com/python/gloss_python_indentation.asp
    w3schools generally has a loooot of useful info on python, so a very good place to learn.
    """

    #Here we have two variables, two and inttwo. 
    #two is a string and inttwo is an integer.
    two = "2"
    inttwo = 2


    print(two*inttwo) #Here we are printing the string '2' twice - in python this will result in 22, which is basically two '2' strings.
    print(int(two)*inttwo) #Here we are converting the string '2' into an integer, and then multiplying it by 2. This will result in 4, which is what you'd expect multiplying two integers.

    """
    Whilst python makes variable handling easy, it is good to recognise what types you are working with to ensure you don't make mistakes.
    For example, a calculator that works by manipulating strings clearly wouldn't be good. After all, 2 plus 2 is not 22.
    """

    #Below we are printing all the variables from earlier.
    print(dog)
    print(cat)
    print(one)
    print(pi)

    #You can edit variables for example:
    dog += " woof!" #This could also be written as 'dog = dog + " woof!"
    cat += " i am a cat..."
    one *= 5 #This could also be written as one = one*5
    pi = pi*2

    #If we print them out again they will be different.
    print(dog) #woof woof
    print(cat) #meow i am a cat...
    print(one) #5
    print(pi) #6.282

    """
    Global and local variables - what are they?

    Variables within functions are local. Variables outside functions (like the ones we have looked at so far) are global. 
    Local functions are only within the scope of that function.
    Global functions are accessible anywhere - this can be a bad thing if you have a large program. KEEP TRACK OF YOUR GLOBAL VARIABLES!

    Demonstration...
    """

    addone() #Here we are calling the function earlier (on row 12), go back and read what i wrote in it.
    #In this function there is a local 'dog' variable but also the global 'cat' variable.
