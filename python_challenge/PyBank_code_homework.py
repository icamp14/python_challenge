#import modules
import os
import csv

#path
budget_data.csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

#variables
total_months = []
total_profits = []
monthly_changes = []
total = 0 

#open csv file
with open('budget_data.csv') as csvfile:
    csvreader =csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    #loop
    for row in csvreader:
        total_months.append(row[0])
        total_profits += int(row[1])
        monthly_changes = int(row[1]) - total
        monthly_changes.append(monthly_changes)
        total += int(row[1])
    
    for nr in range(len(total_months)-1):
        monthly_changes.append(int(total_profits[nr+1]) - int(total_profits[nr]))
    
    
    
    data_max_date = monthly_changes.index(max(monthly_changes))
    data_min_date = monthly_changes.index(max(monthly_changes))
    
    max_date = total_months[data_max_date]
    min_date = total_months[data_min_date]
    average_change = round(int(sum(monthly_changes))/(int(len(total_months))-2),2)
    
    
    

#results
print("Financial Analysis")
print("----------------------------")
print(f'Total months: {len(total_months)}')
print('Total: ${total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {max_date} $({max(monthly_changes)})')
print(f'Greatest Decrease in Profits: {min_date} $({min(monthly_changes)})')
print("next")

textfile = open('', 'w')
textfile.write("Financial Analysis \n")
textfile.write("----------------------------\n")
textfile.write(f'Total Months: {len(total_months)}\n')
textfile.write(f'Total: ${total}\n')
textfile.write(f'Greatest Increase in Profits: {max_date} $({max(monthly_changes)})')
textfile.write(f'Greatest Decrease in Profits: {min_date} $({min(monthly_changes)})')
