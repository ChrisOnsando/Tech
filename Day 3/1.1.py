
import numpy as np
  

today = np.datetime64('today', 'D')
print("Today: ", today)
  

yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
  
print("Yesterday: ", yesterday)
  

tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
  
print("Tomorrow: ", tomorrow)