
import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt
import pandas as pd

# Ticker symbols for SPDR ETF and CNDX ETF

spdr_ticker = ['SPY','S&P 500 ETF']
cndx_l = ['CNDX.L', 'NASDAQ ETF']
cndx_as = ['VWO' ,'Vanguard emerging ETF']
#cndx_as = ['FNGU' ,'Microsectors FANG 3x leverage']  # Treasure
#cndx_as = ['VOO', 'Vanguard 500 index fund']
#cndx_as = ['VHYL.L','Vanguard  High dividend']
#cndx_as = ['VWRD.L','Vanguard UCITS']
#cndx_as = ['BLK','Black Rock']   #Treasure + laregest divident per share
#cndx_as = ['IVZ','INVESCO Ltd '] # highest % divident
#cndx_as = ['BLKB','Blackbaud Inc ']
#cndx_as = ['BX','BlackStone Inc '] #Treasure
#cndx_as = ['BRK-B','Berkshire Hatheway']  #Treasure
# Fetch historical data for SPDR ETF until September 2021

spdr_data = yf.download(spdr_ticker[0], start = '2016-01-01')
cndx_l_data = yf.download(cndx_l[0], start ='2016-01-01')
cndx_as_data = yf.download(cndx_as[0], start = '2016-01-01')

# calculate % change in price on daily basis
spdr_pct =pd.Series(spdr_data['Close']).pct_change()
cndx_l_pct = pd.Series(cndx_l_data['Close'].pct_change())
print(cndx_l_data.Volume)

# calculate % change in volume on daily basis
spdr_vol_pct = pd.Series(spdr_data['Volume']).pct_change()
cndx_l_vol_pct = pd.Series(cndx_l_data['Volume']).pct_change()

#calculate change in price on daily basis
spdr_diff = pd.Series(spdr_data['Close']).diff()
cndx_l_diff = pd.Series(cndx_l_data['Close']).diff()

#create figure and 2x2 subplots
fig, ax = plt.subplots(2,2,figsize=(10, 6))

ax[0,1].plot(spdr_data.index, spdr_pct, label= 'SPY price % change', color= 'blue', linestyle = 'solid')
ax[0,1].plot(cndx_l_pct.index, cndx_l_pct, label= 'CNDX L price % change', color = 'green', linestyle = 'solid')
#ax[0,1].plot(cndx_as_pct.index, cndx_as_pct, label= 'CNDX AS daily % change', color = 'black', linestyle = 'solid')

ax[0,0].plot(spdr_data.index, spdr_data['Close'], label=spdr_ticker[1], color='blue')
ax[0,0].plot(cndx_l_data.index, cndx_l_data['Close'], label=cndx_l[1], color='green')
ax[0,0].plot(cndx_as_data.index, cndx_as_data['Close'], label=cndx_as[1], color='black')


import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt
import pandas as pd

# Ticker symbols for SPDR ETF and CNDX ETF

spdr_ticker = ['SPY','S&P 500 ETF']
cndx_l = ['CNDX.L', 'NASDAQ ETF']
cndx_as = ['VWO' ,'Vanguard emerging ETF']
#cndx_as = ['FNGU' ,'Microsectors FANG 3x leverage']  # Treasure
#cndx_as = ['VOO', 'Vanguard 500 index fund']
#cndx_as = ['VHYL.L','Vanguard  High dividend']
#cndx_as = ['VWRD.L','Vanguard UCITS']
#cndx_as = ['BLK','Black Rock']   #Treasure + laregest divident per share
#cndx_as = ['IVZ','INVESCO Ltd '] # highest % divident
#cndx_as = ['BLKB','Blackbaud Inc ']
#cndx_as = ['BX','BlackStone Inc '] #Treasure
#cndx_as = ['BRK-B','Berkshire Hatheway']  #Treasure
# Fetch historical data for SPDR ETF until September 2021

