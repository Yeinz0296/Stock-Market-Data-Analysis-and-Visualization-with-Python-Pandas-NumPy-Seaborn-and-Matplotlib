import seaborn
import matplotlib.pyplot as plt
import numpy as np
from pandas_datareader import DataReader
from datetime import datetime

stock_list = ['FB', 'AMZN', 'NFLX', 'GOOG'] #nama stock

today = datetime.now()

start = datetime(today.year - 1, today.month, today.day) #tarikh kita nak
end = today

adjusted_closing_dataframe = DataReader(stock_list, 'yahoo', start, end)['Adj Close']

stock_return = adjusted_closing_dataframe.pct_change()
circle_area = np.pi *15
returns = stock_return.dropna() 

plt.scatter(x = returns.mean(), y = returns.std(), s = circle_area)
plt.xlabel('Expected Return')
plt.ylabel('Risk')

for label, x, y in zip (returns.columns, returns.mean(), returns.std()):
    plt.annotate(label, xy = (x, y), xytext = (50, 50), textcoords = 'offset points', ha = 'right', va = 'bottom', arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3, rad = -0.3'))

plt.show()
