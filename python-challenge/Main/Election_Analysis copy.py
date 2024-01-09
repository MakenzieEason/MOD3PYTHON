import os
import csv

# Set the path to your CSV file
csv_path = os.path.join(os.getcwd(), 'election_data.csv')

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header
    header = next(csvreader)
    
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        candidate_name = row[2]
        candidates[candidate_name] = candidates.get(candidate_name, 0) + 1

        # Check for the winner
        if candidates[candidate_name] > winner["votes"]:
            winner["name"] = candidate_name
            winner["votes"] = candidates[candidate_name]

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner['name']}")
print("-------------------------")

# Export results to a text file
output_path = os.path.join(os.getcwd(), 'election_results.txt')
with open(output_path, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner['name']}\n")
    output_file.write("-------------------------\n")

print("Analysis has been printed to the terminal and exported to 'election_results.txt'.")
