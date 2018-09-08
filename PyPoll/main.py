#PyPoll Python Challenge

# Dependencies
import os
import csv

# Set the Input datafile path 
DataFile = os.path.join("election_data.csv")

# Variable Lists to store data
total_votes = 0
candidate = ""
candidate_votes = {}
votes_percentage = {}
winner_vote_count = 0
winner = ""

# Gets data file
with open(DataFile,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Skips header row
    next(csvreader)

# For every row in the input data file checks for votes
    for row in csvreader:

# Total number of votes

        total_votes = total_votes + 1

# List of candidates with vote count
        candidate = row[2]

        if candidate in candidate_votes:

            candidate_votes[candidate] = candidate_votes[candidate] + 1

        else:

            candidate_votes[candidate] = 1

# Calculates percentage and total number of votes for each winner candidate

for person, vote_count in candidate_votes.items():

    votes_percentage[person] = '{0:.3%}'.format(vote_count / total_votes)

# Finds the winner of the election with popular votes
    if vote_count > winner_vote_count:

        winner_vote_count = vote_count

        winner = person

# Prints the election analysis to the terminal

print("Election Results")
print ("--------------------------\n")
print(f"Total Votes: {total_votes}")
print ("\n--------------------------\n")
for person, vote_count in candidate_votes.items():
     print(f"{person}: {votes_percentage[person]} ({vote_count})")
print ("\n--------------------------\n")
print(f"Winner: {winner}")
print ("\n--------------------------")   

# Exports results into text file

output_file = os.path.join("election_data_output.csv")
dashbreak = "-------------------------"

with open(output_file,'w') as text:
    text.write ("Election Results\n")
    text.write(dashbreak + "\n")
    text.write(f"Total Votes: {total_votes}" + "\n")
    text.write(dashbreak + "\n")
    for person, vote_count in candidate_votes.items():
        text.write(f"{person}: {votes_percentage[person]} ({vote_count})" + "\n")
    text.write(dashbreak + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write(dashbreak + "\n")
