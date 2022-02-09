from yahoo_fin.stock_info import *

print(get_live_price("FB"))

print(tickers_sp500())

stock = input("Please enter a sticker symbol")

if stock in tickers_sp500():
   print("The stock is in the S&P 500")
else:
    print("the stock isnt int= the S&P 500")

from pandas import *
from alpha_vantage.timeseries import TimeSeries

from time import 

api_key = "I20G5RKDMWV28VZR"

ts = TimeSeries(key=api_key, output_format="pandas")
data, meta_data = ts.get_intraday(symbol='AAPL', interval= = '1min', ouputsize = "full")
print(data)