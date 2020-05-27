import os
import csv

csvpath = os.path.join('Pybank.csv')

with open (csvpath, 'r') as file_handler:
    lines = file_handler
    print (lines)
    print(type(lines)
    
with open (csvpath)as csvfile:
    csvreader = csv.reader (csvfile, delimiter = ',')

    for row in csvreader:
        print(row)
        