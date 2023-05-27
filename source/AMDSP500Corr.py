
# Date: 2023-05-27
# Author: Shiwen An
# Purpose: Add Correlation study between AMD and SP500

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Download historical data
amd = yf.download('AMD', start='2020-01-01')['Close']
sp500 = yf.download('^GSPC', start='2020-01-01')['Close']

# Calculate daily returns
amd_returns = amd.pct_change()[1:]
sp500_returns = sp500.pct_change()[1:]

# Fit a linear regression to the return values
slope, intercept, r_value, p_value, std_err = linregress(sp500_returns, amd_returns)

# Create a scatter plot of the returns and plot the regression line
plt.figure(figsize=(10, 6))
plt.scatter(sp500_returns, amd_returns, alpha=0.5, edgecolors='r')
plt.plot(sp500_returns, intercept + slope*sp500_returns, 'b', label=f'y={slope:.2f}x+{intercept:.2f}')
plt.xlabel('S&P 500 Returns')
plt.ylabel('AMD Returns')
plt.title('Correlation of Daily Returns: AMD vs S&P 500')
plt.legend()
plt.grid(True)
plt.show()
