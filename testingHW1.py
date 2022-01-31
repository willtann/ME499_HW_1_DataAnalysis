# print('testing')
# # load_data_from_file('data1.csv')
# print(greater_than_index([-3.2, -2.2, -1.1], -4.0))
#
# print('Initial position = ', c_initial('data1.csv'))
# print('Max position = ', c_max('data1.csv'))
# print('Final position = ', c_final('data1.csv'))
#
print('Rise time = ', rise_time('data1.csv'))

print('Peak time = ', peak_time('data1.csv'))

print('Percent overshoot = ', perc_overshoot('data1.csv'))

print('Settling time (2%) = ', settling_time('data1.csv'))

get_system_params('data1.csv')