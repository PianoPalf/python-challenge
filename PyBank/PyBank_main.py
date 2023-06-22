#PyBank - Budget Data Calculations using CSV files

#Import relevant dependencies
import os
import csv

#Create path for CSV file to read
budget_csv = os.path.join("Resources", "budget_data.csv")

#Make Title of Columns a List for future reference
header_row = []

#Create empty lists for calculations
months = []
totals = []
totals_differences = []

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
    
#Sum of Profit/Loss changes between months
total_change = sum(totals_differences)

#Average Profit/Loss change between months 
profit_loss_change = total_change / (len(totals)-1)

output = f"""
Financial Analysis\n
----------------------------\n
Total Months: {len(months)}\n
Total: ${sum(totals)}\n
Average Change: ${round(profit_loss_change, 2)}\n
Greatest Increase in Profit: {months[increase_month+1]} (${max(totals_differences)})\n
Greatest Decrease in Profit: {months[decrease_month+1]} (${min(totals_differences)})
"""

#Print output to Terminal
print(output)

#Create path for CSV file to write
data_output = os.path.join("Resources", "budget_data_export.txt")

#Writes budget date output to text file
with open(data_output, "w") as file:
    file.write(output)