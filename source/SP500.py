# Date: 2023-05-27
# Author: Shiwen An
# Purpose: Write some code for connect Japan Stock Market
# Start of serious data analysis for stock markets 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data for S&P 500
data = yf.download('^GSPC', start='2020-01-01')

# Plot the closing prices
data['Close'].plot(figsize=(10,5))
plt.grid(True)
plt.title('S&P 500 Prices')
plt.ylabel('Price')
plt.show()
