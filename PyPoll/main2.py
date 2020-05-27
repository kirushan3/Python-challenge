import os
import csv



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

    total_votes_main=len(total_votes)
    
    total_votes1 = len(khan)

    total_votes2 = len(correy)

    total_votes3 = len(li)

    total_votes4 = len(otooley)
#percentages for candidates
    percentage1 = total_votes1/total_votes_main

    winner=[total_votes1,total_votes2,total_votes3,total_votes4]
    final_winner= max(winner)
#print winner name, do li and otooley
    if final_winner == total_votes1: 
    winner_name= "Khan" 
    elif final_winner == total_votes2:
    winner_name= "Correy" 

#print statement

#print("Election Results")
#print("Total Votes: " + str(total_votes_main))
#print("Khan: " + str(total_votes1))
#print("Correy: " + str(total_votes2))
#print("Li: " + str(total_votes3))
#print("O'Tooley: " + str(total_votes4))
#print("Winner: winner_name))
#