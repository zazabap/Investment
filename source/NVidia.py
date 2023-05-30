# Date: 2023-05-28
# Author: Shiwen An
# Purpose: Write some code for connect Japan Stock Market
# Start of serious data analysis for stock markets 
import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data for Nvidia
data = yf.download('NVDA', start='2020-01-01')

# Resample data to weekly time frame
weekly_data = data.resample('W').mean()

# Create a new figure and a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Plot daily closing prices
axs[0, 0].plot(data['Close'])
axs[0, 0].grid(True)
axs[0, 0].set_title('NVIDIA Daily Prices')
axs[0, 0].set_ylabel('Price ($)')

# Plot daily volume
axs[0, 1].plot(data['Volume'])
axs[0, 1].grid(True)
axs[0, 1].set_title('NVIDIA Daily Volume')
axs[0, 1].set_ylabel('Volume')

# Plot weekly closing prices
axs[1, 0].plot(weekly_data['Close'])
axs[1, 0].grid(True)
axs[1, 0].set_title('NVIDIA Weekly Prices')
axs[1, 0].set_ylabel('Price ($)')
axs[1, 0].set_xlabel('Date')

# Plot weekly volume
axs[1, 1].plot(weekly_data['Volume'])
axs[1, 1].grid(True)
axs[1, 1].set_title('NVIDIA Weekly Volume')
axs[1, 1].set_ylabel('Volume')
axs[1, 1].set_xlabel('Date')

# Improve layout
fig.tight_layout()
plt.show()

# Get current data
data_current = yf.Ticker('NVDA')

# Get the recent P/E ratio
pe_ratio = data_current.info['trailingPE']

print(f"The current P/E ratio for NVDA is {pe_ratio}")
