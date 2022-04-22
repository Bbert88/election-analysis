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

#Open the election results and read the file
with open(file_to_load) as election_data:

    #read and analyze data
    filereader = csv.reader(election_data)

    #prints each row in the csv file
    for row in filereader:
        print(row)

    #print file object
    

#open text file using with statement
#with open(file_to_save, 'w') as txt_file:

    #write to the txt file using write() function
    #txt_file.write("Counties in the Election\n---------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")



#3.4.4

