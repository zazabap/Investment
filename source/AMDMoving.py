# Date: 2023-05-29
# Author: Shiwen An
# Purpose: Write some code for connect Japan Stock Market
# Start of serious data analysis for stock markets 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Download historical data for AMD
end_date = datetime.now().date()
start_date = end_date - timedelta(days=180)  # Restrict to 180 days of data
data = yf.download('AMD', start=start_date, end=end_date)

# Calculate the 20-day and 50-day moving averages
data['MA_20'] = data['Close'].rolling(window=20).mean()
data['MA_50'] = data['Close'].rolling(window=50).mean()

# Plot the closing prices, volume, and the moving averages
fig, ax1 = plt.subplots(figsize=(10, 6))
ax2 = ax1.twinx()  # Create a secondary y-axis for volume

# Plot closing prices and moving averages
ax1.plot(data.index, data['Close'], label='Closing Prices')
ax1.plot(data.index, data['MA_20'], label='20-day Moving Average')
ax1.plot(data.index, data['MA_50'], label='50-day Moving Average')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price ($)')
ax1.set_title('AMD Stock: Closing Prices and Moving Averages (180 Days)')

# Plot volume as histogram
ax2.bar(data.index, data['Volume'], color='gray', alpha=0.6, label='Volume')
ax2.set_ylabel('Volume')

# Adjust y-axis scales for better visualization
ax1.autoscale()
ax2.autoscale()

# Display legends and gridlines
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.grid(True)

end_date = datetime.now().date()
start_date = end_date - timedelta(days=14)  # Restrict to last 7 trading days
data = yf.download('AMD', start=start_date, end=end_date)

# Calculate the number of up days and down days
up_days = sum(data['Close'].diff() > 0)
down_days = sum(data['Close'].diff() < 0)

# Print the result
print("Last 14 Trading Days:")
print(f"Up Days: {up_days}")
print(f"Down Days: {down_days}")

# Calculate the volume increment and define a threshold
volume_threshold = 2.0  # Define a threshold of 2 times the average volume increment
data['VolumeIncrement'] = data['Volume'].diff()
average_volume_increment = data['VolumeIncrement'].mean()
large_volume_increment = data['VolumeIncrement'] > (volume_threshold * average_volume_increment)

# Print the dates with large trading volume increments
large_volume_dates = data[large_volume_increment].index.strftime('%Y-%m-%d').tolist()
print("Dates with Large Volume Increments:")
print(large_volume_dates)

plt.show()

