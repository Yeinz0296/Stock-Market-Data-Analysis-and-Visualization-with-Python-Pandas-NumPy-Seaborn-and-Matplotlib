import pandas
from pandas_datareader import DataReader
from datetime import datetime

stock_list = ['FB', 'AMZN', 'NFLX', 'GOOG'] #nama stock

today = datetime.now()

start = datetime(today.year - 1, today.month, today.day) #tarikh kita nak
end = today

for stock in stock_list:
    globals()[stock] = DataReader(stock, 'yahoo', start, end) #mana nk ambik

print(NFLX.head(1)['Adj Close'])
#print(FB.describe())
#FB.info()





