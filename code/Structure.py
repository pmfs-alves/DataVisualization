import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as pyo
import plotly.graph_objects as go
import base64

from dash.dependencies import Input, Output
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go

#from code import Code


date_min= 1896  #TODO:  substituir pelo minimo da dataframe  df['year'].min(),
date_max= 2016  #TODO:  substituir pelo maximo da dataframe df['year'].max()
dates = range(date_min,date_max+4,4)
datedict =dict((date, str(date)) for date in dates)



#--------------------------------------- Figure Top Countries ---------------------------------------------------------#
# Import Data



#Encode Image

encoded_image = base64.b64encode(open('images/Olympic-logo.png', 'rb').read())


# Page Layout
app = dash.Dash(__name__, assets_folder='style')

app.layout = html.Div([

    # Div 1. - Title, Heatmap, Top Winers, Top countries
    html.Div([

        # Div 1.1. Title, Heatmap
        html.Div([

            # Div 1.1.1. Title, Nr of Editions, Cities, Countr
            html.Div([
                # Div 1.1.1.1. Title
                html.Div([
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'height':'20%', 'width':'10%'}),
                    #html.Img(src=app.get_asset_url( '/images/Olympic-logo.png')),
                    html.P('Summer Olympics Games')
                ], id='title', className='title'
                ),  # end div 1.1.1.1.

                # Div 1.1.1.2. Nr of Editions
                html.Div([
                    html.P('Number of Editions:'),
                    html.P('XXXI')
                ], id='nr_editions', className='minibox'
                ),  # end div 1.1.1.2.

                # Div 1.1.1.3. Cities Countries
                html.Div([
                    html.P('Number of Countries: '),
                    html.P('Number of Host Cities: '),
                    html.P('Number of Sports: ')
                ], id='details', className='minibox'
                ),  # end div 1.1.1.3.

            ], id='header', className='row_1_1'
            ),  # end div 1.1.1.


            # Div 1.1.2. HeatMap
            html.Div([
                html.P('HEATMAP'),
                # dcc.Graph(id='heatmap', figure=map)
            ], id='HeatMap', className='row_1_2'
            ),  # end div 1.1.2.

        ], id='inner_div_1', className='column_1'
        ),  # end div 1.1.


        # Div 1.2. - Top Winners, Top Countries
        html.Div([
            # Div 1.2.1. - Top Winners
            html.Div([
                html.P('Top Winners'),
                # dcc.Graph(
                #         id='top_contries_fig'
                # )
            ], id='top_winners', className='normalbox'
            ),  # end div 1.2.1.

            # Div 1.2.2. - Top Countries
            html.Div([

                html.P('Top Countries'),

            ], id='top_countries', className='normalbox'
            ),  # end div 1.2.2.

        ], id='inner_div_2', className='column_2'
        ),  # end div 1.2.

    ], className='row_1'
    ),  # end div 1.



    # Div 2. - Slider, Linecharts (Countries, Events, Athletes), Filter, Search
    html.Div([

        # Div 2.1. - Slider, Linecharts (Countries, Events, Athletes)
        html.Div([

            # Div 2.1.1. - Slider
            html.Div([
                html.P('SLIDER'),
                dcc.Slider(
                    id='my-slider',
                    min=date_min,
                    max=date_max + 4,
                    step=4,
                    marks=datedict,
                    value=2016,
                    included=False,
                    persistence_type='session',
                )


            ], id='slider', className='row_2_1',
            ),  # end div 2.1.1.


            # Div 2.1.2. - Linechart/Barchart/Areachart - Countries, Sports, Athletes
            html.Div([
                # Div 2.1.2.1. - Linechart Countries
                html.Div([
                    html.P('Linechart Countries'),
                 #   dcc.Graph(id='linechart', figure=line)
                ], id='countries_linechart', className='boxes'
                ),  # end div 2.1.2.1.

                # Div 2.1.2.2. - Barchart Sports
                html.Div([
                    html.P('Barchart Sports'),
                  #  dcc.Graph(id='linechart', figure=bar)
                ], id='events_linechart', className='boxes'
                ),  # end div 2.1.2.2.

                # Div 2.1.2.3. - Areachart Men & Women
                html.Div([
                    html.P('Athletes Men & Women'),
                  #  dcc.Graph(id='linechart', figure=area)
                ], id='athletes_linechart', className='boxes'
                ),  # end div 2.1.2.3.

            ], id='linecharts', className='row_2_2'
            ),  # end div 2.1.2.

        ], id='inner_div_3', className='column_1'
        ),  # end div 2.1


        # Div 2.2. - Filter, Search
        html.Div([
            html.P('What Type of Sports do you want to see?'),
            dcc.RadioItems(
                id='Sport_type',
                options=[
                    {'label': 'Colective', 'value': 'Colective'},
                    {'label': 'Individual', 'value': 'Individual'},
                    {'label': 'Both', 'value': 'Both'},

                ],
                value='Both',
                labelStyle={'display': 'inline-block'}
            ),
        ], id='inner_div_4', className='column_2'
        ),  # end div 2.2


    ], className='row_2'
    ),  # end div 2.


], id='outer_div'
)



# Run application
if __name__ == '__main__':
    app.run_server(debug=True)