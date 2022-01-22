#! /Users/tannerwilliams/Desktop/ME 499/ME499_HW_1_DataAnalysis

# Importing csv files
import csv


def load_data_from_file(filename):
    # Open indicated file and read
    csv_open = open(filename, 'r')
    # csv_read = csv.DictReader(csv_reader)
    csv_list = list(csv_open)

    # Make a new home for read data
    time = []
    position = []

    # Read through entire column and write all entries under the given name into a list
    for col in csv_list:
        time.append(col['Time'])
        position.append(col['Position'])

        for i in col:
            abyss = float(position(i))


# # BEST PERSONAL WORK
# # Open and read desired csv file
# csv_file = open('data1.csv', 'r')
# csv_read = csv.reader(csv_file)

# # Make two empty lists to fill with their respective data
# time = []
# position = []
#
# # Run for loop for as long as it takes to iterate for each row in .csv
# for i in range(len(csv_file)):


if __name__ == '__main__':
    load_data_from_file('data1.csv')

