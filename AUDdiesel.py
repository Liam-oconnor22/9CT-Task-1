import pandas as pd
import time
import sys

AUD_diesel = pd.read_csv('Avg_DieselPrice_AUD.csv', on_bad_lines="skip")
print(AUD_diesel)
