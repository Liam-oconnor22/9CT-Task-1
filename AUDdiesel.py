import pandas as pd
import matplotlib.pyplot as plt
import time
import sys


###_ _ _ _ _ _ _ _ _ Functions _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

from Functions import (
                        visualisation,
                        nsw_vs_metro_region,
                        main,
                        filter_data
                        )

###_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

AUD_diesel = pd.read_csv('Avg_DieselPrice_AUD.csv', on_bad_lines="skip")


if __name__ == "__main__":
    main()