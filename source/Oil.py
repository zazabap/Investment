# Date: 2023-05-23 
# Author: Shiwen An
# Purpose: Write some code for connect Japan Stock Market
# Start of serious data analysis for stock markets 


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download historical data for USO
data = yf.download('USO', start='2020-01-01')

# Plot the closing prices
data['Close'].plot(figsize=(10,5))
plt.grid(True)
plt.title('USO Prices')
plt.ylabel('Price')
plt.show()