spdr_data = yf.download(spdr_ticker[0], start = '2016-01-01')
cndx_l_data = yf.download(cndx_l[0], start ='2016-01-01')
cndx_as_data = yf.download(cndx_as[0], start = '2016-01-01')

# calculate % change in price on daily basis
spdr_pct =pd.Series(spdr_data['Close']).pct_change()
cndx_l_pct = pd.Series(cndx_l_data['Close'].pct_change())
print(cndx_l_data.Volume)

# calculate % change in volume on daily basis
spdr_vol_pct = pd.Series(spdr_data['Volume']).pct_change()
cndx_l_vol_pct = pd.Series(cndx_l_data['Volume']).pct_change()

#calculate change in price on daily basis
spdr_diff = pd.Series(spdr_data['Close']).diff()
cndx_l_diff = pd.Series(cndx_l_data['Close']).diff()

#create figure and 2x2 subplots
fig, ax = plt.subplots(2,2,figsize=(10, 6))

ax[0,1].plot(spdr_data.index, spdr_pct, label= 'SPY price % change', color= 'blue', linestyle = 'solid')
ax[0,1].plot(cndx_l_pct.index, cndx_l_pct, label= 'CNDX L price % change', color = 'green', linestyle = 'solid')
#ax[0,1].plot(cndx_as_pct.index, cndx_as_pct, label= 'CNDX AS daily % change', color = 'black', linestyle = 'solid')

ax[0,0].plot(spdr_data.index, spdr_data['Close'], label=spdr_ticker[1], color='blue')
ax[0,0].plot(cndx_l_data.index, cndx_l_data['Close'], label=cndx_l[1], color='green')
ax[0,0].plot(cndx_as_data.index, cndx_as_data['Close'], label=cndx_as[1], color='black')


ax[1,0].plot(spdr_data.index, spdr_vol_pct, label='SPDR ETF (SPY) Volume % change', color='blue')
ax[1,0].plot(cndx_l_data.index, cndx_l_vol_pct,label='CNDX L ETF Volume % change', color='green')


ax[1,1].plot(spdr_data.index, spdr_diff, label='SPDR ETF (SPY) price change', color='blue')
ax[1,1].plot(cndx_l_data.index, cndx_l_diff,label='CNDX L ETF price change', color='green')


ax[0,0].set_xlabel('Date')
ax[0,0].set_ylabel('ETF Value')
ax[0,0].set_title('Historical Values of SPDR ETF (SPY) and CNDX ETF')
ax[0,1].set_title('% change from day to day closing, Blue SPY and green CNDX L')
ax[0,0].legend()
ax[0,1].legend()
ax[1,0].legend()
ax[1,1].legend()
ax[1,1].grid()
ax[1,0].grid()
ax[0,1].grid()
ax[0,0].set_facecolor('#ffffe4')
ax[0,0].grid()

plt.show()
import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt
import pandas as pd

# Ticker symbols for SPDR ETF and CNDX ETF

spdr_ticker = ['SPY','S&P 500 ETF']
cndx_l = ['CNDX.L', 'NASDAQ ETF']
cndx_as = ['VWO' ,'Vanguard emerging ETF']
#cndx_as = ['FNGU' ,'Microsectors FANG 3x leverage']  # Treasure
#cndx_as = ['VOO', 'Vanguard 500 index fund']
#cndx_as = ['VHYL.L','Vanguard  High dividend']
#cndx_as = ['VWRD.L','Vanguard UCITS']
#cndx_as = ['BLK','Black Rock']   #Treasure + laregest divident per share
#cndx_as = ['IVZ','INVESCO Ltd '] # highest % divident
#cndx_as = ['BLKB','Blackbaud Inc ']
#cndx_as = ['BX','BlackStone Inc '] #Treasure
#cndx_as = ['BRK-B','Berkshire Hatheway']  #Treasure
# Fetch historical data for SPDR ETF until September 2021

