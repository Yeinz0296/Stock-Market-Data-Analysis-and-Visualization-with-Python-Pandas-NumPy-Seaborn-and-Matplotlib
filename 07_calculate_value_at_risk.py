import seaborn
import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import datetime

stock_list = ['FB', 'AMZN', 'NFLX', 'GOOG'] #nama stock

today = datetime.now()

start = datetime(today.year - 1, today.month, today.day) #tarikh kita nak
end = today

for stock in stock_list:
    globals()[stock] = DataReader(stock, 'yahoo', start, end)

adjusted_closing_dataframe = DataReader(stock_list, 'yahoo', start, end)['Adj Close']

stock_return = adjusted_closing_dataframe.pct_change()
returns = stock_return.dropna() 

GOOG['Daily Return'] = GOOG['Adj Close'].pct_change()
seaborn.distplot(GOOG['Daily Return'].dropna(), bins = 100)
#plt.show()

expected = returns['NFLX'].quantile(0.5)
print(expected)
