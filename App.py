import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

from dash.dependencies import Input, Output
from dash.dependencies import Input, Output
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go
import plotly.express as px


#-------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------ Get Data ---------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------#

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




#-------------------------------------------------------------------------------------------------------------------#
#--------------------------------------------------- Charts --------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------#

#--------------------------------------------------- Line Chart ----------------------------------------------------#
line = go.Figure(data=go.Scatter(x=df_participants['Year'],
                                 y=df_participants['Countries'],
                                 mode="lines+markers",
                                 text=df_participants['Edition'],
                                 hovertemplate="<b>%{y:,.0f}</b> countries participated<br>in the %{text} Summer Olympics <b>(%{x})",
                                 hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                                 bordercolor='rgb(242, 242, 242)',
                                                 font=dict(size=12,
                                                           color='black',
                                                           ),
                                                 namelength=0,
                                                 ),
                                 line=dict(color='rgb(244, 212, 77)',
                                           width=3,
                                           dash='solid'),
                                 marker=dict(symbol="circle-dot",
                                             size=8, color='rgb(230, 230, 230)'),
                                 showlegend=False
                                 ),
                 layout=dict(xaxis=dict(title=dict(text="Year",
                                                   font=dict(family='Arial',
                                                             size=12,
                                                             color='white',
                                                             ),
                                                   ),
                                        showline=True,
                                        showgrid=False,
                                        showticklabels=True,
                                        linecolor='white',
                                        linewidth=1.5,
                                        ticks='outside',
                                        tickcolor='white',
                                        tickfont=dict(
                                            family='Arial',
                                            size=12,
                                            color='white',
                                        ),

                                        tickvals=[1896, 1904, 1912, 1920, 1928, 1936, 1948, 1956, 1964,
                                                  1972, 1980, 1988, 1996, 2004, 2012],
                                        dtick=4,
                                        tickangle=45,
                                        showspikes=True,
                                        spikecolor='rgb(179, 203, 203)'
                                        ),
                             yaxis=dict(title=dict(text="Number of Countries",
                                                   font=dict(family='Arial',
                                                             size=12,
                                                             color='white',
                                                             ),
                                                   ),
                                        showgrid=False,
                                        showline=True,
                                        showticklabels=True,
                                        linecolor='white',
                                        linewidth=1.5,
                                        ticks='outside',
                                        tickcolor='white',
                                        tickfont=dict(family='Arial',
                                                      size=12,
                                                      color='white',
                                                      ),
                                        # tick0 = 0,
                                        dtick=50,
                                        range=[0, 250],
                                        ),

                             autosize=False,
                             width=530,
                             height=400,
                             margin=dict(autoexpand=False,
                                         l=50, r=5, t=10, b=70
                                         ),
                             showlegend=False,
                             paper_bgcolor='rgba(0,0,0,0)',
                             plot_bgcolor='rgba(0,0,0,0)'
                             )
                 )

line.add_annotation(
    go.layout.Annotation(
        x=1976,
        y=92,
        xref="x",
        yref="y",
        text="After New Zealand's rugby team broke the<br>international sports embargo on Apartheid<br>in South Africa, 28 African countries boycotted<br>the summer games in Montreal.",
        showarrow=True,
        font=dict(
            family="Arial",
            size=12,
            color="#ffffff"
        ),
        align="left",
        arrowhead=1,
        arrowsize=1,
        arrowwidth=1,
        arrowcolor="#636363",
        ax=-100,
        ay=-120,
        bordercolor="#619292",
        borderwidth=1,
        borderpad=4,
        bgcolor="#619292",
        opacity=0.8
    )
)

