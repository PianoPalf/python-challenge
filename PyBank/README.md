# PyBank: Budget Data Calculations using CSV files - Python script

Script that calculates total change in profit/loss data and determines months of greatest increase and decrease.

## Table of Contents

- [General info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)
- [Screenshot](#screenshot)
- [Code example](#code-example)
- [References](#references)

## General info

- Reads data in from .csv file.
- Calculates total profit/loss in given data.
- Calculates average change between months.
- Determines months and values of greatest increase and decrease.
- Outputs result to command line and text file.
- Created and submitted for an assignment for Monash University Data Analytics Boot Camp (June 2023).

## Technologies

Project created and run using:

- Python 3.10.9
- Visual Studio Code 1.79.2

## Setup 

Use Python Script on .csv files containing data arranged in three columns:

- 'date', 'profit/loss'.

## Screenshot

Output

![Output Screenshot](https://github.com/PianoPalf/python-challenge/assets/119825935/dec4985c-6de4-4bfb-85a4-16b56d2f8d13)

## Code example

```python
#Read in data from file
with open(budget_csv) as csfile:
    csvreader = csv.reader(csfile, delimiter=',')

    #Store Column titles but skip them for data analysis
    header_row = next(csvreader)

    #Read through every row of data
    for row in csvreader:

    #Place each month in List for calculating number of months
        month = row[0]
        months.append(month)
        
    #Calculate the total Profit/Loss over all months
        total = int(row[1])
        totals.append(total)

#Calculate average change between months
for i in range(len(totals)-1):
    differences = totals[i + 1] - totals[i]
    totals_differences.append(differences)

#Assign variables for greatest increase and decrease in Profit    
greatest_increase = max(totals_differences)
greatest_decrease = min(totals_differences)

#Determine months of greatest increase and decrease in Profit
for x in range(len(totals_differences)-1):
    temporary_profit_loss = totals_differences[x]
    #temporary_decrease = temporary
    if greatest_increase == temporary_profit_loss:
        increase_month = x
    elif greatest_decrease == temporary_profit_loss:
        decrease_month = x
```

## References

- Code, in general, was adapted from Monash University Data Analytics Boot Camp 2023 course learning material.



Created and written by Samuel Palframan - June 2023.









