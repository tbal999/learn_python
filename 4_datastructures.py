"""
Data structures let you do a lot, quickly.
There are many types in python but for now we'll go through two main data structures which are used a LOT.

1) Lists (in other langauges these can be called arrays)

and

2) Dictionaries (in other langauges these can be called maps)

There's a whole list of data structures here - https://realpython.com/python-data-structures/#list-mutable-dynamic-arrays

"""
#These are GLOBAL variables.
alist = [] #This is how you instantiate a 1 dimensional list. You can 1 dimension, 2 dimensions, 3.... etc 
adictionary = {} #This is a dictionary. We'll get to it soon.

if __name__ == "__main__":
    alist.append(1) #The append method lets you attach a new variable or item to the list. Here we are appending the number 1.
    alist.append("one") #You can append different types to the same list. This is a very pythonic thing you can do!
    alist.append(1.618) #Here's the golden ratio.
    print(alist) #This will print out the entire list. [1, 'one', 1.618]

    alist.pop(-1) #This will remove the last item off a list. (index -1 in python literally means the last item)
    print(alist) #This will print out [1, 'one']

    alist.pop(0) #This will remove the first item from a list. (index 0 in a list is the first item) and also return it to you.
    #if you want to delete an item but don't need it - just do: del alist[0]
    print(alist) #This will print out ['one']

    #You can adjust data in a list.
    #Below we are accessing index 0 (the first item) in the list and adding to the string.
    alist[0] += " and a two and a three"
    print(alist)  #This will print out ['one and a two and a three']
    #You can google more methods that lists can use
    # Or try this site: https://docs.python.org/3/tutorial/datastructures.html
    # You learned in the previous section that methods are bolt-on functions for a class.
    # So that means that a list is an object, created by a list class. And the list object has the methods 'pop' and 'append' in it, alongside many others.


    """
    Now we will look at the dictionary.
    """
    #With dictionaries you don't really need to keep track the length of it. You can just place anything you want at any index.
    adictionary[0] = "I've added something to this index!"

    print(adictionary[0])

    adictionary[21] = "And i've added something here too..."

    print(adictionary[21])

    #But if you tried print(adictionary[4]) you would get an error. This is because there's nothing held at index 4, so you'd be trying to print a null (not "" or 0 - literally a null pointer).

    #You can also adjust data in a dictionary.
    adictionary[21] += " here's something more!"

    print(adictionary[21])

    del adictionary[0] #You can also delete items in a dictionary - but don't try to print them after you've deleted them!


"""
Lists are used normally to manipulate data and work with it quickly. You can interate through lists quickly to process many hundreds of thousands of rows of data.
Dictionaries are used to store and retrieve data quickly. You can insert data at any index. 
if you use a dictionary with a hash function, you get a hash table. We'll go into them more later.
"""
