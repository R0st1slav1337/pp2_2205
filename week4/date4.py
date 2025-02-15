from datetime import datetime

# Define two random dates
date1 = datetime(2025, 2, 10, 12, 0, 0)
date2 = datetime(2025, 2, 15, 12, 0, 0)

# Calculate the difference between the two dates
difference = date2 - date1

# Get the difference in seconds
difference_in_seconds = difference.total_seconds()

# Print the difference in seconds
print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in seconds:", difference_in_seconds)