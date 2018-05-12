import os
import csv

csvpath = os.path.join('.', "raw_data", "budget_data_1.csv")

#The total number of months included in the dataset
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    t = -1

    for row in csvreader:
        if row[0] != "":
            t = t + 1

#The total amount of revenue gained over the entire period
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    amount = 0
    for total in csvreader:
       if total[1] != "Revenue":
          amount = amount + int(total[1])

#The average change in revenue between months over the entire period
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    change = []
    
    for row in csvreader:
        change.append(row[1])
    change.pop(0)
    change = list(map(int, change))

new = []
j = 0
for items in range(len(change)-1):
    new.append(change[j + 1] - change[j])
    j = j + 1

average_rev_change = round(sum(new)/len(new), 2)

#The greatest increase in revenue (date and amount) over the entire period
print(max(change))
#The greatest decrease in revenue (date and amount) over the entire period
print(min(change))

#summary
print("Financial Analysis")
print("-" * 20)
print("Total Months: " + str(t))
print("Total Revenue: $" + str(amount))
print("Average Revenue Change: $" + str(average_rev_change))
print("Greatest Increase in Revenue: $" + str(max(change)))
print("Greatest Decrease in Revenue: $" + str(min(change)))