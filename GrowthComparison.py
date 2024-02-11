
import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

# Ticker symbols for SPDR ETF and CNDX ETF

spdr_ticker = ['SPY','S&P 500 ETF']
cndx_l = ['CNDX.L', 'NASDAQ ETF']
#cndx_as = ['VWO' ,'Vanguard emerging ETF']
#cndx_as = ['FNGU' ,'Microsectors FANG 3x leverage']  # Treasure
#cndx_as = ['VOO', 'Vanguard 500 index fund']
#cndx_as = ['VHYL.L','Vanguard  High dividend']
#cndx_as = ['VWRD.L','Vanguard UCITS']
#cndx_as = ['BLK','Black Rock']   #Treasure + laregest divident per share
#cndx_as = ['IVZ','INVESCO Ltd '] # highest % divident
#cndx_as = ['BLKB','Blackbaud Inc ']
# cndx_as = ['BX','BlackStone Inc '] #Treasure
cndx_as = ['BRK-B','Berkshire Hatheway']  #Treasure
#cndx_as = ['APO','Apollo investement']
# cndx_as = ['VGT','Vanguard Growth ETF']
# cndx_as = ['VTI','Vanguard Stock Market index']
# cndx_as = ['VNQ','Vanguard Real Estate']
# cndx_as = ['^N225','Nikkei JPY']
# cndx_as = ['VV','Vanguard large cap et']
#cndx_as = ['SMH','Vaneck semiconductor']
# Fetch historical data for SPDR ETF until September 2021

spdr_data = yf.download(spdr_ticker[0], start = '2016-01-01')
cndx_l_data = yf.download(cndx_l[0], start ='2016-01-01')
cndx_as_data = yf.download(cndx_as[0], start = '2016-01-01')





#create figure and 1x2 subplots
fig, ax = plt.subplots(1,2,figsize=(10, 6))
spdr_data.index
spdr_data.index= pd.to_datetime(spdr_data.index,unit='D').date
cndx_l_data.index= pd.to_datetime(cndx_l_data.index,unit='D').date
cndx_as_data.index = pd.to_datetime(cndx_as_data.index,unit='D').date

ax[1].plot(spdr_data.index, np.log(spdr_data['Close']), label=spdr_ticker[1], color='blue')
ax[1].plot(cndx_l_data.index, np.log(cndx_l_data['Close']), label=cndx_l[1], color='green')
ax[1].plot(cndx_as_data.index, np.log(cndx_as_data['Close']), label=cndx_as[1], color='black')


ax[0].plot(spdr_data.index, spdr_data['Close'], label=spdr_ticker[1], color='blue')
ax[0].plot(cndx_l_data.index, cndx_l_data['Close'], label=cndx_l[1], color='green')
ax[0].plot(cndx_as_data.index, cndx_as_data['Close'], label=cndx_as[1], color='black')

print(cndx_l_data.index[0])
def onclick(event):
    #print(event.xdata)
    date = pd.to_datetime(event.xdata,unit='D').date()
    print(spdr_data['Close'][date])

ax[0].set_xlabel('Date')
ax[0].set_ylabel('ETF Value')
ax[0].set_title('Historical Values')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('growth rate')
ax[1].set_title('Values on natural log scale')
ax[0].legend()
ax[1].legend()

ax[1].grid()
ax[0].set_facecolor('#ffffe4')
ax[1].set_facecolor('#ffffe4')
ax[0].grid()

fig.canvas.mpl_connect('button_press_event',onclick)

plt.show()
