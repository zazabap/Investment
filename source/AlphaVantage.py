import requests
api_key = 'E2S7MZC034PYLV42'
symbol = 'AAPL'
# symbol = '5838.T'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}'
response = requests.get(url)
data = response.json()
import pandas as pd

# Print the opening price for the most recent day of trading
# print(data)
print(data['Time Series (Daily)']['2023-04-06']['1. open'])
print(data['Time Series (Daily)']['2023-04-10']['1. open'])
print(data['Time Series (Daily)']['2023-04-11']['1. open'])
print(data['Time Series (Daily)']['2023-04-12']['1. open'])
print(data['Time Series (Daily)']['2023-04-13']['1. open'])
print(data['Time Series (Daily)']['2023-04-14']['1. open'])
symbol = 'AAPL'
endpoint = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&outputsize=full&apikey={api_key}'
response = requests.get(endpoint)
data = response.json()
# Convert the data to a Pandas dataframe
df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
# Filter the data for the desired time period (April to June 2022)
# Add a bit more historical data
print(2022)
print(data['Time Series (Daily)']['2022-04-13']['1. open'])
print(data['Time Series (Daily)']['2022-06-02']['1. open'])
print(data['Time Series (Daily)']['2022-06-10']['1. open'])
print(data['Time Series (Daily)']['2022-06-13']['1. open'])
# Print the filtered data
print(df)
# print("Apple Stock April and June Invest: ")

# print(data['Time Series (Daily)']['2023-04-13']['1. open'])

# import pandas_datareader as pdr

# # Define the stock symbol and start/end dates
# symbol = '7203.T'
# start_date = '2022-01-01'
# end_date = '2022-12-31'

# # Use pandas-datareader to retrieve the data from Yahoo Finance
# df = pdr.DataReader(symbol, 'yahoojp', start_date, end_date)
# print(df)