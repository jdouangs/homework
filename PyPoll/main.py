import os
import csv

csvpath = os.path.join('.', "raw_data", "election_data_1.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    
#The total number of votes cast
    voter_id = []

    for row in csvreader:
        voter_id.append(row[0])
    total_votes = len(voter_id) - 1


#A complete list of candidates who received votes
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")  

    candidates = []

    for votes in csvreader:
        if votes[2] in candidates:
            pass
        else:
            candidates.append(votes[2])
    candidates.remove("Candidate")

first_candidate = candidates[0]
second_candidate = candidates[1]
third_candidate = candidates[2]
fourth_candidate = candidates[3]

#The total number of votes each candidate won
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")  

    candidate_0 = 0
    candidate_1 = 0
    candidate_2 = 0
    candidate_3 = 0

    for total in csvreader:
        if total[2] == candidates[0]:
            candidate_0 = candidate_0 + 1
        elif total[2] == candidates[1]:
            candidate_1 = candidate_1 + 1
        elif total[2] == candidates[2]:
            candidate_2 = candidate_2 + 1
        else:
            candidate_3 = candidate_3 + 1

            
#The percentage of votes each candidate won
candidate0_percentage = round(int(candidate_0)/int(total_votes)*100, 2)
candidate1_percentage = round(int(candidate_1)/int(total_votes)*100, 2)
candidate2_percentage = round(int(candidate_2)/int(total_votes)*100, 2)
candidate3_percentage = round(int(candidate_3)/int(total_votes)*100, 2)

#The winner of the election based on popular vote.

winner = [candidate0_percentage, candidate1_percentage, candidate2_percentage, candidate3_percentage]

#summary of results
print("Election Results")
print("-" * 20)
print("Total Votes: " + str(total_votes))
print("-" * 20)
print(first_candidate + ": " + str(candidate0_percentage) + "% " + "(" + str(candidate_0) + ")")
print(second_candidate + ": " + str(candidate1_percentage) + "% " + "(" + str(candidate_1) + ")")
print(third_candidate + ": " + str(candidate2_percentage) + "% " + "(" + str(candidate_2) + ")")
print(fourth_candidate + ": " + str(candidate3_percentage) + "% " + "(" + str(candidate_3) + ")")
print("-" * 20)
if max(winner) == winner[0]:
    print("Winner: " + first_candidate)
elif max(winner) == winner[1]:
    print("Winner: " + second_candidate)
elif max(winner) == winner[2]:
    print("Winner: " + third_candidate)
else:
    print("Winner: " + fourth_candidate)