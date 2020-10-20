"""
loops are powerful. They let you iterate through lots of things quickly, and are a key aspect of a lot of programming and automation.
We are going to go through two loops in python - 'for' and 'while', as well as briefly talk about recursion.

Read the stuff in the main entry point first, or not?
"""

#Recursive functions are functions that call themselves, usually in a controlled manner, to complete tasks where iteration is necessary.
def recursion(thelist, index):
    print(thelist[index]) #Here we are printing the item at list[index]
    index += 1 #Then we add 1 to index
    if index < len(thelist): #If index is within the boundaries of the list...
        recursion(thelist, index) #Call the function again, with updated index.

if __name__ == "__main__":
    x = 0
    while x < 10: #This is a while loop. It will loop as long as x is less than 10.
        print(x) #Print x
        x += 1 #add 1 to x (this will break the loop when x hits 9)

    #Now we'll use a for loop to iterate through a list.

    alist = [1,2,3,4,5,6,7,8,9,10] #Here's a list of numbers 1 to 10.

    for item in alist: #This for loop lets us iterate through the list and do something at every index.
        print(item*2) #We're multiplying each item by 2 and printing it

    #You can also iterate through a list whilst keeping track of the index:
    for index, i in enumerate(alist):
        print(index, i) #You could also do print(alist[index]) and it would print out each item.

    #There is another way you can loop through something, and that is through recursion.
    recursion(alist, 0) #This function takes in the list, as well as a starting point.

    #You'll learn over time when it's best to use a for loop, a while loop and recursion.
