import pandas as pd
import matplotlib.pyplot as plt
import sys


AUD_diesel = pd.read_csv('Avg_DieselPrice_AUD.csv', on_bad_lines="skip")

def visualisation():
    AUD_diesel.plot(x='Date', y='Cents per litre (NSW)', kind='line', title='Rise in diesel over time')
    plt.show()

def aus_vs_metro_region():
    plt.plot(AUD_diesel['Date'], AUD_diesel['Cents per litre (NSW)'], label='SYD', marker='o', color='blue')


    plt.plot(AUD_diesel['Date'], AUD_diesel[' Metro Region Average'], label='Metro Average', marker='D', color='red')


    plt.xlabel('Date')
    plt.ylabel('Cents per litre')
    plt.title('NSW versus city average prices of diesel.')
    plt.legend() 
    plt.show()


aus_vs_metro_region()