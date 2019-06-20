#Importing OS and File Type
import os
import csv

#Creates Path to budget_data CSV File
budget_data = 'C:/Users/btech/Desktop/python-challenge/PyBank/Resources/budget_data.csv'

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
    
    profit_list = []
    date_list = []
    
    month_count = month_count + 1
    profitloss_count = profitloss_count + int(row_one[1])
    holder_count = int(row_one[1])

    for row in csvreader:
        date_list.append(row[0])
        adjust_count = int(row[1]) - holder_count
        profit_list.append(adjust_count)
        holder_count = int(row[1])
        month_count = month_count + 1
        profitloss_count = profitloss_count + int(row[1])

    highest_increase = max(profit_list)
    highest_index  = profit_list.index(highest_increase)
    highest_date = date_list[highest_index]

    lowest_decrease = min(profit_list)
    lowest_index = profit_list.index(lowest_decrease)
    lowest_date = date_list[lowest_index]

    average = sum(profit_list) / len(profit_list)

    print("Financial Analysis")
    print("---------------------")
    print(f'Total Months: {str(month_count)}')
    print(f'Total: ${str(profitloss_count)}')
    print(f'Average Change: $ {str(round(average,2))}')
    print(f'Greatest Increase in Profits: {highest_date} (${str(highest_increase)})')
    print(f'Greatest Decrease in Profits: {lowest_date} (${str(lowest_decrease)})')

    output = open("output.txt", "w")

    l1 = "Financial Analysis"
    l2 = "---------------------"
    l3 = str(f'Total Months: {str(month_count)}')
    l4 = str(f'Total: ${str(profitloss_count)}')
    l5 = str(f'Average Change: $ {str(round(average,2))}')
    l6 = str(f'Greatest Increase in Profits: {highest_date} (${str(highest_increase)})')
    l7 = str(f'Greatest Decrease in Profits: {lowest_date} (${str(lowest_decrease)})')
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(l1,l2,l3,l4,l5,l6,l7))