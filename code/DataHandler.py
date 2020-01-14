# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import dash
import dash_html_components as html
import dash_core_components as dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

date_min= 1896  #TODO:  substituir pelo minimo da dataframe  df['year'].min(),
date_max= 2016#TODO:  substituir pelo maximo da dataframe df['year'].max()
dates = range(date_min,date_max+4,4)
datedict =dict((date, str(date)) for date in dates)


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.P([html.Label("Years:"),
    dcc.Slider(
        id='my-slider',
        min=date_min,
        max=date_max+4,
        step=4,
        marks=datedict,
        value=2016,
        included= False,
        persistence_type='session',
        # tooltip= { 'always_visible': True }  #It was fun, mas as funcionalidades das tooltips são limitadas no slider
    )],
    html.Div(id='slider-output-container')
])
#TODO: animations not supported in Dash, check transitions
# https://community.plot.ly/t/exploring-a-transitions-api-for-dcc-graph/15468

#escolha do tipo de modalidades

app.layout = html.Div([
    dcc.RadioItems(
        id='Sport_type',
        options=[
            {'label': 'Colective', 'value': 'Colective'},
            {'label': 'Individual', 'value': 'Individual'},
            {'label': 'Both', 'value': 'Both'}
        ],
        labelStyle={'display': 'inline-block'}
    ),
    html.Div(id='my_filter_team')
])



@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('my_filter_team', 'children'),
    [dash.dependencies.Input('Sport_type', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)






if __name__ == '__main__':
    app.run_server(debug=True)


# app = dash.Dash()
#
# import dash_core_components as dcc
#
# dcc.Dropdown(
#     options=[
#         {'label': 'New York City', 'value': 'NYC'},
#         {'label': 'Montréal', 'value': 'MTL'},
#         {'label': 'San Francisco', 'value': 'SF'}
#     ],
#     value='MTL'
# )









# app.config.suppress_callback_exceptions=True
#
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     html.Div(id='page-content')])
#
# @app.callback(Output('page-content', 'children'),[Input('url', 'pathname')])
# def generate_layout(url):
#     return html.Div([
#         html.Label('Multi-Select Dropdown'),
#         dcc.Dropdown(
#             options=[
#                 {'label': 'New York City', 'value': 'NYC'},
#                 {'label': u'Montréal', 'value': 'MTL'},
#                 {'label': 'San Francisco', 'value': 'SF'}
#             ],
#             value=['MTL', 'SF'],
#             multi=True,
#             id='input'
#         ),
#         html.Div(id='output')
#     ])
#
#
# @app.callback(Output('output', 'children'), [Input('input', 'value')])
# def display_output(value):
#     return 'You have selected "{}"'.format(value)
#
# if __name__ == '__main__':
#     app.run_server(debug=True, host='0.0.0.0')