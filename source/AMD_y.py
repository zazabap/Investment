# Date: 2023-05-23 
# Author: Shiwen An
# Purpose: Write some code for connect Japan Stock Market
# Start of serious data analysis for stock markets 


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data as a DataFrame
data = yf.download('AMD', start='2020-01-01')

# Calculate the 30 week moving average
data['30 Week MA'] = data['Close'].rolling(window=30).mean()

# Plot the close price and the moving average
data[['Close', '30 Week MA']].plot(figsize=(10,5))
plt.grid(True)
plt.title('AMD Prices with 30 Week Moving Average')
plt.ylabel('Price')
plt.show()

# Resample to weekly frequency, taking the last price each week
data_weekly = data.resample('W').last()

# Calculate the 30 week moving average
data_weekly['30 Week MA'] = data_weekly['Close'].rolling(window=30).mean()

# Plot the close price and the moving average
data_weekly[['Close', '30 Week MA']].plot(figsize=(10,5))
plt.grid(True)
plt.title('AMD Weekly Prices with 30 Week Moving Average')
plt.ylabel('Price')
plt.show()
