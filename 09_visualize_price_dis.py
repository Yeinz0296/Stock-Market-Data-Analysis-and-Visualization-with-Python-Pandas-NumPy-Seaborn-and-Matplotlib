import matplotlib.pyplot as plt
import numpy as np
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

days = 365
dt = 1/days
sigma = returns.std()['NFLX']
mu = returns.mean()['NFLX']
starting_price = NFLX.head(1)['Adj Close']


def monte_carlo_analysis(starting_price, days, mu, sigma):
    price = np.zeros(days)
    price[0] = starting_price
    shock = np.zeros(days)
    drift = np.zeros(days)
    
    for day in range(1, days):
        shock[day] = np.random.normal(loc = mu * dt, scale = sigma * np.sqrt(dt))
        drift[day] = mu * dt
        price[day] = price[day -1] + (price[day-1] * (drift[day] + shock[day]))

    return price

number_of_run = 1000
simulation = np.zeros(number_of_run)
quantile = np.percentile(simulation, 1)

for run in range (number_of_run):
    simulation[run] = monte_carlo_analysis(starting_price, days, mu, sigma)[days - 1]

plt.hist(simulation, bins = 100)
plt.figtext(0.2, 0.8, s = 'Starting price: $%.2f' % starting_price)
plt.figtext(0.2, 0.7, s = 'Mean final Price: $%.2f' % simulation.mean())
plt.figtext(0.2, 0.6, s = 'Varience (99 percent Confidence): $%.2f' % (starting_price - quantile))
plt.figtext(0.2, 0.5, s = '1 percent quantile: $%.2f' % quantile)

plt.axvline(x= quantile, linewidth =3)

plt.show()
