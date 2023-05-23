# Date: 2023-05-23 
# Author: Shiwen An 
# Purpose: Try to summarize the investment on AMD Stock. 
# Take a look at the price and volume chart daily and weekly

import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# replace YOUR_API_KEY with your actual Alpha Vantage API key
API_KEY = 'YOUR_API_KEY'  
API_KEY = 'E2S7MZC034PYLV42'


# Create a TimeSeries object
ts = TimeSeries(key=API_KEY, output_format='pandas')

# Get daily data for AMD
data_daily, meta_data_daily = ts.get_daily(symbol='AMD', outputsize='full')

# Get weekly data for AMD
data_weekly, meta_data_weekly = ts.get_weekly(symbol='AMD')

# Plot daily data
data_daily['4. close'].plot()
plt.title('Daily Close Price for AMD')
plt.show()

# Plot weekly data
data_weekly['4. close'].plot()
plt.title('Weekly Close Price for AMD')
plt.show()

# Plot daily volume
data_daily['5. volume'].plot()
plt.title('Daily Trading Volume for AMD')
plt.show()

# Plot weekly volume
data_weekly['5. volume'].plot()
plt.title('Weekly Trading Volume for AMD')
plt.show()
