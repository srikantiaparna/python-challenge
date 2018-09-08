##PyBank Python Challenge
import os
import csv

# Setting Path for input data file and output file
file_to_Load = os.path.join("budget_data.csv")
file_to_output = os.path.join("budget_data_output.csv")

# Assign variables as empty lists, empty dictionary and default
months = []

total_revenue = 0

rev_last_num = 0

revenue_change_dict = {}

total_change = 0 

# Open and Read the data file 
with open(file_to_Load, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip Header Row
    next(csvreader)
    # Loop through all the rows of data
    for row in csvreader:
     
        # Calculate Total net amount of profits/losses over entire period

        total_revenue = total_revenue + int(row[1])

        # Calculate Total number of months to count 

        if row[0] not in months:

            months.append(row[0])

            # Calculate Monthly changes 

            revenue_change_dict[row[0]] = int(row[1]) - rev_last_num

            rev_last_num =  int(row[1])
  

for key, value in revenue_change_dict.items():

    # Skip first month, revenue change starts with 2nd value.

    if key == months[0]:

        num = 0

    else:

        # Calculate Total change for Average 

        total_change = total_change + value

# Find months of Min and Max Changes

min_price = min(zip(revenue_change_dict.values(), revenue_change_dict.keys()))

max_price = max(zip(revenue_change_dict.values(), revenue_change_dict.keys()))



min_change = (min_price[1] + " ($" + str(int(min_price[0]))+")")

max_change = (max_price[1] + " ($" + str(int(max_price[0]))+")")


# Total number of months
Total_months = len(months)

Avg_Change = str(round(total_change/(Total_months - 1), 2))

# Financial Analysis Output

line = "----------------------------------------------------"

output = (
    f"\nFinancial Analysis\n"
    f"--------------------------------------------------\n"
    f"Total Months: {Total_months}\n"
    f"Total: ${total_revenue}\n"
    f"Average Change: ${Avg_Change}\n"
    f"Greatest Increase in Profits: {max_change}\n"
    f"Greatest Decrease in Profits: {min_change}\n"
    )


print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)



