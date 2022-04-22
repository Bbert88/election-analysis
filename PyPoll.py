#Deliverables
#Total number of votes cast
#Complete list of candidates who received votes
#Percentage of votes each candidate won
#Total numer of votes each candidate won
#Winner of the election based on popular vote

import csv
#module to open file which direct path is unknown
import os

#assign a variable for the file to load and the path
#file_to_load = 'Resources\election_results.csv' -- also works to open the file using direct path
file_to_load = os.path.join('Resources', 'election_results.csv')

#Create a filename variable to a path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize variables needed
totalvotes = 0
candidatelist = []
candidatevotes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    #read and analyze data
    filereader = csv.reader(election_data)

    #returns header row
    headers = next(filereader)
    

   
    for row in filereader:
        
        #Count total votes in election
        totalvotes = totalvotes + 1  #can also be written as 'totalvotes += 1'
    
        #Get candidate name 
        candidatename = row[2]

        #check if candidate is already in list, if not then add to list
        if candidatename not in candidatelist:
            candidatelist.append(candidatename)
            #begin tracking each candidates vote count
            candidatevotes[candidatename] = 0
        #increment candidates vote count
        candidatevotes[candidatename] += 1

    #open txt output file to write to
    with open(file_to_save, 'w') as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"--------------------------\n"
            f"Total Votes: {totalvotes:,}\n"
            f"--------------------------\n"
        )

        #print to terminal and txt file
        print(election_results, end="")
        txt_file.write(election_results)
            
    
        #calculate each candidates vote percentage using candidatelist and candidatevotes dict    
        for cand in candidatelist:
            votes = candidatevotes[cand]
            votepercent = float(votes) / float(totalvotes) * 100

            #print each candidates results to terminal and txt file
            candidate_results = (f"{cand}: {votepercent:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

            #determine winning candidate, their vote count, and percentage
            if votes > winning_count:
                winning_count = votes
                winning_percentage = votepercent
                winning_candidate = cand

        #print winning candidate, their vote count, and percentage to terminal and txt file 
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------"
        )

        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)
