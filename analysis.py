#! /Users/tannerwilliams/Desktop/ME 499/ME499_HW_1_DataAnalysis
import csv


def load_data_from_file(filename):
    """
    times is a list of floats
    positions is a list of floats
    """
    with open(filename, "r") as file:  # Open and read desired csv file
        times = []
        positions = []
        for line in file.readlines()[1:]:
            i = line.split(",")
            # Known: first column holds times and second holds positions
            times.append(i[0])
            positions.append(i[1])
        if len(times) == len(positions):  # Check that lists are same length
            # Storing each entry from respective columns in new lists
            positions = [float(position) for position in positions]
            times = [float(time) for time in times]
            return positions[:] and times[:]
        else:
            raise ValueError('Lists of data and times are not of same length')


def greater_than_index(mylist, mynum):
    """
    :param mylist: list of any numbers
    :param mynum: specified number
    :return: first instance of a value in list that is greater than or equal to mynum
    """
    max_mylist = max(mylist)
    if max_mylist < mynum:
        return
    else:
        for val in mylist:  # Go through all values in the list
            # Go through list as long as val in mylist is smaller than mynum
            if val < mynum:
                continue
            else:
                # Return index of that number
                return print('Position of value in list', mylist.index(val))


def c_initial(filename):
    data = load_data_from_file(filename)
    print(data[:10])
    return

# def c_max(*args):


if __name__ == '__main__':
    print(load_data_from_file('data1.csv'))
    # greater_than_index([1, 3, 4, 7, 10], 6)
    # greater_than_index([-2.5, 1, 4, 8, 4, 1, -2.5], 4)
    # greater_than_index([1.1, 2.2, 3.3, 4.4, 5.5], 100.5)

    # c_initial('data1.csv')
