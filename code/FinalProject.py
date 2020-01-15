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
df_countries= pd.read_excel('data/tops_countries.xlsx',sheet_name='Countries')

#df_athletes = pd.read_excel('code/data/athlete_events.xlsx', sheet_name='athlete_events')
#df_participants = pd.read_excel('code/data/athlete_events.xlsx', sheet_name='participants')

#Encode Image

encoded_image = base64.b64encode(open('images/Olympic-logo.png', 'rb').read())

#create years dict
years_select = {str(i): '{}'.format(str(i)) for i in df_participants.Year.unique()}
years_select[1892] = "All"

#create sports dict
sports_select = [dict(label=sport.replace('_', ' '), value=sport) for sport in df_athletes.Sport.unique()]


#calculate numbers
nr_countries = df_athletes.Country.unique()
nr_countries = len(nr_countries)

nr_host_cities = df_participants.City.unique()
nr_host_cities = len(nr_host_cities)

nr_events = df_athletes.Event.unique()
nr_events = len(nr_events)


#-------------------------------------------------------------------------------------------------------#
#----------------------------------------------LAYOUT---------------------------------------------------#
#-------------------------------------------------------------------------------------------------------#

app = dash.Dash(__name__)

app.layout = html.Div([

    # Div 1. - Title, Top Winners, Top countries, Filter, Search
    html.Div([

        # Div 1.1. - Title
        html.Div([
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), id='logo'),
            #html.Img(src=app.get_asset_url( '/images/Olympic-logo.png')),
            html.P('Summer Olympics Games')
        ], id='title', className='title leftboxes'
        ),  # end div 1.1.

        # Div 1.2. - Top Winners
        html.Div([
            html.P('Top Winners'),
            # dcc.Graph(
            #         id='top_contries_fig'
            # )
        ], id='top_winners', className='leftboxes'
        ),  # end div 1.2.

        # Div 1.3. - Top Countries
        html.Div([

            html.P('Top Countries')

        ], id='top_countries', className='leftboxes'
        ),  # end div 1.3.

        # Div 1.4. - Search, Filter
        html.Div([
            # Div 1.4.1. - Filter
            html.Div([
                html.P('What Type of Sports do you want to see?'),
                dcc.RadioItems(
                    id='sport_type',
                    options=[
                        {'label': 'Colective', 'value': 'colective'},
                        {'label': 'Individual', 'value': 'individual'},
                        {'label': 'Both', 'value': 'both'},

                    ],
                    value='both',
                    labelStyle={'display': 'inline-block'}
                )
            ], id='filter'
            ),  # end div 1.4.1

            # Div 1.4.2. - Search
            html.Div([
                html.P(),
                html.P("Do you want to select particular sports?"),
                dcc.Dropdown(
                    id='sport_select',
                    options=sports_select,
                    value=[],
                    multi=True
                )
            ], id='search'
            )  # end div 1.4.2.

        ], id='filters', className='leftboxes'
        )  # end div 1.4.


    ], id='div_1', className='column_1'
    ),  # end div 1.



    # Div 2. - Nr of Editions, HeatMap, Slider, Linecharts (Countries, Events, Athletes)
    html.Div([

        # Div 2.1. - Nr of Editions, Nr Countries, Nr Cities, Nr Events
        html.Div([
            # Div 2.1.1. - Nr of Editions
            html.Div([
                html.P('Number of Editions:'),
                html.P('XXXI')
            ], id='nr_editions', className='miniboxes'
            ),  # end div 2.1.1.

            # Div 2.1.2. - Nr Countries
            html.Div([
                html.P('Number of Countries: '),
                html.Div([str(nr_countries)], className='nr')
            ], id='nr_countries', className='miniboxes'
            ),  # end div 2.1.2.

            # Div 2.1.2. - Nr Cities
            html.Div([
                html.P('Number of Host Cities: '),
                html.Div([str(nr_host_cities)], className='nr'),
            ], id='nr_cities', className='miniboxes'
            ),  # end div 2.1.2.

            # Div 2.1.3. - Nr Events
            html.Div([
                html.P('Number of Events: '),
                html.Div([str(nr_events)], className='nr')
            ], id='nr_events', className='miniboxes'
            ),  # end div 2.1.3.

        ], id='counts', className='row_1'
        ),  # end div 2.1.


        # Div 2.2. - HeatMap
        html.Div([
            html.P('HEATMAP'),
            html.Div([dcc.Graph(id='map_choroplet')], className='nice_choro'),
            html.P('Rita'),
            # dcc.Graph(id='heatmap', figure=map)
        ], id='heatmap', className='row_2'
        ),  # end div 2.2.

        # Div 2.3. - Slider
        html.Div([
            html.P('SLIDER'),
            dcc.Slider(
                id='year_slider',
                min=1892,
                max=2016,
                step=4,
                #marks=datedict,
                marks=years_select, #.insert(0, 'All')
                #tooltip=str(value),
                value=1892,
                included=False,
                persistence_type='session',
            )
        ], id='slider', className='row_3'
        ),  # end div 2.3.

        # Div 2.4. - Linechart/Barchart/Areachart - Countries, Sports, Athletes
        html.Div([
            # Div 2.4.1. - Linechart Countries
            html.Div([
                html.P('Linechart Countries'),
             #   dcc.Graph(id='linechart', figure=line)
            ], id='countries_linechart', className='boxes'
            ),  # end div 2.4.1.

            # Div 2.4.2. - Barchart Sports
            html.Div([
                html.P('Barchart Sports'),
              #  dcc.Graph(id='linechart', figure=bar)
            ], id='events_linechart', className='boxes'
            ),  # end div 2.4.2.

            # Div 2.4.3. - Areachart Men & Women
            html.Div([
                html.P('Athletes Men & Women'),
              #  dcc.Graph(id='linechart', figure=area)
            ], id='athletes_linechart', className='boxes'
            ),  # end div 2.4.3.

        ], id='linecharts', className='row_4'
        )  # end div 2.4.


    ], id='div_2', className='column_2'
    )  # end div 2.

], id='outer_div',
)


