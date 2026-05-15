from turtle import update

import pandas as pd
import matplotlib.pyplot as plt
import time
import sys


###_ _ _ _ _ _ _ _ _ Functions _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

from Data_module import (
                        visualisation,
                        nsw_vs_metro_region,
                        main,
                        filter_data,
                        upd_data_entry
                        )

###_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

###- read in csv dataframe

AUD_diesel = pd.read_csv('Avg_DieselPrice_AUD.csv', on_bad_lines="skip")

###- user interface loop

if __name__ == "__main__":
    main()