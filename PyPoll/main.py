import os
import csv

polling_csv = os.path.join("C:\\Users\\pippi\\OneDrive\\Documents\\NU-Homework\\python-challenge\\Instructions\\PyPoll\\Resources\\election_data.csv")
polling_analysis = os.path.join("C:\\Users\\pippi\\OneDrive\\Documents\\NU-Homework\\python-challenge\\Instructions\\PyPoll\\Resources\\election_analysis.txt")

total_votes = 0
Candidate_List = []
Candidate_Votes = {}
Candidate_Percentage = {}
Winning_Candidate = []
Winning_Tally = 0

with open(polling_csv) as Election_Results:
    reader = csv.reader(Election_Results)
    
    #skip the header
    header = next(reader)

    for row in reader:
        # count the total votes
        total_votes += 1
        # add to the list of candidates
        Candidate = row[2]
        if Candidate not in Candidate_List:
            Candidate_List.append(Candidate)
            Candidate_Votes[Candidate] = 0
        # count votes for each candidate
        Candidate_Votes[Candidate] += 1

    for Candidate in Candidate_Votes:
        Votes = Candidate_Votes[Candidate]
        Vote_Percentage = Votes / total_votes * 100
        Candidate_Percentage[Candidate] = Vote_Percentage
        if Votes> Winning_Tally:
            Winning_Candidate = Candidate
            Winning_Tally = Votes

#print the results
with open(polling_analysis, 'w') as txt_file:
    ElectionResults = (
        f'Election Results\n'
        f'--------------------\n'
        f'Total Votes: {total_votes} \n'
        f'--------------------\n'
    )
    
    print(ElectionResults)
    
    txt_file.write(ElectionResults)

    for Candidate in Candidate_Votes:
        Results_by_candidate = f'{Candidate}: {Candidate_Percentage[Candidate]:.2f}% ({Votes})'
        print(Results_by_candidate)
        txt_file.write(Results_by_candidate)

    The_Winner = (
        f'--------------------\n'
        f'Winner: {Winning_Candidate}\n'
        f'--------------------\n'
    )
    
    print(The_Winner)

    txt_file.write(The_Winner)



