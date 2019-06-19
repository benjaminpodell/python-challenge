#(successful) Method 1 Opening PyBank File

#file = 'C:/Users/btech/Desktop/python-challenge/PyBank/Resources/budget_data.csv'
#with open(file, 'r') as text:
    #print(text)
    #lines = text.read()
    #print(lines)  

import os
import csv

budgetdata = os.path.join('..', 'Resources', 'budget_data.csv')

with open(budgetdata, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
     print(csvreader)
     csv_header = next(csvreader)
     print(f"CSV Header: {csv_header}")
   
     for row in csvreader:
        print(row)

