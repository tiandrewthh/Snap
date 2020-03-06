#Title: DataFrame for Equities
#By: Andrew Tran
#github repo: https://github.com/tiandrewthh/Snap
#Description:   This python scripts renames table columns and merges them into one table
#               Use the github repo to download directories and files and run python script 
#               using 'python Equities_Python_DataFrame.py'
#               Make sure Anaconda and panda has been configured in your environment

import os
import pandas as pd
from functools import reduce 

#Declaring arrays and int variables
files = []
equity_name = []
index = 0

#Scans the directory for files
with os.scandir('Equities/') as entries:
    for entry in entries:
        files.insert(index, 'Equities/' + entry.name)
        equity_name.insert(index, os.path.splitext(entry.name))
        index += 1

equity = []
index = 0
#Inserts csv table data into arrays, renames the columns and appends columns using outer join
while index < len(files):
    equity.insert(index, pd.read_csv(files[index]))
    equity[index] = pd.DataFrame(equity[index], columns= ['Date', 'Close'])
    equity[index].rename(columns = {'Close': equity_name[index]}, inplace=True)
    index += 1
    
total_equities = pd.concat(equity, axis=0, sort=False, join='outer')
#Use print function to test
#print(total_equities)


