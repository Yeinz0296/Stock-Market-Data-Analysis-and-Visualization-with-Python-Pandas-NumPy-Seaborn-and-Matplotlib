import seaborn
import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import datetime

stock_list = ['FB', 'AMZN', 'NFLX', 'GOOG'] #nama stock

today = datetime.now()

start = datetime(today.year - 1, today.month, today.day) #tarikh kita nak
end = today

adjusted_closing_dataframe = DataReader(stock_list, 'yahoo', start, end)['Adj Close']

#print(adjusted_closing_dataframe)
#print(adjusted_closing_dataframe.head())
stock_return = adjusted_closing_dataframe.pct_change()

seaborn.jointplot('GOOG', 'FB', data = stock_return, color= 'orange')
seaborn.pairplot(data = stock_return.dropna())

plt.show()