# Import the datetime and timedelta classes from the datetime module
from datetime import datetime, timedelta

# Today's date
today = datetime.now()

# Calculate yesterday's date
yesterday = today - timedelta(days=1)

# Calculate tomorrow's date
tomorrow = today + timedelta(days=1)

# Print the dates
print("Yesterday's date:", yesterday.strftime("%d-%m-%Y"))
print("Today's date:", today.strftime("%d-%m-%Y"))
print("Tomorrow's date:", tomorrow.strftime("%d-%m-%Y"))