from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
import plotly.figure_factory as ff

#init_notebook_mode(connected=True)

import pandas as pd

df = pd.read_excel('gantt.xlsx')
colors = {'0-25': 'rgb(135,206,250)',
          '25-50': 'rgb(30,144,255)',
          '50-75': 'rgb(138,43,226)',
          '75-100': 'rgb(0,0,255)',
          'Complete': 'rgb(25,25,112)',
          'Not_Started':'rgb(192,192,192)'}

fig = ff.create_gantt(df, colors=colors, index_col='Percentage_of_Completion', title='Projects - Gantt chart',
	  show_colorbar=True,group_tasks=True,showgrid_x=True, showgrid_y=True)

plot(fig, filename='Projects-Gantt_chart.html')