import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.offline as pyo
import plotly.graph_objects as go

# DATAFRAMES
df_athletes = pd.read_excel(r'.\data\athlete_events.xlsx', 'athlete_events')
df_participants = pd.read_excel(r'.\data\athlete_events.xlsx', 'participants')

# QUERIES
medals_country = pd.DataFrame(df_athletes.groupby("ISO3")["Medal"].count().copy().astype(str))

# CHOROPLETH
#fazer dataframe
df_participants['text'] = 'Country: ' + df_participants['Country'] + '<br>' + \
                                        'Host City ' + df_participants['City'] + '<br>' + \
                                        'Edition ' + df_participants['Edition'] + '<br>' + \
                                        'Hosting Year ' + df_participants['Year'].astype(str)#, + '<br>' + \
                                        #'Number of Medals ' + medals_country


map = go.Figure(data=go.Choropleth(locations=df_athletes['ISO3'],
                                   locationmode='ISO-3',
                                   z=medals_country,
                                   #zmin=0,
                                   #zmax=2650,
                                   #nticks=,
                                   showscale=True,
                                   hovertext= df_participants['text'],
                                   colorscale='BrBG', #RdGy
                                   colorbar={'title': 'Total Number<br>of Medals'}
                                   ),
                layout=dict(geo=dict(landcolor='rgb(255, 255, 255)',
                                     showframe=False,
                                     projection={'type': 'equirectangular'})
                            #sliders=sliders)
                            )
                )

pyo.plot(map)

# LINE CHART

line = go.Figure(data=go.Scatter(x=df_participants['Year'],
                                 y=df_participants['Countries'],
                                 mode='lines',
                                 hovertext=df_participants['Countries'],
                                 line=dict(color='cadetblue',
                                           width=5,
                                           dash='dot'), # "solid", "dot", "dash", "longdash", "dashdot", or "longdashdot"
                                 # shape = "linear" | "spline" | "hv" | "vh" | "hvh" | "vhv"
                                 marker=dict(size=[40, 60, 80, 100],
                                             color=[0, 1, 2, 3]),
                                 showlegend=False
                                 ),
                 layout=dict(#title='',
                             xaxis=dict(title='Year'),
                             yaxis=dict(title='Number of Countries')
                             )
                 )

fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)',
        ),
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    autosize=False,
    margin=dict(
        autoexpand=False,
        l=100,
        r=20,
        t=110,
    ),
    showlegend=False,
    plot_bgcolor='white'
)

# LINE POINT CHART

area = go.Figure(data=go.Scatter(x=df_participants['Year'],
                                 y=df_participants['Countries'],
                                 mode='lines',
                                 hovertext=df_participants['Countries'],
                                 line=dict(color='cadetblue',
                                           width=5,
                                           dash='dot'), # "solid", "dot", "dash", "longdash", "dashdot", or "longdashdot"
                                 # shape = "linear" | "spline" | "hv" | "vh" | "hvh" | "vhv"
                                 marker=dict(size=[40, 60, 80, 100],
                                             color=[0, 1, 2, 3],
                                             symbol='hexagon2-open'),
                                 showlegend=False
                                 ),
                 layout=dict(#title='',
                             xaxis=dict(title='Year'),
                             yaxis=dict(title='Number of Countries')
                             )
                 )

# AREA CHART