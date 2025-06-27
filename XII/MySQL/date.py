# Import the datetime module
import datetime

# Define a MySQL datetime string
dateu = '2023-12-08 15:39:30'

# Parse the MySQL datetime string into a datetime object
obj = datetime.datetime.strptime (dateu, '%Y-%m-%d %H:%M:%S')

# Format the datetime object into a Python date string
strd = obj.strftime ('%Y-%m-%d')

# Print the result
print (strd)
