import csv
from msilib import change_sequence
import os


os.chdir(os.path.dirname(os.path.abspath(__file__))) # sets current directory, so terminal knows which file to run from

#path to collect data from resources folder and define variables
csvpath = os.path.join("Resources","budget_data.csv")
totalmonths= 0 
netprofits= 0 
previousprofit = 0
totalchange = 0
increasedate = "" #empty string
greatestincrease = 0
decreasedate = ""
greatestdecrease = 0

with open(csvpath) as budgetcsv:
    csvreader = csv.reader(budgetcsv, delimiter=',')
    print(csvreader)

    next(csvreader, None) #skip the header
    change =0
    changecounter = 0

    for row in csvreader:
        totalmonths += 1  
        netprofits += int(row[1]) 
        currentprofit = int(row[1])

        if previousprofit != 0:
            change = currentprofit - previousprofit
            totalchange += change
            changecounter += 1
        
        previousprofit = currentprofit

        if change > greatestincrease:
            increasedate = row[0]
            greatestincrease = change
            
        if change < greatestdecrease:
            decreasedate = row[0]
            greatestdecrease = change
            

#print(f"{increasedate} {greatestincrease} {decreasedate} {greatestdecrease}") print out test to make sure calcs are correct

output = f"""
Financial Analysis
----------------------------
Total Months: {totalmonths}
Total: ${netprofits}
Average Change: ${totalchange / changecounter:.2f} 
Greatest Increase in Profits: {increasedate} (${greatestincrease})
Greatest Decrease in Profits: {decreasedate} (${greatestdecrease})
"""
print(output)
#:.2f in line 55 tells the code to only look at two decimal places after the decimal

#sending the results to a new txt file
with open("Analysis/pybankoutput.csv",'w') as file:
    file.write(output)