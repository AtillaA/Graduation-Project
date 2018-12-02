import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
from cycler import cycler
import matplotlib.pyplot as plt
import matplotlib.style
import pandas as pd
import csv

#--------------------------------------------#

data = pd.read_csv("car_ad_edited.csv")
tnr = {'fontname':'Calibri'}

plt.style.use('ggplot')
data.plot(x='Year', y=['Petrol', 'Diesel', 'Gas'], figsize=(10,5), grid=True)
plt.title('Production Rate of Petrol/Diesel/Gas-Based Cars from 1960 to 2016', **tnr, fontsize=18)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Production Rate', fontsize=14)

# fuel['frequency'] = fuel.groupby('year')['year'].transform('size') # Finding the frequency

plt.legend()
plt.show()
