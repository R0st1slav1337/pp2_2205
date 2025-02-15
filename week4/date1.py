# Import the datetime and timedelta classes from the datetime module
from datetime import datetime, timedelta 
# Current date
current_date = datetime.now()

# Subtract five days from the current date
new_date = current_date - timedelta(days=5)

# Print the new date
print("Current date:", current_date.strftime("%Y-%m-%d"))
print("Date five days ago:", new_date.strftime("%Y-%m-%d"))