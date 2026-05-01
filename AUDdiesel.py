import pandas as pd
import time
import sys

AUD_diesel = pd.read_csv('data/Avg_DieselPrice_AUD.csv', on_bad_lines="skip")
