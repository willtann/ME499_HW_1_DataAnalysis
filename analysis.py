#! /Users/tannerwilliams/Desktop/ME 499/ME499_HW_1_DataAnalysis

# Importing csv files
import csv


def load_data_from_file(filename):
    with open(filename, "r") as file:  # Open and read desired csv file
        times = []
        positions = []

        for line in file.readlines()[1:]:
            l = line.split(",")
            times.append(l[0])
            positions.append(l[1])

        positions = [float(position) for position in positions]

        """
        times is a list of strings ( if you want it to be a list of floats then do... times = [float(time) for time in times]
        positions is a list of floats
        """


# BEST PERSONAL WORK
# Open and read desired csv file
csv_file = open('data1.csv', 'r')
csv_read = csv.reader(csv_file)

# Make two empty lists to fill with their respective data
time = []
position = []

# Run for loop for as long as it takes to iterate for each row in .csv
for i in range(len(csv_file)):


if __name__ == '__main__':
    load_data_from_file('data1.csv')

