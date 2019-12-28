import pandas as pd
from itertools import islice
import csv

Sourcedataframe = pd.read_csv("blankAgentList.csv", header=None)
count = 1
count2 = 0

for index, row in Sourcedataframe.iterrows(): #going through each row line by line

    #this for loop counts the amount of times it has gone through the csv file. If it has gone through it more than three times, it resets the counter back to 1.
    for column in Sourcedataframe: 
        if count > 3:
            count = 1

            #if program is on it's first count, it opens the 'Sourcedataframe', reads/writes every third row to a new csv file named 'agentList1.csv'.
        if count == 1:
            with open('blankAgentList.csv') as infile: 
                
              with open('agentList1.csv', 'w') as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                writer.writeheader()
                for row in reader:
                    count2 += 1
                    if not count2 % 3:
                        writer.writerow(row)
            
        elif count == 2:
            with open('blankAgentList.csv') as infile:
              
              with open('agentList2.csv', 'w') as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                #Sourcedataframe.iloc[2, 0]
                writer.writeheader()
                for row in reader:
                    count2 += 1
                    if not count2 % 3:
                        writer.writerow(row)
            
        elif count == 3:
            with open('blankAgentList.csv') as infile:
                
              with open('agentList3.csv', 'w') as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
                writer.writeheader()
                for row in reader:
                    count2 += 1
                    if not count2 % 3:
                        writer.writerow(row)
            
        count = count + 1 #counts how many times it has ran through the main for loop. 


