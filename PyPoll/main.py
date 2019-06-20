#Importing OS and File Type
import os
import csv

#Creates Path to election_data CSV File
election_data = 'C:/Users/btech/Desktop/python-challenge/PyPoll/Resources/election_data.csv'

#Allows the File Path to be Read based on CSV Conditions
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Reads the Header of election_data CSV
    csv_header = next(csvreader)

    #Setting Total Votes Count to Zero In Order To Track Addition Towards Total 
    vote_counter = 0
    
    candidate_list = []
    vote_list = []
    percent_list = []

    for row in csvreader:
        vote_counter = vote_counter + 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            find_candidate = candidate_list.index(row[2])
            vote_list.append(1)
        else:
            find_candidate = candidate_list.index(row[2])
            vote_list[find_candidate] = vote_list[find_candidate] + 1

    for v in vote_list:
        percent = (v/vote_counter) * 100
        percent = round(percent)
        percent = "%.3f%%" % percent
        percent_list.append(percent)

    Win = max(vote_list)
    find_candidate = vote_list.index(Win)
    winner = candidate_list[find_candidate]

print("Election Results!")
print("----------------")
print(f'Total Votes: {str(vote_counter)}')
print("--------------------")
for x in range(len(candidate_list)):
    print(f'{candidate_list[x]}: {str(percent_list[x])} ({str(vote_list[x])})')
print("-------------------------")
print(f'Winner: {winner}')
print("------------")

output = open("output.txt", "w")
l1 = str("Election Results!")
l2 = str("----------------")
l3 = str(f'Total Votes: {str(vote_counter)}')
l4 = str("--------------------")
#Outputs file and creates new line, I referenced 
#https://stackoverflow.com/questions/28462164/python-writing-to-a-new-line
output.write('{}\n{}\n{}\n{}\n'.format(l1, l2, l3, l4))
for y in range(len(candidate_list)):
    ln = str(f'{candidate_list[y]}: {str(percent_list[y])} ({str(vote_list[y])})')
    output.write('{}\n'.format(ln))
l5 = str("-------------------------")
l6 = str(f'Winner: {winner}')
l7 = str("------------")
#Outputs file and creates new line, I referenced 
#https://stackoverflow.com/questions/28462164/python-writing-to-a-new-line
output.write('{}\n{}\n{}\n'.format(l5, l6, l7))