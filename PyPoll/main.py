#!/usr/bin/python
import os
import csv

voterID = []
candidate = []

with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    noheader = next(csvreader, None)
    
    for row in csvreader:
        voterID.append(row[0])
        candidate.append(row[2])

    #total number of votes
    totalVotes = len(list(voterID))
    
    print("Election Results \n -------------------")
    print("Election Results \n -------------------", file=open('PyPoll.txt', 'a'))
    print("Total Votes: " + str(totalVotes) + "\n -------------------")
    print("Total Votes: " + str(totalVotes) + "\n -------------------",file=open('PyPoll.txt', 'a'))
 
    #unique candidates
    uniqCandidates = list(set(candidate))
    
    #for loop to calculate total votes and percentages for each candidate
    for name in uniqCandidates:
        print(name + ":" + "(" + str(candidate.count(name)) + ") " + 
                str(round((candidate.count(name)/totalVotes * 100))) + "%")
        print(name + ":" + "(" + str(candidate.count(name)) + ") " +
                str(round((candidate.count(name)/totalVotes * 100))) + "%",file=open('PyPoll.txt', 'a'))
    
    #count the names in list to identify winner
    nameCounter = {}
    for name in candidate:
        if name in nameCounter:
            nameCounter[name] += 1
        else:
            nameCounter[name] = 1
    names = sorted(nameCounter, key = nameCounter.get, reverse = True)
    print("-------------------\nWinner: " + str(names[:1])) 
    print("-------------------\nWinner: " + str(names[:1]),file=open('PyPoll.txt', 'a'))
