#Reading file to list:
file_content = open("election_data.csv", "r").readlines()[1:]

#Creation and filling lists for id, counties, and candidates:
id_list = []
candidate_list = []
for i in file_content:
    splitted_line = i.split(",")
    id_list.append(splitted_line[0])
    candidate_list.append(splitted_line[2])

#Cleaning list of candidates:
candidate_list = [i.replace("\n", "") for i in candidate_list]

#Determination of number of votes:
votes_n = len(id_list)

#Determination of results of every candidate:
unique_candidates = sorted(list(set(candidate_list)))
unique_candidates_counts = []
for i in unique_candidates:
    count = 0
    for j in candidate_list:
        if i == j:
            count = count + 1
    unique_candidates_counts.append(count)
unique_candidates_percentages = [100 * i / votes_n for i in unique_candidates_counts]

#Determination of winner:
best_result = max(unique_candidates_counts)
for i in range(0, len(unique_candidates_counts)):
    if unique_candidates_counts[i] == best_result:
        best_result_candidate = unique_candidates[i]

#Displaying results:
print("Election Results")
print("-" * 28)
print("Total Votes: " + str(votes_n))
print("-" * 28)
for i in range(0, len(unique_candidates)):
    print(unique_candidates[i] + ": " + "{:.3f}".format(unique_candidates_percentages[i]) +
          "% (" + str(unique_candidates_counts[i]) + ")")
print("-" * 28)
print("Winner: " + best_result_candidate)
print("-" * 28)

#Writing results to file:
output_file = open("PyPollResults.txt", "w")
output_file.write("Election Results" + "\n")
output_file.write("-" * 28  + "\n")
output_file.write("Total Votes: " + str(votes_n)  + "\n")
output_file.write("-" * 28  + "\n")
for i in range(0, len(unique_candidates)):
    output_file.write(unique_candidates[i] + ": " + "{:.3f}".format(unique_candidates_percentages[i]) +
          "% (" + str(unique_candidates_counts[i]) + ")"  + "\n")
output_file.write("-" * 28  + "\n")
output_file.write("Winner: " + best_result_candidate  + "\n")
output_file.write("-" * 28  + "\n")
output_file.close()

