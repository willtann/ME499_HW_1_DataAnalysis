#! /Users/tannerwilliams/Desktop/ME 499/ME499_HW_1_DataAnalysis


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
            return times, positions
        else:
            raise ValueError('Lists of data and times are not of same length')


def greater_than_index(mylist, mynum):
    """
    :param mylist: list of any numbers
    :param mynum: specified number
    :return: first instance of a value in list that is greater than or equal to mynum
    """
    # Check if there are any values in my list larger than my number
    max_mylist = max(mylist)
    # print(max_mylist)
    if str(max_mylist) < str(mynum):
        return
    else:
        # There is a larger value than my number...
        for val in mylist:  # Go through all values in the list
            # Stop when the value is same or larger than my number
            if val >= mynum:
                # Return index of said value
                return mylist.index(val)

            # if val < mynum:
            #     continue
            # else:
            #     # Return index of that number
            #     return print('Position of value in list', mylist.index(val))


def c_initial(filename):
    """
    :param filename: local .csv file with time vs position
    :return: the initial measured position
    """
    # Get lists from csv file from previous function 'load_data_from_file'
    times, positions = load_data_from_file(filename)
    # return the first index
    # print('Initial position = ')
    return positions[0]


def c_max(filename):
    """
    :param filename: local .csv file with time vs position
    :return: the maximum measured position
    """
    # Get lists from csv file from previous function 'load_data_from_file'
    times, positions = load_data_from_file(filename)
    # return max of positions
    # print('Max displacement from initial position = ')
    return max(positions)


def c_final(filename):
    """
    :param filename: local .csv file with time vs position
    :return: the final measured position
    """
    # Get lists from csv file from previous function 'load_data_from_file'
    times, positions = load_data_from_file(filename)
    # return the last index of positions
    # print('Final position of system = ')
    return positions[-1]


def rise_time(filename):
    # Get lists from csv file from previous function 'load_data_from_file'
    times, positions = load_data_from_file(filename)
    # Retrieve c_initial and c_final... find displacement
    disp = c_initial(filename) - c_final(filename)
    # print(disp)
    # Calculate 10% and 90% values
    rise_10 = 0.9 * disp
    rise_90 = 0.1 * disp
    # Find positions that are closest to these values
    rise_10_index = greater_than_index(positions, rise_10)
    # print(rise_10_index)
    rise_90_index = greater_than_index(positions, rise_90)
    # print(rise_90_index)
    # Find corresponding time-stamps and calculate the elapsed time
    return times[rise_90_index] - times[rise_10_index]


def peak_time(filename):
    """
    :param filename: local .csv file with time vs position
    :return: time for system to reach max position
    """
    # Get lists from csv file from previous function 'load_data_from_file'
    times, positions = load_data_from_file(filename)
    # Retrieve c_peak
    peak = c_max(filename)
    peak_index = greater_than_index(positions, peak)
    # print(peak_index)
    # return time corresponding to the max position or 'peak time'
    # print('Peak time (s) for system = ')
    return times[peak_index]


def perc_overshoot(filename):
    """
    :param filename: local .csv file with time vs position
    :return: percent overshoot of system
    """
    # Retrieve c_initial, c_max, and c_final
    # Distance from initial to final
    disp = abs(c_initial(filename) - c_final(filename))
    # Distance from final to max
    net_disp = abs(c_max(filename) - c_final(filename))
    # How much did max overshoot the final position
    return (net_disp / disp) * 100


# def settling_time(filename):


# if __name__ == '__main__':
#     # load_data_from_file('data1.csv')
#     # greater_than_index([1.1, 2.2, 3.3, 4.4, 5.5], 100.5)
#
#     print('Initial position = ', c_initial('data1.csv'))
#     print('Max position = ', c_max('data1.csv'))
#     print('Final position = ', c_final('data1.csv'))
#
#     print('Rise time = ', rise_time('data1.csv'))
#
#     print('Peak time = ', peak_time('data1.csv'))
#
#     print('Percent overshoot = ', perc_overshoot('data1.csv'))
#
#     # print('Settling time (2%) = ', settling_time('data1.csv'))