line.add_annotation(
    go.layout.Annotation(
        x=1980,
        y=80,
        xref="x",
        yref="y",
        text="Led by the United States, 66 countries<br>boycotted the games because<br>of the Soviet–Afghan War.",
        showarrow=True,
        font=dict(
            family="Arial",
            size=12,
            color="#ffffff"
        ),
        align="left",
        arrowhead=1,
        arrowsize=1,
        arrowwidth=1,
        arrowcolor="#636363",
        ax=50,
        ay=40,
        bordercolor="#619292",
        borderwidth=1,
        borderpad=4,
        bgcolor="#619292",
        opacity=0.8
    )
)

fig_countries_linechart = line

# -------------------------------------------------------------------------------------------------------------------
# AREA CHART
# -----------------------------------------------------------------------------------------------------------------

trace1 = go.Scatter(x=df_participants['Year'],
                    y=df_participants['Men'],
                    mode="lines+markers",
                    fill="tonexty",  # "none" | "tozeroy" | "tozerox" | "tonexty" | "tonextx" | "toself" | "tonext"
                    fillcolor='rgb(179, 204, 204)',
                    stackgroup='one',
                    text=df_participants['Participants'],
                    hovertemplate="<b>%{x}</b><br>Total: %{text:.0f}<br>Men: %{y:.0f}",
                    hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(242, 242, 242)',
                                    font=dict(size=12,
                                              color='rgb(0, 0, 0)',
                                              ),
                                    namelength=0,
                                    ),
                    line=dict(color='rgb(102, 153, 153)',
                              width=3,
                              dash='solid',
                              shape="linear"),  # "linear" | "spline"
                    marker=dict(symbol='x-dot',
                                size=5, color='rgb(31, 46, 46)'),
                    showlegend=False,
                    )

trace2 = go.Scatter(x=df_participants['Year'],
                    y=df_participants['Women'],
                    mode="lines+markers",
                    fill="tonexty",  # "tozeroy" |"tonexty" | "tonextx" | "toself" | "tonext"
                    fillcolor='rgb(255, 217, 179)',
                    stackgroup='one',
                    text=df_participants['Participants'],
                    hovertemplate="<b>%{x}</b><br>Total: %{text:.0f}<br>Women: %{y:.0f}",
                    hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(242, 242, 242)',
                                    font=dict(size=12,
                                              color='rgb(0, 0, 0)',
                                              ),
                                    namelength=0,
                                    ),
                    line=dict(color='rgb(255, 191, 128)',
                              width=3,
                              dash='solid',
                              shape="linear"),  # "linear" | "spline"
                    marker=dict(symbol='x-dot',
                                size=5, color='rgb(153, 77, 0)'),
                    showlegend=False,
                    )

layout = dict(xaxis=dict(title=dict(text="Year",
                                    font=dict(family='Arial',
                                              size=13,
                                              color='white',
                                              ),
                                    ),
                         showline=True,
                         showgrid=False,
                         showticklabels=True,
                         linecolor='rgb(0, 0, 0)',
                         linewidth=2,
                         ticks='outside',
                         tickcolor='white',
                         tickfont=dict(
                             family='Arial',
                             size=12,
                             color='white',
                         ),
                         tickvals=[1896,1904,1912,1920,1928,1936,1948,1956,1964,
                                                  1972,1980,1988,1996,2004,2012],
                         dtick=4,
                         tickangle=45,
                         showspikes=True,
                         spikecolor='rgb(0, 0, 0)',
                         spikethickness=2,
                         ),
              yaxis=dict(title=dict(text="Number of Athletes",
                                    font=dict(family='Arial',
                                              size=13,
                                              color='white',
                                              ),
                                    ),
                         showgrid=False,
                         showline=True,
                         showticklabels=True,
                         linecolor='white',
                         linewidth=2,
                         ticks='outside',
                         tickcolor='white',
                         tickfont=dict(family='Arial',
                                       size=12,
                                       color='white',
                                       ),
                         tick0=0,
                         range=[0, 12000],
                         side='right',
                         ),
              autosize=False,
              width=520,
              height=400,
              margin=dict(autoexpand=False,
                          l=10,r=50,t=10,b=70
                       ),
              showlegend=False,
              paper_bgcolor='rgba(0, 0, 0)',
              plot_bgcolor='rgba(0, 0, 0)'
              )

