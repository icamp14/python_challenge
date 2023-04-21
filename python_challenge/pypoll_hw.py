
import pandas as pd
from pathlib import Path

election_data = Path('Resources/election_data.csv')

election_data_df = pd.read_csv(election_data)

                    
#variables
candidates = []
total = 0
percent = []
data = {}
votes = []


with open ('election_data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[2] in candidates
    else:
        candidates.append(row[2])
total = -1

for i in range(1, len(candidates)):
    count = 0
    for j in range(len(votes)):
        if candidates [i] =votes[j]:
        count = +1
data [candidates[i]] = count 
        









print(f"Election Results")
print("--------------------")
print(f"Total Votes:")