spdr_data = yf.download(spdr_ticker[0], start = '2016-01-01')
cndx_l_data = yf.download(cndx_l[0], start ='2016-01-01')
cndx_as_data = yf.download(cndx_as[0], start = '2016-01-01')

# calculate % change in price on daily basis
spdr_pct =pd.Series(spdr_data['Close']).pct_change()
cndx_l_pct = pd.Series(cndx_l_data['Close'].pct_change())
print(cndx_l_data.Volume)

# calculate % change in volume on daily basis
spdr_vol_pct = pd.Series(spdr_data['Volume']).pct_change()
cndx_l_vol_pct = pd.Series(cndx_l_data['Volume']).pct_change()

#calculate change in price on daily basis
spdr_diff = pd.Series(spdr_data['Close']).diff()
cndx_l_diff = pd.Series(cndx_l_data['Close']).diff()

#create figure and 2x2 subplots
fig, ax = plt.subplots(2,2,figsize=(10, 6))

ax[0,1].plot(spdr_data.index, spdr_pct, label= 'SPY price % change', color= 'blue', linestyle = 'solid')
ax[0,1].plot(cndx_l_pct.index, cndx_l_pct, label= 'CNDX L price % change', color = 'green', linestyle = 'solid')
#ax[0,1].plot(cndx_as_pct.index, cndx_as_pct, label= 'CNDX AS daily % change', color = 'black', linestyle = 'solid')

ax[0,0].plot(spdr_data.index, spdr_data['Close'], label=spdr_ticker[1], color='blue')
ax[0,0].plot(cndx_l_data.index, cndx_l_data['Close'], label=cndx_l[1], color='green')
ax[0,0].plot(cndx_as_data.index, cndx_as_data['Close'], label=cndx_as[1], color='black')


ax[1,0].plot(spdr_data.index, spdr_vol_pct, label='SPDR ETF (SPY) Volume % change', color='blue')
ax[1,0].plot(cndx_l_data.index, cndx_l_vol_pct,label='CNDX L ETF Volume % change', color='green')


ax[1,1].plot(spdr_data.index, spdr_diff, label='SPDR ETF (SPY) price change', color='blue')
ax[1,1].plot(cndx_l_data.index, cndx_l_diff,label='CNDX L ETF price change', color='green')


ax[0,0].set_xlabel('Date')
ax[0,0].set_ylabel('ETF Value')
ax[0,0].set_title('Historical Values of SPDR ETF (SPY) and CNDX ETF')
ax[0,1].set_title('% change from day to day closing, Blue SPY and green CNDX L')
ax[0,0].legend()
ax[0,1].legend()
ax[1,0].legend()
ax[1,1].legend()
ax[1,1].grid()
ax[1,0].grid()
ax[0,1].grid()
ax[0,0].set_facecolor('#ffffe4')
ax[0,0].grid()

plt.show()
import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt
import pandas as pd

# Ticker symbols for SPDR ETF and CNDX ETF

spdr_ticker = ['SPY','S&P 500 ETF']
cndx_l = ['CNDX.L', 'NASDAQ ETF']
cndx_as = ['VWO' ,'Vanguard emerging ETF']
#cndx_as = ['FNGU' ,'Microsectors FANG 3x leverage']  # Treasure
#cndx_as = ['VOO', 'Vanguard 500 index fund']
#cndx_as = ['VHYL.L','Vanguard  High dividend']
#cndx_as = ['VWRD.L','Vanguard UCITS']
#cndx_as = ['BLK','Black Rock']   #Treasure + laregest divident per share
#cndx_as = ['IVZ','INVESCO Ltd '] # highest % divident
#cndx_as = ['BLKB','Blackbaud Inc ']
#cndx_as = ['BX','BlackStone Inc '] #Treasure
#cndx_as = ['BRK-B','Berkshire Hatheway']  #Treasure
# Fetch historical data for SPDR ETF until September 2021

