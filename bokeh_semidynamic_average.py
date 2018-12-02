import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file


def datetime(x):
    return np.array(x, dtype=np.datetime64)


data = pd.read_csv("car_ad_edited.csv")

aapl = np.array(data['Petrol'])
aapl_dates = np.array(data['Year'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

p2 = figure(x_axis_type="datetime", title="Petrol-Based Car Production / 1960 - 2016 Average")
p2.grid.grid_line_alpha = 0
p2.xaxis.axis_label = 'Date'
p2.yaxis.axis_label = 'Production Rate'
p2.ygrid.band_fill_color = "olive"
p2.ygrid.band_fill_alpha = 0.1

p2.circle(aapl_dates, aapl, size=4, legend='close',
          color='darkgrey', alpha=0.2)

p2.line(aapl_dates, aapl_avg, legend='avg', color='navy')
p2.legend.location = "top_left"
p1.legend.location = "top_left"

show(p2)  # open a browser
