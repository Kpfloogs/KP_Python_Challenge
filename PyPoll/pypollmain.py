import csv
from msilib import change_sequence
import os


os.chdir(os.path.dirname(os.path.abspath(__file__))) # sets current directory, so terminal knows which file to run from

#path to collect data from resources folder
csvpath = os.path.join("pypoll Resources","election_data.csv")
totalvotes = 0
winner = ""
charles_votes = 0
diana_votes = 0
raymon_votes = 0
maxvotes = 0

with open(csvpath) as electioncsv:
    csvreader = csv.reader(electioncsv, delimiter=',')
    print(csvreader) 
   
    next(csvreader, None) #skip the header
    

    for row in csvreader:
        totalvotes += 1 # calculating the total number of votes
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row [2] == "Raymon Anthony Doane":
            raymon_votes +=1

        cvotes = charles_votes / totalvotes *100
        dvotes = diana_votes / totalvotes *100
        rvotes = raymon_votes / totalvotes *100

    dict_candidate_vote = {
        "Charles Casper Stockham": charles_votes,
        "Diana DeGette": diana_votes,
        "Raymon Anthony Doane": raymon_votes
    }

#Comparing the amount of votes each candidate receieved and defining the winner
    for candidate, votes in dict_candidate_vote.items(): 
        if votes > maxvotes:
            maxvotes = votes
            winner = candidate


output = f"""
Election Results
-------------------------
Total Votes: {totalvotes}
-------------------------
Charles Casper Stockham: {cvotes:.3f}% ({charles_votes})
Diana DeGette: {dvotes:.3f}% ({diana_votes})
Raymon Anthony Doane: {rvotes:.3f}% ({raymon_votes})
-------------------------
Winner: {winner}
-------------------------
"""
print(output)

#Sending the output to a new txt file
with open("Analysis/pypolloutput.csv",'w') as file:
    file.write(output)