# importing the module
import csv

def load_data_from_file(csvfile):
# Open indicated file and read
filename = open(csvfile, 'r')
file = csv.DictReader(filename)

# Make a new home for read data
time = []
position = []

# Read through entire column and write all entries under the given name into a list
for col in file:
    time.append(col['Time'])
    position.append(col['Position'])

print(time)
print(position)

