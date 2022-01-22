#! /Users/tannerwilliams/Desktop/ME 499/ME499_HW_1_DataAnalysis

# Importing csv files
import csv


def load_data_from_file(filename):
    time_list = []
    position_floats = []
    with open(filename) as file:
        csvreader = csv.reader(file)  # Reader
        next(csvreader)  # Skip the name of the data columns

        for row in csvreader:
            time_list = row
            print(time_list)




load_data_from_file('data1.csv')


#
# def read_my_csv_pedantic(fname):
#     """ Read the file back in again
#     :param fname name of the file
#     :returns a list of tuples
#     """
#
#     # First open the file - notice the 'r' which means read
#     with open(fname, 'r') as f:
#         # This is a class that knows how to read in lines of
#         #  text from a file - it needs a pointer to the file
#         csv_file = csv.reader(f)
#
#         # Place to put the data
#         new_data = []
#         new_data_fancy = []
#
#         # Read in a row at a time, parsing out the elements.  Line is a list.
#         for row in csv_file:
#             # line is a list of strings.  You have to interpret what they are yourself.  In this case, we know that
#             # they're integers, so we use map to apply the int function to each element of the list, then cast this
#             # to a tuple.  Finally, we append this tuple to a list.
#             new_row = []
#             for r in row:
#                 make_int = int(r)
#                 new_row.append(make_int)
#             new_data.append(tuple(new_row))
#
#             # Note that you can do this in one line using
#             #  map, which applies int(r) to each element r in row
#             new_data_fancy.append(tuple(map(int, row)))
#
#         # new_data and new_data_fancy are the same thing
#         return new_data


# if __name__ == '__main__':
#
#     # data1 = read_my_csv_pedantic('data1.csv')
#     file = open('data1.csv', 'r')
#     csv_reader = csv.reader(file)
#     lists_from_csv = []
#     for column in csv_reader:
#         lists_from_csv.append(column)
#
#     print(lists_from_csv)

# def load_data_from_file(file_name):
#     columns = ["Time", "Position"]
#     read = pandas.read_csv(file_name, usecols=columns)
#     print(read["Time"])
#     print(read["Position"])
#
# load_data_from_file("data1.csv")


# def load_data_from_file(file_name):
#     with open(file_name, 'r') as file:
#         csvfile = csv.reader(file)
#         # Time column
#         time_data = []
#         # Position column
#         position_data = []
#
#         for column in csvfile:
#             new_row = []
#             for data in column:
#                 temp_int = int(data)
#                 new_row.append(temp_int)
#             new_data.append()
