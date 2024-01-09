import os
import csv

# Set the path to your CSV file
csv_path = os.path.join(os.getcwd(), 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

# Read the CSV file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header
    header = next(csvreader)
    
    for row in csvreader:
        # Calculate total months and net total
        total_months += 1
        net_total += int(row[1])
        
        # Calculate changes in profit/loss
        if total_months > 1:
            change = int(row[1]) - previous_profit_loss
            changes.append(change)
            dates.append(row[0])
        
        previous_profit_loss = int(row[1])

# Calculate average change, greatest increase, and greatest decrease
average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Export results to a text file
output_path = os.path.join(os.getcwd(), 'financial_analysis.txt')
with open(output_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${round(average_change, 2)}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Analysis has been printed to the terminal and exported to 'financial_analysis.txt'.")
