import csv

txt_file = "msd.txt"
csv_file = "msd_data.csv"

with open (txt_file, "r") as infile, open(csv_file, "w", newline = "") as outfile:
    reader = infile.readlines()
    writer = csv.writer(outfile)

    # Define column headers
    headers = ["time", "msd"]
    writer.writerow(headers)  # Write headers to CSV

    # Write data, skipping the first two lines
    for line in reader[2:]:
        row = line.strip().split()
        writer.writerow(row)

print(f"Conversion complete: {csv_file} with headers")
