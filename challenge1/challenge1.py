"""
Challenge 1

1) Try importing the 'challenge1.csv' file into python (using pandas, or some other method)

2) Grab the highest score for every single player.

3) From that list of high scores, list the 1st, 2nd and 3rd highest scoring player.

Bonus:

4) Turn it into a function where you can pick which row you want to grab for each player i.e the highest score, the second highest, the third highest.
   
"""

import pandas as pd

def highscore(file,row):
    input = pd.read_csv(file)
    input.sort_values(by=['PLAYER','HIGHSCORE'], ignore_index=True)
    input['row'] = input.groupby(['PLAYER']).cumcount()+1
    inter = input.loc[input['row'] == row]
    output = inter.values.tolist()
    output = sorted(output,key=lambda l:l[1], reverse=True)
    for index, _ in enumerate(output):
        print(f'{output[index][0]}, Score: {output[index][1]}')


if __name__ == "__main__":
    #Begin!
    highscore("challenge1.csv", 1)