area = go.Figure(data=[trace1, trace2], layout=layout)

area.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

area.add_annotation(
    go.layout.Annotation(
        x=1932,
        y=1332,
        xref="x",
        yref="y",
        text="Worldwide Great<br>Depression",
        showarrow=True,
        font=dict(
            family="Arial",
            size=12,
            color="#ffffff"
        ),
        align="left",
        arrowhead=1,
        arrowsize=1,
        arrowwidth=1,
        arrowcolor="#636363",
        ax=-50,
        ay=-130,
        bordercolor="#619292",
        borderwidth=1,
        borderpad=4,
        bgcolor="#619292",
        opacity=0.8
    )
)

area.add_annotation(
    go.layout.Annotation(
        x=1956,
        y=3314,
        xref="x",
        yref="y",
        text="Protest due to the IOC's<br>rejection to suspend the USSR<br>after their invasion of Hungary.",
        showarrow=True,
        font=dict(
            family="Arial",
            size=12,
            color="#ffffff"
        ),
        align="left",
        arrowhead=1,
        arrowsize=1,
        arrowwidth=1,
        arrowcolor="#636363",
        ax=-75,
        ay=-150,
        bordercolor="#619292",
        borderwidth=1,
        borderpad=4,
        bgcolor="#619292",
        opacity=0.8
    )
)


# ------------------------------------------------------------------------------------------------------------------
#  STACKED BAR FOR SPORTS
# ------------------------------------------------------------------------------------------------------------------

years=df_participants['Year']

df_participants['New Sports']=""
df_participants['Returned Sports']=""
df_participants['Maintained Sports']=""
df_participants['Lost Sports']=""

