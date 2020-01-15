import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

from dash.dependencies import Input, Output
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go

#--------------------------------------- Get Data ---------------------------------------------------------#
#df_athletes = pd.read_excel(r'C:\Users\Sofia\OneDrive - NOVAIMS\Nova IMS\Mestrado\Cadeiras\Data_Visualization\Projeto DV\DataVisualization\code\data\athlete_events.xlsx', 'athlete_events')
#df_participants = pd.read_excel(r'C:\Users\Sofia\OneDrive - NOVAIMS\Nova IMS\Mestrado\Cadeiras\Data_Visualization\Projeto DV\DataVisualization\code\data\athlete_events.xlsx', 'participants')
#df_athletes = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'athlete_events')
#df_participants = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'participants')

df_athletes = pd.read_excel('data/athlete_events.xlsx', sheet_name='athlete_events')
df_participants = pd.read_excel('data/athlete_events.xlsx', sheet_name='participants')
#df_athletes = pd.read_excel('code/data/athlete_events.xlsx', sheet_name='athlete_events')
#df_participants = pd.read_excel('code/data/athlete_events.xlsx', sheet_name='participants')


#--------------------------------------- Calculations ----------------------------------------------------#
nr_countries = df_athletes.Country.unique()
nr_countries = len(nr_countries)

nr_host_cities = df_participants.City.unique()
nr_host_cities = len(nr_host_cities)

nr_events = df_athletes.Event.unique()
nr_events = len(nr_events)





#Encode Image

encoded_image = base64.b64encode(open('images/Olympic-logo.png', 'rb').read())


#temp

#----------------------------------------Layout------------------------------------------------------------------------#
# Page Layout

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
                    html.P('Summer Olympics Games'),
                ], id='title', className='title', style={'display': 'inline-block'},
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
                    html.Div([str(nr_countries)], className='nr'),
                    html.P('Number of Host Cities: '),
                    html.Div([str(nr_host_cities)], className='nr'),
                    html.P('Number of Events: '),
                    html.Div([str(nr_events)], className='nr')
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
                    #min=df_athletes['year'].min(),
                    #max=df_athletes['year'].max(),
                    #step=4,
                    #marks=datedict,
                    marks={str(i): '{}'.format(str(i)) for i in [df_athletes.Year.unique()]}, #.insert(0, 'All')

                    #tooltip=str(value),
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





#--------------------------------------- Figure Top Countries ---------------------------------------------------------#

#
# athletes_medals = df_athletes[['Name', 'Medal']]
# athletes_medals['c'] = 1
# a_m = athletes_medals.groupby(by=['Name', 'Medal']).c.sum()
# a_m = a_m.to_frame().reset_index()
#
# athletes_names = a_m.Name.unique()
#
# athletes_names_ordered = a_m.groupby(by='Name').c.sum()
# athletes_names_ordered = athletes_names_ordered.to_frame().reset_index()
# athletes_names_ordered = athletes_names_ordered.sort_values(by=['c'], ascending=False)
# top_5_winners = athletes_names_ordered.head()
#
# for athlete in top_5_winners.Name:
#     a_medals = a_m.loc[a_m['Name'] == athlete]
#
#     aux = pd.Series(dict(zip(a_medals.Medal, a_medals.c)))
#
#     Xlim = 29
#     Ylim = 1
#     Xpos = 0
#     Ypos = 1
#     series = []
#     for medal, count in aux.iteritems():
#         x = []
#         y = []
#         for j in range(0, count):
#             if Xpos == Xlim:
#                 Xpos = 0
#                 Ypos -= 1  ##change to positive for upwards
#             x.append(Xpos)
#             y.append(Ypos)
#             Xpos += 1
#         if (medal == 'Gold'):
#             #pass
#             series.append(go.Scatter(x=x, y=y, mode='markers',
#                                      marker={'symbol': 'circle', 'size': 8, 'color': 'rgb(255, 215, 0)'},
#                                      name=f'{medal} ({count})'))
#         elif (medal == 'Silver'):
#             # pass
#             series.append(go.Scatter(x=x, y=y, mode='markers',
#                                      marker={'symbol': 'circle', 'size': 8, 'color': 'rgb(192, 192, 192)'},
#                                      name=f'{medal} ({count})'))
#         elif (medal == 'Bronze'):
#             # pass
#             series.append(go.Scatter(x=x, y=y, mode='markers',
#                                      marker={'symbol': 'circle', 'size': 8, 'color': 'rgb(205, 127, 50)'},
#                                      name=f'{medal} ({count})'))





# Run application
if __name__ == '__main__':
    app.run_server(debug=True)