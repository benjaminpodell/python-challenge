#Importing OS and File Type
import os
import csv

#Creates Path to budget_data CSV File
#Had trouble opening 'budget_data.csv so implemented os.getcwd() to help open filepath
#https://www.tutorialspoint.com/python/os_getcwd.htm

print(os.getcwd())
budget_data = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#Allows the File Path to be Read based on CSV Conditions
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Reads the Header of budget_data CSV
    csv_header = next(csvreader)
    
    #Reads the First Row of budget_data CSV
    row_one = next(csvreader)

    #Setting Month Total, Profit Loss Total, Holder Count, and Adjust Count to Zero In Order To Track Addition Towards Total For Each
    month_count = 0
    profitloss_count = 0
    holder_count = 0
    adjust_count = 0
    
    #Stores profit and date data 
    profit_list = []
    date_list = []
    
    #Totals the months, profitloss count, and adds to the holder count for the very first row before going through the other rows
    month_count = month_count + 1
    profitloss_count = profitloss_count + int(row_one[1])
    holder_count = int(row_one[1])

    #creates for loop reading each row in csv reader
    for row in csvreader:
        
        #Goes through the dates holder and tracks changes
        date_list.append(row[0])
        
        #Adjusts the profits holder by iterating through each row and then moving to next holder_count which assists with pushing through the rows
        adjust_count = int(row[1]) - holder_count
        profit_list.append(adjust_count)
        holder_count = int(row[1])
        
        #Calculates the total months exluding header and first row
        month_count = month_count + 1
        
        #Calculates them total profit loss count excluding header and first row
        profitloss_count = profitloss_count + int(row[1])

    #Finds the Greatest Profit Increase's Value and Date by indexing through profit list and returning the maximum value and date using 'max()' function
    highest_increase = max(profit_list)
    highest_index  = profit_list.index(highest_increase)
    highest_date = date_list[highest_index]

    #Finds the Greatest Profit Decreases's Value and Date by indexing through profit list and returning the minimum value and date using 'min()' function
    lowest_decrease = min(profit_list)
    lowest_index = profit_list.index(lowest_decrease)
    lowest_date = date_list[lowest_index]

    #Formula that Calulates the Average Change in Profit by dividing the sum of all profits in created profit holder by the entire length of profit holder 
    average = sum(profit_list) / len(profit_list)

    #Printing and Summarizing Data 
    print("Financial Analysis")
    print("------------------")
    print(f'Total Months: {str(month_count)}')
    print(f'Total: ${str(profitloss_count)}')
    
    #Round function that rounds the average change to 2 decimal places
    print(f'Average Change: $ {str(round(average,2))}')
    print(f'Greatest Increase in Profits: {highest_date} (${str(highest_increase)})')
    print(f'Greatest Decrease in Profits: {lowest_date} (${str(lowest_decrease)})')

    #Creates and exports an 'output' text file that is write only
    export_txtfile = open("output.txt", "w")

    #Creates the output text files lines 'l1, l2, ect...' based on Printing and Summarizing Data
    l1 = "Financial Analysis"
    l2 = "------------------"
    l3 = str(f'Total Months: {str(month_count)}')
    l4 = str(f'Total: ${str(profitloss_count)}')
    
    #Round function that rounds the average change to 2 decimal places
    l5 = str(f'Average Change: $ {str(round(average,2))}')
    l6 = str(f'Greatest Increase in Profits: {highest_date} (${str(highest_increase)})')
    l7 = str(f'Greatest Decrease in Profits: {lowest_date} (${str(lowest_decrease)})')
    
    #Syntax that outputs each line of text file for all 7 lines
    #https://stackoverflow.com/questions/21019942/write-multiple-lines-in-a-file-in-python/21020007
    export_txtfile.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(l1,l2,l3,l4,l5,l6,l7))