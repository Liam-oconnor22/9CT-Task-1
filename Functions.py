from re import search

import pandas as pd
import matplotlib.pyplot as plt
import sys
import time


AUD_diesel = pd.read_csv('Avg_DieselPrice_AUD.csv', on_bad_lines="skip")








def visualisation():
    AUD_diesel.plot(x='Date', y='Cents per litre (NSW)', kind='line', title='Rise in diesel over time')
    plt.show()

def nsw_vs_metro_region():
    plt.plot(AUD_diesel['Date'], AUD_diesel['Cents per litre (NSW)'], label='SYD', marker='o', color='blue')


    plt.plot(AUD_diesel['Date'], AUD_diesel[' Metro Region Average'], label='Metro Average', marker='D', color='red')


    plt.xlabel('Date')
    plt.ylabel('Cents per litre')
    plt.title('NSW versus city average prices of diesel.')
    plt.legend() 
    plt.show()


def filter_data():
    print("Columns are: Date, NSW average, Metro average")
    print("rows are: 1 -> 13.")
    search = input("Please enter a column or row you would like to view.").lower()

    ###- columns

    if search == 'date':
        date_column = AUD_diesel["Date"]
        print(date_column)
    elif search == 'nsw average':
        NSW_column = AUD_diesel['Cents per litre (NSW)']
        print(NSW_column)
    elif search == 'metro average':
        Metro_column = AUD_diesel[' Metro Region Average']
        print(Metro_column)

    ###- rows

    elif search == '1':
        first_row = AUD_diesel.iloc[0]
        print(first_row)
    elif search == '2':
        second_row = AUD_diesel.iloc[1]
        print(second_row)
    elif search == '3':
        third_row = AUD_diesel.iloc[2]
        print(third_row)
    elif search == '4':
        fourth_row = AUD_diesel.iloc[3]
        print(fourth_row)
    elif search == '5':
        fifth_row = AUD_diesel.iloc[4]
        print(fifth_row)
    elif search == '6':
        sixth_row = AUD_diesel.iloc[5]
        print(sixth_row)
    elif search == '7':
        seventh_row = AUD_diesel.iloc[6]
        print(seventh_row)
    elif search == '8':
        eighth_row = AUD_diesel.iloc[7]
        print(eighth_row)
    elif search == '9':
        ninth_row = AUD_diesel.iloc[8]
        print(ninth_row)
    elif search == '10':
        tenth_row = AUD_diesel.iloc[9]
        print(tenth_row)
    elif search == '11':
        eleventh_row = AUD_diesel.iloc[10]
        print(eleventh_row)
    elif search == '12':
        twelfth_row = AUD_diesel.iloc[11]
        print(twelfth_row)
    elif search == '13':
        thirteenth_row = AUD_diesel.iloc[12]
        print(thirteenth_row)

    else:
        print("you suck")

###-------------------------------------------------------------------------------------###

def main():
    print("Loading..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Welcome to the main menu!")
    while True:
        time.sleep(1)
        print("||=-=-=-=-=-= Data Viewer Interface =-=-=-=-=-=||")
        time.sleep(1)
        print("1. View dataset.                               ||")
        time.sleep(0.5)
        print("2. View visualisation.                         ||")
        time.sleep(0.5)
        print("3. Search or filter data.                      ||")
        time.sleep(0.5)
        print("4. Update a data entry.                        ||")
        time.sleep(0.5)
        print("5. Save changes                                ||")
        time.sleep(0.5)
        print("6. Exit.                                       ||")
        print("||=-=-=--=--=---=-=-=--=-=-=-=-=-=-==-=-=-=-=-=||")
        time.sleep(0.5)
        data_viewing = int(input("Select an option 1-6.|"))
        print("_____________________/")

        if data_viewing == 1:
            print(AUD_diesel)
        if data_viewing == 2:
            graphs = input("View graph 1- NSW diesel overtime, or graph 2- NSW diesel versus Mewtro region average? (1/2)   ")
            if graphs == '1':
                visualisation()
            elif graphs == '2':
                nsw_vs_metro_region()
            else:
                while not graphs == '1' and not graphs == '2':
                    time.sleep(1)
                    print("That is not a valid option please try again.")
                    graphs = input("Select a valid option (1/2).   ")
                    if graphs == '1':
                        visualisation()
                    elif graphs == '2':
                        nsw_vs_metro_region()
        if data_viewing == 3:
            time.sleep(1)
            filter_data()
        if data_viewing == 4:
            time.sleep(1)
            print("4")
        if data_viewing == 5:
            time.sleep(1)
            print("5")
        if data_viewing == 6:
            time.sleep(1)
            print("Exiting menu...")
            break





###-------------------------------------------------------------------------------------###