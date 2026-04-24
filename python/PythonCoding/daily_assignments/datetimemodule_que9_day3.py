# Use the Datetime Module:
# Write a program that imports the datetime module and uses it to:
# Get and print the current date and time .
# Calculate and print the number of days between two dates.
# Format and print the current date in the format "DD-MM-YYYY"

from datetime import datetime

now = datetime.now()
print("Current Date and Time: ", now)

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12,31)
difference = (date2 - date1).days
print("Days between: ", difference)

formatted_date = now.strftime("%d-%m-%Y")
print("Formatted Date: ", formatted_date)