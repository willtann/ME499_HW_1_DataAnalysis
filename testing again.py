#! /Users/tannerwilliams/Desktop/ME 499/ME499_HW_1_DataAnalysis
import csv


def load_data_from_file_test(file_name):
    with open(file_name, 'r') as data:
        rows = csv.reader(data, delimiter= ' ')
        next(rows)  # Skip the headers.
        floats = [[item for number, item in enumerate(row) if item and (1 <= number <= 12)] for row in rows]

    print(floats)