all_sports = []
previous_list=[]
for idx, x in enumerate(years):
    if (idx!=0):
        previous_list.extend(df_participants.at[idx-1,'New Sports'])
        previous_list.extend(df_participants.at[idx-1,'Returned Sports'])
        previous_list.extend(df_participants.at[idx-1,'Maintained Sports'])
        df_participants.at[idx, 'Lost Sports'] = [a for a in previous_list
                                                  if a not in df_athletes[
                                                      df_athletes['Year'] == x].Sport.unique().tolist()]

    if (idx == 0):
        df_participants.at[idx, 'New Sports'] = df_athletes[df_athletes['Year'] == years[0]].Sport.unique().tolist()
        df_participants.at[idx, 'Returned Sports'] = []
        df_participants.at[idx, 'Maintained Sports'] = []
        df_participants.at[idx, 'Lost Sports'] = []
    elif (idx == 1):
        df_participants.at[idx, 'New Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist() if a not in df_participants['New Sports'][idx - 1]]
        df_participants.at[idx, 'Returned Sports'] = []
        df_participants.at[idx, 'Maintained Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist() if a in df_participants['New Sports'][idx - 1]]
    else:
        df_participants.at[idx, 'New Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist() if a not in all_sports]
        df_participants.at[idx, 'Returned Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist()
                                                        if a not in df_participants['New Sports'][idx - 1] and a in all_sports and
                                                             a not in df_participants['Maintained Sports'][idx - 1] and a not in
                                                             df_participants['Returned Sports'][idx - 1]]
        df_participants.at[idx, 'Maintained Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist()
                                                       if a in df_participants['New Sports'][idx - 1]
                                                       or a in df_participants['Returned Sports'][idx - 1]
                                                       or a in df_participants['Maintained Sports'][idx - 1]]

    previous_list=[]
    all_sports.extend(df_participants.at[idx,'New Sports'])

df_participants['New Sports_Count']=""
df_participants['Returned Sports_Count']=""
df_participants['Maintained Sports_Count']=""

for idx, x in enumerate(years):
    df_participants.at[idx,'New Sports_Count'] = len(df_participants.at[idx,'New Sports'])
    df_participants.at[idx,'Returned Sports_Count'] = len(df_participants.at[idx,'Returned Sports'])
    df_participants.at[idx,'Maintained Sports_Count'] = len(df_participants.at[idx,'Maintained Sports'])

for idx, x in enumerate(years):
    df_participants.at[idx,'New Sports'] = [' {0}'.format(elem) if idx!=0 else '{0}'.format(elem) for idx, elem in enumerate(df_participants.at[idx,'New Sports'])]
    df_participants.at[idx,'Returned Sports'] = [' {0}'.format(elem) if idx!=0 else '{0}'.format(elem) for idx, elem in enumerate(df_participants.at[idx,'Returned Sports'])]
    df_participants.at[idx,'Maintained Sports'] = [' {0}'.format(elem) if idx!=0 else '{0}'.format(elem) for idx, elem in enumerate(df_participants.at[idx,'Maintained Sports'])]
    df_participants.at[idx,'Lost Sports'] = [' {0}'.format(elem) if idx!=0 else '{0}'.format(elem) for elem in df_participants.at[idx, 'Lost Sports']]

for idx, x in enumerate(years):
    if df_participants.at[idx,'Lost Sports'] == []:
        df_participants.at[idx, 'Lost Sports'] = 0

layout= dict(title=dict(text="<b><i> Even Sports need to qualify?",
                        font=dict(family='Raleway',
                                  size=30,
                                  color='rgb(0, 0, 0)',
                                  ),
                        x=0.5,
                        ),
             xaxis=dict(title=dict(text="<b>Year",
                                   font=dict(family='Arial',
                                             size=16,
                                             color='rgb(0, 0, 0)',
                                           ),
                                   ),
                        showline=True,
                        showgrid=False,
                        showticklabels=True,
                        linecolor='rgb(0, 0, 0)',
                        linewidth=2,
                        ticks='outside',
                        range=[1894,2018],
                        tickfont=dict(
                                family='Arial',
                                size=14,
                                color='rgb(0, 0, 0)',
                                ),
                        tickvals=df_participants['Year'].unique().tolist(),
                        dtick = 4,
                        tickangle=45
                        ),
              yaxis=dict(title=dict(text="<b>Number of Sports",
                                   font=dict(family='Arial',
                                             size=16,
                                             color='rgb(0, 0, 0)',
                                           ),
                                   ),
                         showgrid=True,
                         showline=True,
                         showticklabels=True,
                         linecolor='rgb(0, 0, 0)',
                         linewidth=2,
                         ticks='outside',
                         tickfont=dict(family='Arial',
                                       size=14,
                                       color='rgb(0, 0, 0)',
                                       ),
                         tick0 = 0

                       ),
            showlegend=True,

            template='plotly_white'  # added to show grid
            #plot_bgcolor='white' erased to enable grid
            ,legend=dict(
             uirevision=False
    )
)


bar = go.Figure(data=[
    go.Bar(name='Maintained Sports', x=df_participants['Year'], y=df_participants['Maintained Sports_Count'],
           text=df_participants['Lost Sports'], marker=dict(color='rgb(0, 153, 204)'),
           hovertemplate="<b>Maintained Sports:</b> %{y:.0f}<br><b>Lost Sports:</b> %{text}",
           hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(242, 242, 242)',
                                    font=dict(size=13,
                                              color='rgb(0, 0, 0)',
                                              ),
                                    namelength=0,
                                    )),

    go.Bar(x=df_participants['Year'], y=df_participants['Returned Sports_Count'], name='Returned Sports',
           text= df_participants['Returned Sports'], marker=dict(color='rgb(255, 153, 102)'),
           hovertemplate="<b>Returned Sports:'</b> %{y:.0f}<br>%{text}", #Total Sports: %{text}<br>
           hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(242, 242, 242)',
                                    font=dict(size=13,
                                              color='rgb(0, 0, 0)',
                                              ),
                                    namelength=0,
                                    )),
    go.Bar(name='New Sports', x=df_participants['Year'], y=df_participants['New Sports_Count'],
           text=df_participants['New Sports'], marker=dict(color='rgb(0, 204, 153)'),#color='time',
           hovertemplate="<b>New Sports:</b> %{y:.0f}<br>%{text}", #Total Sports: %{text}<br>
           hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(242, 242, 242)',
                                    font=dict(size=13,
                                              color='rgb(0, 0, 0)',
                                              ),
                                    namelength=0,
                                    ))],
    layout=layout)

