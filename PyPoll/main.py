#Importing OS and File Type
import os
import csv

#Creates Path to election_data CSV File
#Had trouble opening 'budget_data.csv so implemented os.getcwd() to help open filepath
#https://www.tutorialspoint.com/python/os_getcwd.htm
print(os.getcwd())
election_data = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#Allows the File Path to be Read based on CSV Conditions
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Reads the Header of election_data CSV
    csv_header = next(csvreader)

    #Setting Total Votes Count to Zero In Order To Track Addition Towards Total 
    vote_counter = 0
    
    #Stores Candidate, Voter, and Percent data
    candidate_list = []
    vote_list = []
    percent_list = []

    #creates for loop reading each row in csv reader
    for row in csvreader:
        
        #Calculates the Total Vote Count
        vote_counter = vote_counter + 1

        #Conditional that checks if while iterating the candidate is not in Third Column, adds them to created Candidate Holder (candidate_list) then indexes them in Candidate Holder or else will continue to add/append their votes to vote_list
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            find_candidate = candidate_list.index(row[2])
            vote_list.append(1)
        else:
            find_candidate = candidate_list.index(row[2])
            vote_list[find_candidate] = vote_list[find_candidate] + 1

    #Creates for loop that calculates Vote Percentage
    for v in vote_list:
        #Format that floats Percentage Formula to 3 decimal places i.e. '3f' and adds to the Percent Holder (percent_list)
        #https://codereview.stackexchange.com/questions/69542/function-to-return-percentages-in-python
        percent = '{0:.3f}'.format((v / vote_counter * 100))
        percent_list.append(percent)

    #Finds Winning Candidate's highest Voting Count from the Created Vote Holder (vote_list) Value by indexing through (vote_list), returning the maximum value using 'max()' function, and storing it in variable called winner
    Win = max(vote_list)
    find_candidate = vote_list.index(Win)
    winner = candidate_list[find_candidate]

#Printing and Summarizing Data 
print("Election Results!")
print("----------------")
print(f'Total Votes: {str(vote_counter)}')
print("--------------------")

#Creates For loop that outputs candidates name, percent of votes, and number of votes from each of the created holders by going through the range of each lists length 
for x in range(len(candidate_list)):
    print(f'{candidate_list[x]}: {str(percent_list[x])}% ({str(vote_list[x])})')
print("-------------------------")
print(f'Winner: {winner}')
print("------------")

#Creates and exports an 'output' text file that is write only
export_txtfile = open("output.txt", "w")
l1 = str("Election Results!")
l2 = str("----------------")
l3 = str(f'Total Votes: {str(vote_counter)}')
l4 = str("--------------------")

#Syntax that outputs each line of text file for l1, l2, l3,l4
#https://stackoverflow.com/questions/21019942/write-multiple-lines-in-a-file-in-python/21020007
export_txtfile.write('{}\n{}\n{}\n{}\n'.format(l1, l2, l3, l4))

#Creates For loop that outputs candidates name, percent of votes, and number of votes from each of the created holders by going through the range of each lists length 
for y in range(len(candidate_list)):
    ln = str(f'{candidate_list[y]}: {str(percent_list[y])}% ({str(vote_list[y])})')
    
    #Syntax that outputs each line of text file for ln
    #https://stackoverflow.com/questions/21019942/write-multiple-lines-in-a-file-in-python/21020007
    export_txtfile.write('{}\n'.format(ln))

l5 = str("-------------------------")
l6 = str(f'Winner: {winner}')
l7 = str("------------")
#Syntax that outputs each line of text file for l5, l6, l7
#https://stackoverflow.com/questions/21019942/write-multiple-lines-in-a-file-in-python/21020007
export_txtfile.write('{}\n{}\n{}\n'.format(l5, l6, l7))