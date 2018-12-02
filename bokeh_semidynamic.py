import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file


def datetime(x):
    return np.array(x, dtype=np.datetime64)


data = pd.read_csv("test.csv")

p1 = figure(x_axis_type="datetime", title="Production Rate of Petrol/Diesel/Gas Based Cars")
p1.grid.grid_line_alpha = 0.3
p1.xaxis.axis_label = 'Date'
p1.yaxis.axis_label = 'Production Rate'
#p1.xgrid.band_fill_color = "#F0FDFF"
p1.ygrid.band_fill_color = "#F0FDFF"
p1.xgrid.band_fill_alpha = 0.05
p1.ygrid.band_fill_alpha = 0.05

p1.line(datetime(data['Year']), data['Diesel'], color='#FF7271', legend='Diesel')
p1.line(datetime(data['Year']), data['Petrol'], color='#00B1FB', legend='Petrol')
p1.line(datetime(data['Year']), data['Gas'], color='#87FE56', legend='Gas')

show(p1)  # open in a browser