spdr_data = yf.download(spdr_ticker[0], start = '2016-01-01')
cndx_l_data = yf.download(cndx_l[0], start ='2016-01-01')
cndx_as_data = yf.download(cndx_as[0], start = '2016-01-01')

# calculate % change in price on daily basis
spdr_pct =pd.Series(spdr_data['Close']).pct_change()
cndx_l_pct = pd.Series(cndx_l_data['Close'].pct_change())
print(cndx_l_data.Volume)

# calculate % change in volume on daily basis
spdr_vol_pct = pd.Series(spdr_data['Volume']).pct_change()
cndx_l_vol_pct = pd.Series(cndx_l_data['Volume']).pct_change()

#calculate change in price on daily basis
spdr_diff = pd.Series(spdr_data['Close']).diff()
cndx_l_diff = pd.Series(cndx_l_data['Close']).diff()

#create figure and 2x2 subplots
fig, ax = plt.subplots(2,2,figsize=(10, 6))

ax[0,1].plot(spdr_data.index, spdr_pct, label= 'SPY price % change', color= 'blue', linestyle = 'solid')
ax[0,1].plot(cndx_l_pct.index, cndx_l_pct, label= 'CNDX L price % change', color = 'green', linestyle = 'solid')
#ax[0,1].plot(cndx_as_pct.index, cndx_as_pct, label= 'CNDX AS daily % change', color = 'black', linestyle = 'solid')

ax[0,0].plot(spdr_data.index, spdr_data['Close'], label=spdr_ticker[1], color='blue')
ax[0,0].plot(cndx_l_data.index, cndx_l_data['Close'], label=cndx_l[1], color='green')
ax[0,0].plot(cndx_as_data.index, cndx_as_data['Close'], label=cndx_as[1], color='black')


ax[1,0].plot(spdr_data.index, spdr_vol_pct, label='SPDR ETF (SPY) Volume % change', color='blue')
ax[1,0].plot(cndx_l_data.index, cndx_l_vol_pct,label='CNDX L ETF Volume % change', color='green')


ax[1,1].plot(spdr_data.index, spdr_diff, label='SPDR ETF (SPY) price change', color='blue')
ax[1,1].plot(cndx_l_data.index, cndx_l_diff,label='CNDX L ETF price change', color='green')


ax[0,0].set_xlabel('Date')
ax[0,0].set_ylabel('ETF Value')
ax[0,0].set_title('Historical Values of SPDR ETF (SPY) and CNDX ETF')
ax[0,1].set_title('% change from day to day closing, Blue SPY and green CNDX L')
ax[0,0].legend()
ax[0,1].legend()
ax[1,0].legend()
ax[1,1].legend()
ax[1,1].grid()
ax[1,0].grid()
ax[0,1].grid()
ax[0,0].set_facecolor('#ffffe4')
ax[0,0].grid()

plt.show()
ax[1,0].plot(spdr_data.index, spdr_vol_pct, label='SPDR ETF (SPY) Volume % change', color='blue')
ax[1,0].plot(cndx_l_data.index, cndx_l_vol_pct,label='CNDX L ETF Volume % change', color='green')


ax[1,1].plot(spdr_data.index, spdr_diff, label='SPDR ETF (SPY) price change', color='blue')
ax[1,1].plot(cndx_l_data.index, cndx_l_diff,label='CNDX L ETF price change', color='green')


ax[0,0].set_xlabel('Date')
ax[0,0].set_ylabel('ETF Value')
ax[0,0].set_title('Historical Values of SPDR ETF (SPY) and CNDX ETF')
ax[0,1].set_title('% change from day to day closing, Blue SPY and green CNDX L')
ax[0,0].legend()
ax[0,1].legend()
ax[1,0].legend()
ax[1,1].legend()
ax[1,1].grid()
ax[1,0].grid()
ax[0,1].grid()
ax[0,0].set_facecolor('#ffffe4')
ax[0,0].grid()

plt.show()
