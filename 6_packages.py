"""
Packages are ubiquitous in python (and every other language), and they're essentially wrapped up bundles of code that you can import and use immediately.
In this example, i've imported pandas, sys and os.path.
They all have different methods that i can access to do lots of things that would generally be long-winded to code from scratch.
Packages generally (should!) have documentation that lets you know what you can do with them in detail.

They're INCREDIBLY useful, as without them you'd need to build everything yourself.
Imagine building a car. But then you'd need to build the wheels, 
forge the steel for the hubs, the screws, the bolts, refine your own petrol, make the rubber for the tyres
etc etc you get the point. Use libraries!!!!

The thing you _must learn_ to use with packages is their documentation.
The documentation for pandas for example is very detailed and easy to use.
I.E https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
[documentation in pandas on how to convert a Dataframe to a CSV file]


Below is an example of various packages being put to use together to fullfil a purpose that none of them probably could do alone.
"""

# This little script will grab any csv file and remove all whitespace within it.
# You can run it with arguments.
# Usage is python script inputfile outputfile.
# i.e python script.py input.csv output.csv

import pandas as pd #pandas - very powerful data manipulation library (called in the script as 'pd' - makes it easier to work with)
import sys #sys is a package that has various system interfaces i.e working with arguments in this case
import os.path #package that enables us to verify whether a file exists.

#Documentation for sys: https://docs.python.org/3/library/sys.html
#Some documentation for pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html
#Documentation for os.path: https://docs.python.org/3/library/os.path.html

#process - this function takes in two variables 'inn' and 'out'.
def process(inn, out):
    table = pd.read_csv(inn) #Read the csv file 'inn' and place it in a pandas dataframe i've labelled as 'table'.
    columns = table.columns.values #Grab the column names of the table and place them in a list. 
    for index, i in enumerate(columns): #Iterate through the column names list
        table[i] = table[i].str.replace(" ","") #For each column we want to iterate through the column and remove all whitespace.
    table.to_csv(out ,header=True, index=False) #Afterwards we want to save the dataframe as a csv file.

if __name__ == "__main__": #Standard 'entry point' method for python. 
    if len(sys.argv) <= 1: #If the length of the system arguments is less than or equal to one...
        exit("usage: python " + sys.argv[0] + " inputfilename outputfilename") #Exit with printing of instructions on how to use this script.
    else: 
        if os.path.isfile(sys.argv[1]): #If this file exists
            process(sys.argv[1], sys.argv[2]) #Invoke process function with arguments 1 and 2 (0 is the name of the script itself)
        else:
            print(sys.argv[1] + " does not exist.") #If file doesn't exist - tell them!
