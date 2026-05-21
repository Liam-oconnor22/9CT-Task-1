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
    print("rows are: 1. Note that each row represents the month of when the price was recorded, being from row 1,may 2025 to row 13,may 2026 (or later depending on updated data).")
    search = input("View a row or column? (row/column)   ").lower()

    ###- columns
    if search == "column":
        column_q = input("Please select a column.")
        if column_q == 'date':
            date_column = AUD_diesel["Date"]
            print(date_column)
        elif column_q == 'nsw average':
            NSW_column = AUD_diesel['Cents per litre (NSW)']
            print(NSW_column)
        elif column_q == 'metro average':
            Metro_column = AUD_diesel[' Metro Region Average']
            print(Metro_column)

    ###- rows

    if search == "row":
        row_q= int(input("Please enter a row number (1+).   "))
        try:
            row_index = row_q - 1  
            print(AUD_diesel.iloc[row_index])
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid row number.")



def upd_data_entry():

    NSW_column = AUD_diesel['Cents per litre (NSW)']
    Metro_column = AUD_diesel[' Metro Region Average']

    row_idx = int(input("Select the row index you would like to update (0-12, 13+ to add new rows.)   "))
    col_name = input("Please enter the column name you would like to update (Date, NSW_column, Metro_column. Entering anything else will add a new column listed under it.)   ")

    new_val = input(f"Enter the new value in place of the {col_name} column and row {row_idx}.")

    AUD_diesel.at[row_idx, col_name] = new_val
    print(AUD_diesel)

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
        print("5. Save changes to file.                               ||")
        time.sleep(0.5)
        print("6. Exit.                                       ||")
        print("||=-=-=--=--=---=-=-=--=-=-=-=-=-=-==-=-=-=-=-=||")
        time.sleep(0.5)
        data_viewing = int(input("Select an option 1-6. |   "))
        print("|___|___|___|___|___|_/")

        if data_viewing == 1:
            print(AUD_diesel)
        if data_viewing == 2:
            graphs = input("View graph 1- NSW diesel overtime, or graph 2- NSW diesel versus Metro region average? (1/2)   ")
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
            upd_data_entry()
        if data_viewing == 5:
            time.sleep(1)
            verify = input("Are you sure you would like to save your changes? (yes/no)   ").lower()
            if verify == 'yes':
                print("If a column was deleted, make sure to delete the commas in the dataset!")
                AUD_diesel.to_csv("AVG_DieselPrice_AUD.csv", index=False)
                time.sleep(1)
                print("✅ Entry updated and saved to AVG_DieselPrice_AUD.csv")
            else:
                time.sleep(1)
                print("Changes were not saved. returning to main menu...")
        if data_viewing == 6:
            time.sleep(1)
            print("Exiting menu...")
            time.sleep(1)
            print("            ...")
            break





###-------------------------------------------------------------------------------------###