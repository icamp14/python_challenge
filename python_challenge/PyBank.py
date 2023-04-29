#Reading file to list:
file_content = open("budget_data.csv", "r").readlines()[1:]

#Creation and filling lists for dates and values:
dates_list = []
values_list = []
for i in file_content:
    splitted_line = i.split(",")
    dates_list.append(splitted_line[0])
    values_list.append(splitted_line[1])

#Conversion of values to integer format:
values_list = [int(i) for i in values_list]

#Determination of number of months:
months_n = len(dates_list)

#Determination of total amount:
total_amount = sum(values_list)

#Determination of average change:
changes = []
for i in range(1, len(values_list)):
    changes.append(values_list[i] - values_list[i-1])
average_change = sum(changes) / len(changes)

#Determination of best change and its month:
max_change = max(changes)
for i in range(0, len(changes)):
    if changes[i] == max_change:
        max_change_month = dates_list[i + 1]

#Determination of worse change and its month:
min_change = min(changes)
for i in range(0, len(changes)):
    if changes[i] == min_change:
        min_change_month = dates_list[i + 1]

#Displaying results:
print("Financial Analysis")
print("-" * 28)
print("Total Months: " + str(months_n))
print("Total: $" + str(total_amount))
print("Average Change: $" + "{:.2f}".format(average_change))
print("Greatest Increase in Profits: " + max_change_month + " ($" + str(max_change) + ")")
print("Greatest Decrease in Profits: " + min_change_month + " ($" + str(min_change) + ")")

#Writing results to file:
output_file = open("PyBankResults.txt", "w")
output_file.write("Financial Analysis" + "\n")
output_file.write("-" * 28 + "\n")
output_file.write("Total Months: " + str(months_n) + "\n")
output_file.write("Total: $" + str(total_amount) + "\n")
output_file.write("Average Change: $" + "{:.2f}".format(average_change) + "\n")
output_file.write("Greatest Increase in Profits: " + max_change_month + " ($" + str(max_change) + ")" + "\n")
output_file.write("Greatest Decrease in Profits: " + min_change_month + " ($" + str(min_change) + ")" + "\n")
output_file.close()
