import csv

# Input and output file names
txt_file = "Al_SC_900.def1.txt"  # Replace with your txt file
csv_file = "data.csv"

# Open the TXT file for reading and the CSV file for writing
with open(txt_file, "r") as infile, open(csv_file, "w", newline="") as outfile:
    reader = infile.readlines()
    writer = csv.writer(outfile)

    # Define column headers
    headers = ["Strain", "-pxx/10000", "-pyy/10000", "-pzz/10000"]
    writer.writerow(headers)  # Write headers to CSV

    # Write data, skipping the first line
    for line in reader[1:]:
        row = line.strip().split()
        writer.writerow(row)

print(f"Conversion complete: {csv_file} with headers")

