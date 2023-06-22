# PyPoll: Vote Counter for Election - Python script

Script that counts votes for each electoral candidate and determines winner.

## Table of Contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Screenshot](#screenshot)
- [Code example](#code-example)
- [References](#references)

## General info

- Reads data in from .csv file.
- Tallies the total votes cast.
- Determines how many candidates recieved votes.
- Records how many votes each candidate received, shows total votes and percentage of votes (Function).
- Outputs the result to command line and text file.
- Created and submitted for an assignment for Monash University Data Analytics Boot Camp (June 2023).

## Technologies

Project created and run using:

- Python 3.10.9
- Visual Studio Code 1.79.2

## Setup 

Use Python Script on .csv files containing data arranged in three columns:

- 'ballot ID', 'seat', 'candidate'.

## Screenshot

Output

![Screenshot - Output](/Users/samuelpalframan/Documents/Text Documents/University/Monash/Data Analytics Boot Camp/Modules/Module_3_Python/Module_3_Challenge/Starter_Code-3/PyPoll/Submitted/Screenshot - Output.png)

## Code example

```python
#PyPoll - Vote Counting Script

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
```

## References

- Determine maximum value in Dictionary:
  - https://www.entechin.com/how-to-find-the-max-value-in-a-dictionary-in-python/#:~:text=The%20simplest%20way%20to%20get,max%20value%20of%20any%20iterable

- Creating Dictionary Keys from List:
  - https://www.geeksforgeeks.org/python-initialize-a-dictionary-with-only-keys-from-a-list/

- Creating List from Dictionary Keys:
  - https://www.tutorialspoint.com/How-to-print-all-the-keys-of-a-dictionary-in-Python#:~:text=Python%27s%20dict.,keys()%20method

- Code, in general, was adapted from Monash University Data Analytics Boot Camp 2023 course learning material.



Created and written by Samuel Palframan - June 2023.









