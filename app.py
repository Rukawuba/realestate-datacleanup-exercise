import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

ds = pd.read_csv('assets/real_estate.csv', sep=';')

Am = ds[ds['level5'] == 'Arroyomolinos (Madrid)']
Am_mean = Am['level5'].mean()


print(f"The mean price in Arroyomolinos (Madrid) is: {Am_mean}")



