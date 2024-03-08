# Date: 2023-05-29
# Author: Shiwen An
# Purpose: Write some code for connect Japan Stock Market
# Start of serious data analysis for stock markets 

import yfinance as yf
import matplotlib.pyplot as plt

import pandas as pd
from scipy.stats import linregress


# Download historical data for Nvidia
data = yf.download('NVDA', start='2020-01-01')

# Resample data to weekly time frame
weekly_data = data.resample('W').mean()

# Create a new figure and a 2x2 grid of subplots
fig, axs = plt.subplots(3, 3, figsize=(15, 15))

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
axs[0, 2].plot(weekly_data['Close'])
axs[0, 2].grid(True)
axs[0, 2].set_title('NVIDIA Weekly Prices')
axs[0, 2].set_ylabel('Price ($)')
axs[0, 2].set_xlabel('Date')


amd = yf.download('AMD', start='2020-01-01')

# Plot daily closing prices
axs[1, 0].plot(amd['Close'])
axs[1, 0].grid(True)
axs[1, 0].set_title('AMD Daily Price')
axs[1, 0].set_ylabel('Prices ($)')

sp500 = yf.download('^GSPC', start='2020-01-01')

# Pl S&P500
axs[1, 1].plot(sp500['Close'])
axs[1, 1].grid(True)
axs[1, 1].set_title('S&P 500 Prices')
axs[1, 1].set_ylabel('Price')

amd_returns = amd['Close'].pct_change()[1:]
sp500_returns = sp500['Close'].pct_change()[1:]
slope, intercept, r_value, p_value, std_err = linregress(sp500_returns, amd_returns)

# Plot weekly volume
axs[1, 2].scatter(sp500_returns, amd_returns, alpha=0.5, edgecolors='r')
axs[1, 2].plot(sp500_returns, intercept + slope*sp500_returns, 'b', label=f'y={slope:.2f}x+{intercept:.2f}')
axs[1, 2].set_title('Correlation of Daily Returns: AMD vs S&P 500')
axs[1, 2].set_ylabel('AMD Returns')
axs[1, 2].set_xlabel('S&P 500 Returns')
axs[1, 2].legend()
axs[1, 2].grid(True)

msft = yf.download('MSFT', start='2020-01-01')
msft['MA_20'] = msft['Close'].rolling(window=20).mean()
msft['MA_50'] = msft['Close'].rolling(window=50).mean()
# Plot daily closing prices
axs[2, 0].plot(msft['Close'])
axs[2, 0].grid(True)
axs[2, 0].plot(msft.index, msft['MA_20'], label='20-day Moving Average')
axs[2, 0].plot(msft.index, msft['MA_50'], label='50-day Moving Average')
axs[2, 0].set_title('Microsoft Daily Prices')
axs[2, 0].set_ylabel('Price ($)')

snow = yf.download('SNOW', start='2020-09-18')
# Plot daily volume
axs[2, 1].plot(snow['Close'])
axs[2, 1].grid(True)
axs[2, 1].set_title('SnowFlake Daily Prices')
axs[2, 1].set_ylabel('Price ($)')
# axs[2, 1].set_xlabel('Date')

aapl = yf.download('AAPL', start='2020-01-01')
# Plot weekly closing prices
axs[2, 2].plot(aapl['Close'])
axs[2, 2].grid(True)
axs[2, 2].set_title('Apple Daily Prices')
axs[2, 2].set_ylabel('Price ($)')
axs[2, 2].set_xlabel('Date')

# Improve layout
fig.tight_layout()
plt.show()

# Get current data
data_current = yf.Ticker('NVDA')

# Get the recent P/E ratio
pe_ratio = data_current.info['trailingPE']

print(f"The current P/E ratio for NVDA is {pe_ratio}")