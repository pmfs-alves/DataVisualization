import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go

df = pd.read_excel(r'.\data\athlete_events.xlsx')

map = go.Figure(data=go.Choropleth(locations=['Portugal'],
                                   z=[100],
                                   showscale=True,
                                   locationmode='ISO-3'),

                layout=dict(geo=dict(showframe=False,
                                     projection={'type': 'equirectangular'}))
                            #sliders=sliders)
                )


