from datetime import datetime

# Current datetime
current_datetime = datetime.now()

# Drop microseconds by replacing them with zero
current_datetime_without_microseconds = current_datetime.replace(microsecond=0)

# Print the datetime without microseconds
print("Current datetime with microseconds:", current_datetime)
print("Current datetime without microseconds:", current_datetime_without_microseconds)