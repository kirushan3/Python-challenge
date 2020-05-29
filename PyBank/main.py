import os
import csv

#import and read csv

csvpath = os.path.join('Resources', 'Pybank.csv')

with open (csvpath, 'r', encoding='utf-8') as csvfile:
    csvfile.readline()
    
    csvreader = csv.reader (csvfile, delimiter = ',')

    revenue=[]
    date=[]
    net=[]
    average=[]

    for row in csvreader:
        revenue.append(int(row[1]))
        date.append(row[0])
        net = revenue
        net = [int(row) for row in net]
        total_amount=sum(net) 

#average loop

    for i in range(0, len(net) -1):
        average.append(int(net[i+1])-int(net[i]))
        average_final=sum(average)/len(average)

#analysis for total months, total amount, average amount, max prof, min prof

    total_months = len(date)

    total_amount = sum(revenue)

    max_prof = max(average)

    min_prof = min(average)

    max_date = date[average.index(max_prof)]

    min_date = date[average.index(min_prof)]

#print statement, need to update greatest increase/decrease profits

print("Financial Analysis")
print("Total Months: " + str(total_months))
print("Total Profit: $ " + str(total_amount))
print("Average profit: $ " + str(average_final))
print("Greatest Increase in Profits:  " + max_date + " ($" + str(max_prof) + ")")
print("Greatest Decrease in Profits:  " + min_date + " ($" + str(min_prof) + ")")

#output textfile

f = open('PyBank Results.txt', 'w')
f.write("Financial Analysis")
f.write("\nTotal Months: " + str(total_months))
f.write("\nTotal Profit: $ " + str(total_amount))
f.write("\nAverage profit: $ " + str(average_final))
f.write("\nGreatest Increase in Profits:  " + max_date + " ($" + str(max_prof) + ")")
f.write("\nGreatest Decrease in Profits:  " + min_date + " ($" + str(min_prof) + ")")
f.close()