#small data analysis

import numpy as np
import pandas as pd
import os

workspace_path = r"C:\Users\kaefer\Desktop\Schulemappe\Master\MasterEBusiness\E Business Seminar\NAB-master"
os.chdir(workspace_path)

path = "data//artificialNoAnomaly//art_daily_small_noise.csv"
df = pd.read_csv(path)

df
variance = np.var(df["value"])
std_dev = np.std(df["value"])
snr = np.mean(df["value"]) / std_dev
autocorr = df["value"].autocorr(lag=1)

print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
print(f"SNR: {snr}")
print(f"Autocorrelation (lag=1): {autocorr}")
mean = np.mean(df["value"])
mean








