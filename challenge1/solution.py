import pandas as pd

"""
below is hastily put together example solution

"""

def highscore(filename,row):
    # this is a dictionary
    objtoreturn = {}

    # we want to keep track of how many scores we have collected
    count = 3

    # read the csv file using pandas library
    input = pd.read_csv(filename)

    # sort the dataframe by player and highscore
    input.sort_values(by=['PLAYER','HIGHSCORE'], ignore_index=True)

    input['row'] = input.groupby(['PLAYER']).cumcount()+1
    inter = input.loc[input['row'] == row]
    output = inter.values.tolist()
    output = sorted(output,key=lambda l:l[1], reverse=True)
    for index, _ in enumerate(output):
        objtoreturn[output[index][0]] = {output[index][1]}
        count -= 1
        if count == 0:
            break
    return objtoreturn