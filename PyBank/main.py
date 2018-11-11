import os 
import csv
csvpath = "Resources/budget_data.csv"
destination = "Final/budget.txt"

total_mon = 0
total_amt = 0
diff = 0
prev_amt = 0 
monthlychange = []
maxinc = 0
maxdec = 0

#convert budget_data to dictionary

with open(csvpath) as data:
    reader = csv.DictReader(data)

#tract total months

    for row in reader:
        total_mon = total_mon + 1
        total_amt = total_amt + int(row ['Profit/Losses'])

        if total_mon > 1:
            diff = int(row["Profit/Losses"])- prev_amt
            monthlychange.append(diff)

        if diff > maxinc:
            maxinc = diff
            maxincmonth = row['Date']

        if diff < maxdec:
            maxdec = diff
            maxdecmonth = row['Date']

prev_amt = int(row["Profit/Losses"])
avg = round(sum(monthlychange)/len(monthlychange)+0.0,2)

# avg = sum(monthlychange) / len(monthlychange)
output = ("Total number of months = "+ str(total_mon)+'\n' +
"Total net amount of Profit/Losses = " + str(total_amt) + '\n' +
"Average change in Profit/Losses between months = " + str(avg) + '\n' +
"The greatest increase in Profit/Losses (date and amount) = " + str(maxincmonth) + " " + "$" + str(maxinc) + '\n' +
"The greatest decrease in Profit/Losses (date and amount) = " + str(maxdecmonth) + " " + "$" + str(maxdec) + '\n')
print(output)
'''
with open(destination, 'w') as destinationfile :
    destinationfile.write(Final)
'''