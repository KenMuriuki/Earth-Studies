# importing the neccesary packages
from matplotlib.axes._axes import _log as matplotlib_axes_logger
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import earthpy as et

# handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# dealing with errors thrown by one of the plots
matplotlib_axes_logger.setLevel("ERROR")
import warnings
warnings.filterwarnings('ignore')

# adjusting fontsixe with seaborn
sns.set(font_scale=1.5, style='whitegrid')

# reading the precipitation dataset
precip_data = pd.read_csv(
    "Earth-Studies\precip-daily-2003-2013.csv",
    parse_dates=['DATE'],
    na_values=999.99,
    index_col='DATE'
)

# subset time series data by time case year 2005 & remove missing values
data_2005 = precip_data['2005'].dropna()

# hourly precipitation
from matplotlib.dates import DateFormatter
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(data_2005.index.values, data_2005['HPCP'])
ax.xaxis.set_major_formatter(DateFormatter("%m"))
plt.title("Hourly precipitation in 2005")
plt.xlabel("Month")
plt.show()

# draw plot of daily sums precipitation
data_D = data_2005.resample("D").sum()

fig, ax = plt.subplots(figsize=(8,6))
plt.scatter(x=data_D.index.values,
        y=data_D['HPCP'])
plt.title("Scatter graph of daily preciptation")
plt.show()

# draw plot of monthly average precipitation
data_m = data_2005.resample("M").mean()

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(data_m.index.values, data_m['HPCP'])
ax.set_title("Monthly Average Precipitation for year 2005")
plt.show()