#----------------------------------------Callbacks---------------------------------------------------------------------#

@app.callback(

        Output("map_choroplet", "figure"),
        # Output("choropleth", "figure"),
        # Output("countries_linechart", "figure"),

    [
        Input("sport_type", "value"),
        Input("sport_select", "value"),
        Input("year_slider", "value"),

    ]
    )


#----------------------------------------Callbacks---------------------------------------------------------------------#
def update_graph (team, sport, year):


    #reduces the dataframe to be used to update the graphs, given the inputs
    #def countries(year, sport, team):
    if (year == 1892) & (len(sport) == 0) & (team == 'both'):
        df = df_countries
    elif (year != 1892) & (len(sport) == 0) & (team == 'both'):
        df = df_countries.loc[df_countries['Year'] == year, :]
    elif (year != 1892) & (len(sport) != 0) & (team == 'both'):
        df = df_countries.loc[(df_countries['Year'] == year) & (df_countries['Sport'].isin(sport)), :]
    elif (year != 1892) & (len(sport) != 0) & (team != 'both'):
        df = df_countries.loc[(df_countries['Year'] == year) & (df_countries['Sport'].isin(sport)) & (
                    df_countries['Team Sport'] == team), :]
    elif (year == 1892) & (len(sport) != 0) & (team == 'both'):
        df = df_countries.loc[df_countries['Sport'].isin(sport), :]
    elif (year == 1892) & (len(sport) == 0) & (team != 'both'):
        df = df_countries.loc[df_countries['Team Sport'] == team, :]
    elif (year == 1892) & (len(sport) != 0) & (team != 'both'):
        df = df_countries.loc[(df_countries['Sport'].isin(sport)) & (df_countries['Team Sport'] == team), :]
    elif (year != 1892) & (len(sport) == 0) & (team != 'both'):
        df = df_countries.loc[(df_countries['Year'] == year) & (df_countries['Team Sport'] == team), :]

    df = df.groupby(by=['Country'])['Gold', 'Silver', 'Bronze', 'Total'].sum()
    df['Country'] = df.index
    df.reset_index(drop=True, inplace=True)

    df = df.merge(df_athletes[['ISO3', 'Country']], on='Country', how='left')
    df.drop_duplicates(inplace=True)

    df = df.merge(df_participants[['City', 'Country', 'Edition']], how='outer', on='Country')
    df.fillna('No host', inplace=True)

    df = df.groupby('Country').agg({'Gold': 'first', 'Silver': 'first', 'Bronze': 'first', 'Total': 'first',
                                    'ISO3': 'first', 'City': ', '.join, 'Edition': ', '.join}).reset_index()

     #   return df
    
    #df = countries(year, sport, team)

    ######################################MAP  CREATION##################################################33



    #map.add_trace(go.Choropleth(locations=df['ISO3'],
    trace1= go.Choropleth(locations=df['ISO3'],
                                locationmode='ISO-3',
                                z=df['Total'],
                                text=np.array(df),
                                name='Total',
                                hovertemplate="<b>%{text[0]}</b><br>" +
                                              "Host City: %{text[6]}<br>" +
                                              "Edition: %{text[7]}<br>" +
                                              "Total Number of Medals: %{text[4]:.0f}<br>",
                                hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                                bordercolor='rgb(242, 242, 242)',
                                                font=dict(size=13,
                                                          color='rgb(0, 0, 0)',
                                                          ),
                                                namelength=0,
                                                ),
                                autocolorscale=False,
                                marker=dict(line=dict(width=0)),
                                colorscale='Cividis',
                                colorbar=dict(title=dict(text='Total Number<br>of Medals \n',
                                                         font=dict(color='white')),
                                              tickfont=dict(color='white')))
    #map.add_trace(go.Choropleth(locations=df['ISO3'],
    trace2= go.Choropleth(locations=df['ISO3'],
                                locationmode='ISO-3',
                                z=df['Gold'],
                                text=np.array(df),
                                name='Gold',
                                hovertemplate="<b>%{text[0]}</b><br>" +
                                              "Host City: %{text[6]}<br>" +
                                              "Edition: %{text[7]}<br>" +
                                              "Total Number of Medals: %{text[4]:.0f}<br>" +
                                              "   Gold:  %{text[1]:.0f}",
                                hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                                bordercolor='rgb(242, 242, 242)',
                                                font=dict(size=13,
                                                          color='rgb(0, 0, 0)',
                                                          ),
                                                namelength=0,
                                                ),
                                autocolorscale=False,
                                marker=dict(line=dict(width=0)),
                                colorscale='Cividis',
                                colorbar=dict(title=dict(text='Total Number<br>of Golden Medals \n',
                                                         font=dict(color='white')),
                                              tickfont=dict(color='white')))
    trace3= go.Choropleth(locations=df['ISO3'],
                                locationmode='ISO-3',
                                z=df['Silver'],
                                text=np.array(df),
                                name='Silver',
                                hovertemplate="<b>%{text[0]}</b><br>" +
                                              "Host City: %{text[6]}<br>" +
                                              "Edition: %{text[7]}<br>" +
                                              "Total Number of Medals: %{text[4]:.0f}<br>" +
                                              "   Silver:  %{text[2]:.0f}",
                                hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                                bordercolor='rgb(242, 242, 242)',
                                                font=dict(size=13,
                                                          color='rgb(0, 0, 0)',
                                                          ),
                                                namelength=0,
                                                ),
                                autocolorscale=False,
                                marker=dict(line=dict(width=0)),
                                colorscale='Cividis',
                                colorbar=dict(title=dict(text='Total Number<br>of Silver Medals \n',
                                                         font=dict(color='white')),
                                              tickfont=dict(color='white')))
    trace4= go.Choropleth(locations=df['ISO3'],
                                locationmode='ISO-3',
                                z=df['Bronze'],
                                text=np.array(df),
                                name='Bronze',
                                hovertemplate="<b>%{text[0]}</b><br>" +
                                              "Host City: %{text[6]}<br>" +
                                              "Edition: %{text[7]}<br>" +
                                              "Total Number of Medals: %{text[4]:.0f}<br>" +
                                              "   Bronze:  %{text[3]:.0f}",
                                hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                                bordercolor='rgb(242, 242, 242)',
                                                font=dict(size=13,
                                                          color='rgb(0, 0, 0)',
                                                          ),
                                                namelength=0,
                                                ),
                                autocolorscale=False,
                                marker=dict(line=dict(width=0)),
                                colorscale='Cividis',
                                colorbar=dict(title=dict(text='Total Number<br>of Bronze Medals \n',
                                                         font=dict(color='white')),
                                              tickfont=dict(color='white')))
    trace5= dict(geo=dict(landcolor='rgb(43, 43, 43)',
                               showcountries=False,
                               # showframe=False,
                               framewidth=0,
                               coastlinecolor='rgb(43, 43, 43)',
                               showcoastlines=True,
                               showland=True,
                               showocean=True,
                               oceancolor='rgb(30, 30, 30)',
                               showlakes=True,
                               lakecolor='rgb(30, 30, 30)',
                               projection={'type': 'equirectangular'}),
                      paper_bgcolor='rgb(30, 30, 30)',
                      plot_bgcolor='rgb(30, 30, 30)',
                 updatemenus=[
                     go.layout.Updatemenu(
                         visible=True,
                         type='buttons',
                         direction="right",
                         active=0,
                         buttons=list([
                             dict(args=[{"visible": [True, False, False, False]}],
                                  label="Total", method="update"),
                             dict(args=[{"visible": [False, True, False, False]}],
                                  label="Gold", method="update"),
                             dict(args=[{"visible": [False, False, True, False]}],
                                  label="Silver", method="update"),
                             dict(args=[{"visible": [False, False, False, True]}],
                                  label="Bronze", method="update"),
                         ]),
                         showactive=True,
                         x=0,
                         xanchor="left",
                         y=0,
                         yanchor="top",
                         bgcolor='rgb(30, 30, 30)',
                         font=dict(color='rgb(165, 149, 1)')
                     )
                 ],
                 annotations=[
                     go.layout.Annotation(text="Medals Type", showarrow=False,
                                          x=0, y=0, yref="paper", align="left", font=dict(color='white'))
                 ]
                 )

    #pyo.plot(map)


    return go.Figure(data=[trace1, trace2,trace3,trace4], layout=trace5)
