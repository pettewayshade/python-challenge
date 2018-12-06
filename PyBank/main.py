#
import os
import csv

#variables to hold the data from each column in csv
months = []
profitLose = []

#read in file
with  open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    #for loop to append the data to months and profitLose
    for row in csvreader:
        months.append(row[0])
        profitLose.append(row[1])

    #get the number of months    
    totalMonths = len(list(months))
    
    #for loop to sum the profits and losses 
    total = 0
    for profit in profitLose:    
        total += float(profit)
    
    #list comprehension to subtract previous month's num from current
    change = [float(y)-float(x) for x, y in zip(profitLose, profitLose[1:])]
    
    # for loop to sum numbers in change list
    changeSum = 0
    for num in change:
        changeSum += float(num)
    
    #getting average
    averageChange = changeSum / len(list(change))    

    #get max and min in change list
    greatestInc = max(change)
    greatestDec = min(change)
    posInc = [i for i, x in enumerate(change) if x == greatestInc]
    posDec = [i for i, x in enumerate(change) if x == greatestDec]
    monthPosI = posInc[0]+1
    monthPosD = posDec[0]+1

#print output to txt file
print("Financial Analysis \n ----------------", file=open('PyBank.txt', 'a'))
print("Total Months: " + str( totalMonths), file=open('PyBank.txt', 'a'))
print("Total: $" + str(round(total)), file=open('PyBank.txt', 'a'))
print("Average Change: $" + str(round(averageChange, 2)), file=open('PyBank.txt', 'a'))
print("Greatest Increase in Profits: " +str(months[monthPosI]) + " $" + str(round(greatestInc)), file=open('PyBank.txt', 'a'))
print("Greatest Decrease in Profits: " +str(months[monthPosD]) + " $" + str(round(greatestDec)), file=open('PyBank.txt', 'a'))

#print to terminal
print("Financial Analysis \n ----------------")
print("Total Months: " + str(totalMonths))
print("Total: $" + str(round(total)))
print("Average Change: $" + str(round(averageChange, 2)))
print("Greatest Increase in Profits: " +str(months[monthPosI]) + " $" + str(round(greatestInc)))
print("Greatest Decrease in Profits: " +str(months[monthPosD]) + " $" + str(round(greatestDec)))
