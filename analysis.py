#! /Users/tannerwilliams/Desktop/ME 499/ME499_HW_1_DataAnalysis
import math


def load_data_from_file(filename):
    """
    :param filename: local .csv file with time vs position
    :return: two lists; times and positions
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
    if max_mylist < mynum:
        return
    else:
        # There is a larger value than my number...
        for val in mylist:  # Go through all values in the list
            # Stop when the value is same or larger than my number
            if val >= mynum:
                # Return index of said value
                return mylist.index(val)


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
    """
    :param filename: local .csv file with time vs position
    :return: Rise time of system
    """
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


def settling_time(filename):
    """
    :param filename: local .csv file with time vs position
    :return: 2% settling time of system
    """
    # Distance from initial to final
    disp = abs(c_initial(filename) - c_final(filename))

    # Deviation allowed on either side of final for 2% settling calculation
    window_oneside = disp * 0.02

    # Get lists from csv file from previous function 'load_data_from_file'
    times, positions = load_data_from_file(filename)
    # flip positions across the axis, theoretically, so that we can compare for when min positions enter settle window
    positions_flipped = [-val for val in positions]
    # print(positions_flipped)

    # Use greater_than_index to return the indexes of when positions exit the 2% window
    settle_start_index_high = greater_than_index(positions[::-1], c_final(filename) + window_oneside)
    settle_start_index_low = greater_than_index(positions_flipped[::-1], c_final(filename) + window_oneside)

    # Flip index value forward in time and find the corresponding time value
    settle_start_time_high = times[len(times) - settle_start_index_high]
    settle_start_time_low = times[len(times) - settle_start_index_low]

    # return the maximum time value which is when both sides of window are stable
    return max(settle_start_time_low, settle_start_time_high)


def get_system_params(filename):
    """
    :param filename: local .csv file with time vs position
    :return: mass, spring_constant, damping_ratio of system
    """
    # Using equation 4.39 to calculate the damping ratio
    zeta_439 = (- math.log((perc_overshoot(filename)) / 100)) / \
               ((math.sqrt(math.pi ** 2)) + (math.log((perc_overshoot(filename)) ** 2) / 100))
    # Using equation 4.42 to calculate w_n
    w_n = 4 / (zeta_439 * settling_time(filename))

    # Using equation 4.29 to get the mass, spring constant, and damping ratio
    # Given
    m = 1
    # Spring constant is w_n squared
    k = w_n ** 2
    # Damping ratio is
    c = 2 * zeta_439 * w_n
    return m, k, c


def analyze_data(filename):
    """
    :param filename: local .csv file with time vs position
    :return: system information
    """
    # c_initial(filename)
    # c_max(filename)
    # c_final(filename)
    t_r = rise_time(filename)
    t_p = peak_time(filename)
    percent_overshoot = perc_overshoot(filename)
    T_s = settling_time(filename)
    m, k, c = get_system_params(filename)
    system_dict = {'c_initial': c_initial(filename),
                   'c_max': c_max(filename),
                   'c_final': c_final(filename),
                   'rise_time': t_r,
                   'peak_time': t_p,
                   'perc_overshoot': percent_overshoot,
                   'settling_time': T_s,
                   'system_mass': m,
                   'system_spring': k,
                   'system_damping': c}
    return system_dict


if __name__ == '__main__':
    system = analyze_data('data1.csv')
    for key, value in sorted(system.items()):
        print(key, value)
