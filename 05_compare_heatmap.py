import seaborn
import matplotlib.pyplot as plt
from pandas_datareader import DataReader
from datetime import datetime

stock_list = ['FB', 'AMZN', 'NFLX', 'GOOG'] #nama stock

today = datetime.now()

start = datetime(today.year - 1, today.month, today.day) #tarikh kita nak
end = today

adjusted_closing_dataframe = DataReader(stock_list, 'yahoo', start, end)['Adj Close']

stock_return = adjusted_closing_dataframe.pct_change()
correlation = stock_return.corr()

# return_figure = seaborn.PairGrid(data = adjusted_closing_dataframe)

# return_figure.map_upper(plt.scatter)
# return_figure.map_diag(plt.hist, bins = 30)
# return_figure.map_lower(seaborn.kdeplot)

print(correlation)
seaborn.heatmap(data = correlation, fmt ='6g')

plt.show()