# Change the bar mode
bar.update_layout(barmode='stack')

# Add totals at the top of the bars
bar.add_trace(go.Scatter(
    x=df_participants['Year'],
    y=df_participants['Sports'],
    mode="text",
   # name="Lines, Markers and Text",
    text=df_participants['Sports'],
    textposition="top center",
    showlegend=False,
    hoverinfo='skip'
))







#--------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------LAYOUT-----------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------#

app = dash.Dash(__name__, assets_folder='style')

server = app.server

app.layout = html.Div([

    # Div 1. - Title, Top Winners, Top countries, Filter, Search
    html.Div([

        # Div 1.1. - Title
        html.Div([
            html.P('Olympic Games'),
            html.P('Summer', id='p2'),
            html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), id='logo')
            #html.Img(src=app.get_asset_url( '/images/Olympic-logo.png')),

        ], id='title', className='title leftboxes'
        ),  # end div 1.1.

        # Div 1.2. - Top Winners
        html.Div([
            html.H2('Top Winners'),
            # dcc.Graph(
            #         id='top_contries_fig'
            # )
        ], id='top_winners', className='leftboxes'
        ),  # end div 1.2.

        # Div 1.3. - Top Countries
        html.Div([

            html.H2('Top Countries')

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
                        {'label': 'Team', 'value': 'Team'},
                        {'label': 'Individual', 'value': 'Individual'},
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
                html.H3('Number of Editions:'),
                html.P('XXXI')
            ], id='nr_editions', className='miniboxes'
            ),  # end div 2.1.1.

            # Div 2.1.2. - Nr Countries
            html.Div([
                html.H3('Number of Countries: '),
                html.Div([str(nr_countries)], className='nr')
            ], id='nr_countries', className='miniboxes'
            ),  # end div 2.1.2.

            # Div 2.1.2. - Nr Cities
            html.Div([
                html.H3('Number of Host Cities: '),
                html.Div([str(nr_host_cities)], className='nr'),
            ], id='nr_cities', className='miniboxes'
            ),  # end div 2.1.2.

            # Div 2.1.3. - Nr Events
            html.Div([
                html.H3('Number of Events: '),
                html.Div([str(nr_events)], className='nr')
            ], id='nr_events', className='miniboxes'
            ),  # end div 2.1.3.

        ], id='counts', className='row_1'
        ),  # end div 2.1.


        # Div 2.2. - HeatMap
        html.Div([
            html.Div([dcc.Graph(id='map_choroplet',config={'displayModeBar':False})], className='nice_choro'),
            # dcc.Graph(id='heatmap', figure=map)
        ], id='heatmap', className='row_2'
        ),  # end div 2.2.

        # Div 2.3. - Slider
        html.Div([
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

        # Div 2.4. - Linechart/Barchart/Areachart - Countries, Areachart Men & Women
        html.Div([
            # Div 2.4.1. - Linechart Countries
            html.Div([
                html.P('Olympics getting Popular'),
                dcc.Graph(
                    id='c_linechart',
                    config={'displayModeBar':False},
                    figure=fig_countries_linechart
                )
            ], id='countries_linechart', className='boxes'
            ),  # end div 2.4.1.

            # Div 2.4.2. - Areachart Men & Women
            html.Div([
                html.P('Athletes Men & Women'),
                dcc.Graph(
                    id='a_linechart',
                    config={'displayModeBar':False},
                    figure=area
                )
            ], id='athletes_linechart', className='boxes'
            ),  # end div 2.4.2.

        ], id='linecharts', className='row_4'
        ),  # end div 2.4.

        # Div 2.5. - Barchart
        html.Div([
            # Div 2.5.1. - Barchart Sports
            html.Div([
                html.P('Even Sports need to Qualify?'),

            ], id='sports_linechart', className='boxes'
            ),  # end div 2.5.1.
            dcc.Graph(
                id='barchart',
                config={'displayModeBar':False},
                figure=bar
            )
        ], id='bar_chart', className='row_5'
        ),  # end div 2.4.2.


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

    trace1 = go.Choropleth(locations=df['ISO3'],
                           locationmode='ISO-3',
                           z=df['Total'],
                           text=np.array(df),
                           name='Total',
                           hovertemplate="<b>%{text[0]}</b><br>" +
                                         "Host City: %{text[6]}<br>" +
                                         "Edition: %{text[7]}<br>" +
                                         "Total Number of Medals: %{text[4]:.0f}<br>" +
                                         "     Gold:  %{text[1]:.0f}" +
                                         "     Silver:  %{text[2]:.0f}" +
                                         "     Bronze:  %{text[3]:.0f}",
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
    trace2 = go.Choropleth(locations=df['ISO3'],
                           locationmode='ISO-3',
                           z=df['Gold'],
                           text=np.array(df),
                           name='Gold',
                           hovertemplate="<b>%{text[0]}</b><br>" +
                                         "Host City: %{text[6]}<br>" +
                                         "Edition: %{text[7]}<br>" +
                                         "Total Number of Medals: %{text[4]:.0f}<br>" +
                                         "     Gold:  %{text[1]:.0f}",
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
    trace3 = go.Choropleth(locations=df['ISO3'],
                           locationmode='ISO-3',
                           z=df['Silver'],
                           text=np.array(df),
                           name='Silver',
                           hovertemplate="<b>%{text[0]}</b><br>" +
                                         "Host City: %{text[6]}<br>" +
                                         "Edition: %{text[7]}<br>" +
                                         "Total Number of Medals: %{text[4]:.0f}<br>" +
                                         "     Silver:  %{text[2]:.0f}",
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
    trace4 = go.Choropleth(locations=df['ISO3'],
                           locationmode='ISO-3',
                           z=df['Bronze'],
                           text=np.array(df),
                           name='Bronze',
                           hovertemplate="<b>%{text[0]}</b><br>" +
                                         "Host City: %{text[6]}<br>" +
                                         "Edition: %{text[7]}<br>" +
                                         "Total Number of Medals: %{text[4]:.0f}<br>" +
                                         "     Bronze:  %{text[3]:.0f}",
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
    layout = dict(geo=dict(landcolor='rgb(43, 43, 43)',
                           showcountries=False,
                           showframe=False,
                           #framewidth=0,
                           #framecolor='rgb(30, 30, 30)',
                           coastlinecolor='rgb(43, 43, 43)',
                           showcoastlines=True,
                           showland=True,
                           showocean=True,
                           oceancolor='rgb(30, 30, 30)',
                           showlakes=True,
                           lakecolor='rgb(30, 30, 30)',
                           projection={'type': 'equirectangular'}),
                  dragmode=False,
                  margin=dict(autoexpand=False,
                              l=10, r=150, t=10, b=40
                              ),
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
                          x=0.90,
                          xanchor="right",
                          y=0.10,
                          yanchor="top",
                          bgcolor='rgb(30, 30, 30)',
                          font=dict(color='rgb(165, 149, 1)')
                      )
                  ]
                  )



    return go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)





# Run application
if __name__ == '__main__':
    app.run_server(debug=True)