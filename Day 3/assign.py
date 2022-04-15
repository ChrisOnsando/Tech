import numpy as np

def my_array():
    z = np.array(["1, 435, 56633, 2400, 868"])
    return(z)
my_array()

def my_dates():
    todays_date = np.datetime64('today', 'D')
    print("Today's Date: ", todays_date)

    yesterdays_date = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
    print("Yesterday's Date: ", yesterdays_date)

    tomorrows_date = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
    print("Tomorrow's Date: ", tomorrows_date)

my_dates()   