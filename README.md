# Election Analysis

## Project Overview
A Colorado Board of Elections employee requested the following tasks to be completed in regards to the election audit of a recent local congressional election. Python will be used for this analysis along with Visual Studio Code, Git, and Github.com. The election data was provided, see the *election_results.csv* file. This file will be accessed, read, and analyzed with the results being written in to a new txt file, see *election_analysis.txt*. An explanation of the methods used will be explained in the Summary section. Please see the below list of tasks which will be completed:
1. Calculate the total number of votes cast.
2. Formulate a complete list of candidates who received votes.
3. Calculate the total votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Analyize the data based on the counties in which the votes were cast.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Results

The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana Degette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the total vote and 85,213 votes. 
    - Diana Degette received 73.8% of the total vote and 272,892 votes. 
    - Raymon Anthony Doane received 3.1% of the total vote and 11,606 votes.
- The winner of the election was Diana Degette who received 272,892 votes accounting for 73.8% of the total votes. 
- The county results were: 
    - Jefferson County accounted for 10.5% of the total vote (38,855 votes).
    - Denver County accounted for 82.8% of the total vote (306,055 votes). 
    - Arapahoe County accounted for 6.7% of the total vote (24,801 votes). 
- The county with the largest voter turnout was Denver by a wide margin. 


provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
## Summary

It is clear that some powerful tools were used in this project. Python, coupled with other applications, can accomplish 
cumbersome tasks with ease. Another great attribute of this Python script is that it can be used repeatedly for other
elections. This script can analyze any set of election data which is provided, with only a few modifications. It is my proposal that this script be considered for use in all future elections. The script would not need to be changed due to varying number of counties, candidates, or votes. A few examples of simple changes which could be made to allow for the analysis of another election are as follows:
- ![filetoload](Resources\filetoload.png)
This image represents the line of code which assigns the file path to a variable. The 'election_results.csv' would need to be edited to match the csv file name for additional election data sets. This is a simple change which could be managed quite easily. 
- 