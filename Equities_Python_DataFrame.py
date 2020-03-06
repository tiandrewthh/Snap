import os
import pandas as pd
from functools import reduce 

#Declaring arrays and int variables
files = []
array = [1,2,3,4,5]
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
#Inserts csv table data into arrays, renames the columns and concatenates columns using outer join
while index < len(files):
    equity.insert(index, pd.read_csv(files[index]))
    equity[index] = pd.DataFrame(equity[index], columns= ['Date', 'Close'])
    equity[index].rename(columns = {'Close': equity_name[index]}, inplace=True)
    total_equities = pd.concat(equity, axis=1, sort=False, join='outer')
    #print (total_equities)
    index += 1


