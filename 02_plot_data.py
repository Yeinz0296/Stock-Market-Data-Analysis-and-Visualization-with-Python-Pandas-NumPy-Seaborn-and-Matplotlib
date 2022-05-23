import pandas
import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import datetime

stock_list = ['FB', 'AMZN', 'NFLX', 'GOOG'] #nama stock
moving_average_intervals = [5, 20, 50]

today = datetime.now()

start = datetime(today.year - 1, today.month, today.day) #tarikh kita nak
end = today

for stock in stock_list:
    globals()[stock] = DataReader(stock, 'yahoo', start, end) #mana nk ambik

# GOOG['Adj Close'].plot(legend = True, figsize = (14, 6))
# GOOG['Open'].plot(legend = True)

# plt.show()

for moving_average in moving_average_intervals:
    column_name = 'Moving_average for %s days' %(str(moving_average))
    GOOG[column_name] = GOOG['Adj Close'].rolling(moving_average).mean()

GOOG[['Adj Close', 'Moving_average for 5 days', 'Moving_average for 20 days', 'Moving_average for 50 days']].plot()

plt.show()