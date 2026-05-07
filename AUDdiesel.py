import pandas as pd
import matplotlib.pyplot as plt
import time
import sys

AUD_diesel = pd.read_csv('Avg_DieselPrice_AUD.csv', on_bad_lines="skip")

### Line Graph - - - - - - - - - - - - - - - -

AUD_diesel.plot(x='Date', y='Cents per litre (NSW)', kind='line', title='Rise in diesel over time')

###- - - - - - - - - - - - - - - - - - - - - -

### Line Graph (against AUD average) - - - - - - - - - - - - - - - -

AUD_diesel.plot(x='Date', y='Cents per litre (NSW)', secondary_y= True, y= 'Metro region average', kind='line', title='Rise in diesel over time')

plt.show()

###- - - - - - - - - - - - - - - - - - - - - -
