#! /Users/tannerwilliams/Desktop/ME 499/ME499_HW_1_DataAnalysis
import csv


def load_data_from_file_test(file_name):
    with open(file_name, 'r') as data:
        rows = csv.reader(data, delimiter= ' ')
        print(rows)
        next(rows)  # Skip the headers.
# csv file time|position
# 500 rows
#GOAL:



    print(floats)