#--------------------------------------- Figure Top Countries ---------------------------------------------------------#


athletes_medals = df_athletes[['Name', 'Medal']]
athletes_medals['c'] = 1
a_m = athletes_medals.groupby(by=['Name', 'Medal']).c.sum()
a_m = a_m.to_frame().reset_index()

athletes_names = a_m.Name.unique()

athletes_names_ordered = a_m.groupby(by='Name').c.sum()
athletes_names_ordered = athletes_names_ordered.to_frame().reset_index()
athletes_names_ordered = athletes_names_ordered.sort_values(by=['c'], ascending=False)
top_5_winners = athletes_names_ordered.head()

for athlete in top_5_winners.Name:
    a_medals = a_m.loc[a_m['Name'] == athlete]

    aux = pd.Series(dict(zip(a_medals.Medal, a_medals.c)))

    Xlim = 29
    Ylim = 1
    Xpos = 0
    Ypos = 1
    series = []
    for medal, count in aux.iteritems():
        x = []
        y = []
        for j in range(0, count):
            if Xpos == Xlim:
                Xpos = 0
                Ypos -= 1  ##change to positive for upwards
            x.append(Xpos)
            y.append(Ypos)
            Xpos += 1
        if (medal == 'Gold'):
            #pass
            series.append(go.Scatter(x=x, y=y, mode='markers',
                                     marker={'symbol': 'circle', 'size': 8, 'color': 'rgb(255, 215, 0)'},
                                     name=f'{medal} ({count})'))
        elif (medal == 'Silver'):
            # pass
            series.append(go.Scatter(x=x, y=y, mode='markers',
                                     marker={'symbol': 'circle', 'size': 8, 'color': 'rgb(192, 192, 192)'},
                                     name=f'{medal} ({count})'))
        elif (medal == 'Bronze'):
            # pass
            series.append(go.Scatter(x=x, y=y, mode='markers',
                                     marker={'symbol': 'circle', 'size': 8, 'color': 'rgb(205, 127, 50)'},
                                     name=f'{medal} ({count})'))





# Run application
if __name__ == '__main__':
    app.run_server(debug=True)