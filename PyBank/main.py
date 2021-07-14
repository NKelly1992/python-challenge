import os
import csv

budget_data = os.path.join("C:\\Users\\pippi\\OneDrive\\Documents\\NU-Homework\\python-challenge\\Instructions\\PyBank\\Resources\\budget_data.csv")

month = []
month_change_list = []
monthCount = 0
greatestInc = ["", 0]
greatestDec = ["", 0]
netTotal =0
monthChange = 0
monthAverage = 0

with open(budget_data) as financial_analysis:
    csvreader = csv.reader(financial_analysis)
    csvheader = next(csvreader)

    # remove the header from the equation
    first_row = next(csvreader)
    lastMonth = int(first_row[1])

    for row in csvreader:
        # count the month
        monthCount += 1
        # change the net total
        netTotal += int(row[1])
        # calculate monthly change
        monthChange = int(row[1]) - lastMonth
        # track the monthly change
        month_change_list += [monthChange]
        # reset lastMonth
        lastMonth = int(row[1])

        #check for greatest changes
        if monthChange > greatestInc[1]:
            greatestInc[0] = row[0]
            greatestInc[1] = monthChange
        
        if monthChange < greatestDec[1]:
            greatestDec[0] = row[0]
            greatestDec[1] = monthChange

monthAverage = sum(month_change_list)/len(month_change_list)
        
# financial summary
financialSummary = (
    f'Financial Analysis\n'
    f'--------------------\n'
    f'Total Months: {monthCount}\n'
    f'Total: ${netTotal}\n'
    f'Average change: ${monthAverage:.2f}\n'
    f'Greatest Increase in Profits: {greatestInc[0]} - $ {greatestInc[1]} \n'
    f'Greatest Decrease in Profits: {greatestDec[0]} - $ {greatestDec[1]} \n'
)

print(financialSummary)

# Export results
budget_analysis = os.path.join("C:\\Users\\pippi\\OneDrive\\Documents\\NU-Homework\\python-challenge\\Instructions\\PyBank\\", "budget_analysis.txt")
with open(budget_analysis, "w") as txt_file:
    txt_file.write(financialSummary)


