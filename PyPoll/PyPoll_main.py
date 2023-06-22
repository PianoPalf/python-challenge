#PyPoll - Vote Counting Script

#Import relevant dependencies
import os
import csv

#Create path for CSV file to read
election_csv = os.path.join("Resources", "election_data.csv")

#Create empty Dictionary for election results to append in Vote Counter Function
result = {}

#Makes Total Candidate Votes List and Column Header List (for future reference)
candidate_list = []
header_row = []

#Vote Counter Function: input Candidate name and Candidate List as Parameters
def vote_counter(candidate, candidate_list):
    #counts number of votes for candidate
    no_votes = 0
    for i in candidate_list:
        temp_candidate = i
        if candidate == temp_candidate:
            no_votes = no_votes + 1
    #calculates vote percentage
    vote_percentage = round((no_votes / total_votes) * 100, 3)
    #appends election result Dictionary
    result[candidate] = vote_percentage, no_votes
    return result

#Read in data from file
with open(election_csv) as csfile:
    csvreader = csv.reader(csfile, delimiter=',')

    #Records Column Headers in List and Skips first row for data analysis
    header_row = next(csvreader)

    #Read through every row of data
    for row in csvreader:

        #Make List containing all candidates
        candidate = row[2]
        candidate_list.append(candidate)
    
#Determine unique candidates by making List into Dictionary Keys (removes duplicates) 
candidates_Dict = dict.fromkeys(candidate_list, None) #using: dict.fromkeys() method
    
#Convert Dictionary Keys back to List for easy access
candidates = list(candidates_Dict.keys())
 
#Determine total number of votes
total_votes = len(candidate_list)

#Calling Vote Counter Function for each candidate
for x in range(len(candidates)):
    vote_counter(candidates[x], candidate_list)
        
#Determines winner of election using max() and get() Functions
winner = max(result, key=result.get)    

#Variable assigned to output results
output = f"""
Election Results
=========================\n
Total Votes: {total_votes}
-------------------------\n
Votes Received For:
\n
{candidates[0]}: {result[candidates[0]][0]}% ({result[candidates[0]][1]})\n
{candidates[1]}: {result[candidates[1]][0]}% ({result[candidates[1]][1]})\n
{candidates[2]}: {result[candidates[2]][0]}% ({result[candidates[2]][1]})\n
-------------------------\n
Winner: {winner}\n
-------------------------
"""

#Prints election results to Terminal
print(output)

#Creates path for output text file
data_output = os.path.join("Resources", "election_results.txt")

#Writes election results to text file
with open(data_output, "w") as file:
    file.write(output)