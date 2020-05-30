import os
import csv

#import and read csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open (csvpath, 'r', encoding='utf-8') as csvfile:
    csvfile.readline()
    
    csvreader = csv.reader (csvfile, delimiter = ',')

    total_votes=[]
    candidate=[]
    khan=[]
    correy=[]
    li=[]
    otooley=[]
    winner=[]
   

    for row in csvreader:
        total_votes.append(row[0])
        
        if (row[2] == "Khan" ):
            khan.append(row[2])
        elif(row[2] == "Correy"):
            correy.append(row[2])
        elif(row[2] == "Li"):
            li.append(row[2])
        elif(row[2] == "O'Tooley"):
            otooley.append(row[2])   

#totals for candidates

    total_votes_main=len(total_votes)
    
    total_votes1 = len(khan)

    total_votes2 = len(correy)

    total_votes3 = len(li)

    total_votes4 = len(otooley)

#percentages for candidates

    percentage1 = total_votes1/total_votes_main
    percentage1 = ("{:.2%}".format(percentage1))
    
    percentage2 = total_votes2/total_votes_main
    percentage2 = ("{:.2%}".format(percentage2))
    
    percentage3 = total_votes3/total_votes_main
    percentage3 = ("{:.2%}".format(percentage3))
    
    percentage4 = total_votes4/total_votes_main
    percentage4 = ("{:.2%}".format(percentage4))

#winner criteria

    winner=[total_votes1,total_votes2,total_votes3,total_votes4]
    
    final_winner= max(winner)

#winner name

    if final_winner == total_votes1: 
        winner_name= "Khan" 
    elif final_winner == total_votes2:
        winner_name= "Correy" 
    elif final_winner == total_votes3:
        winner_name= "Li" 
    elif final_winner == total_votes4:
        winner_name= "O'Tooley" 

#print statement

print("Election Results")
print("Total Votes: " + str(total_votes_main))
print("Khan: " + str(percentage1) + " (" + str(total_votes1) + ")")
print("Correy: " + str(percentage2) + " (" + str(total_votes2) + ")")
print("Li: " + str(percentage3) + " (" + str(total_votes3) + ")")
print("O'Tooley: " + str(percentage4) + " (" + str(total_votes4) + ")")
print("Winner: " + winner_name)

#output textfile
f = open('PyPoll Results.txt', 'w')
f.write("Election Results")
f.write("\nTotal Votes: " + str(total_votes_main))
f.write("\nKhan: " + str(percentage1) + " (" + str(total_votes1) + ")")
f.write("\nCorrey: " + str(percentage2) + " (" + str(total_votes2) + ")")
f.write("\nLi: " + str(percentage3) + " (" + str(total_votes3) + ")")
f.write("\nO'Tooley: " + str(percentage4) + " (" + str(total_votes4) + ")")
f.write("\nWinner: " + winner_name)
f.close()