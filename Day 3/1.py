# Write a NumPy program to get the dates of yesterday,today and tomorrow
import numpy as np

todays_date = np.datetime64('today', 'D')
print("Today's Date: ", todays_date)

yesterdays_date = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yesterday's Date: ", yesterdays_date)

tomorrows_date = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow's Date: ", tomorrows_date)