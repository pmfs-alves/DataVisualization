import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

# DATAFRAMES
df_athletes = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'athlete_events')
df_participants = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'participants')

df_participants['Edition'] = df_participants['Edition'].astype(str)

df_countries = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\tops_countries.xlsx','Countries')

# -----------------------------------------------------------------------------
# CHOROPLETH
# -----------------------------------------------------------------------------
year=2000
team='Individual'
sport=[]

# FILTERING
def countries(year, sport, team):
    if (year == 1892) & (len(sport) == 0) & (team == 'both'):
        df = df_countries
    elif (year != 1892) & (len(sport) == 0) & (team == 'both'):
        df = df_countries.loc[df_countries['Year']==year,:]
    elif (year != 1892) & (len(sport) != 0) & (team == 'both'):
        df = df_countries.loc[(df_countries['Year']==year) & (df_countries['Sport'].isin(sport)),:]
    elif (year != 1892) & (len(sport) != 0) & (team != 'both'):
        df = df_countries.loc[(df_countries['Year']==year) & (df_countries['Sport'].isin(sport)) & (df_countries['Team Sport']==team),:]
    elif (year == 1892) & (len(sport) != 0) & (team == 'both'):
        df = df_countries.loc[df_countries['Sport'].isin(sport),:]  
    elif (year == 1892) & (len(sport) == 0) & (team != 'both'):
        df = df_countries.loc[df_countries['Team Sport']==team,:]
    elif (year == 1892) & (len(sport) != 0) & (team != 'both'):
        df = df_countries.loc[(df_countries['Sport'].isin(sport)) & (df_countries['Team Sport']==team),:]
    elif (year != 1892) & (len(sport) == 0) & (team != 'both'):
        df = df_countries.loc[(df_countries['Year']==year) & (df_countries['Team Sport']==team),:]
    
    df= df.groupby(by=['Country'])['Gold','Silver','Bronze','Total'].sum()
    df['Country'] = df.index
    df.reset_index(drop=True, inplace=True)
    
    df = df.merge(df_athletes[['ISO3','Country']], on='Country', how='left')
    df.drop_duplicates(inplace=True)
    
    df = df.merge(df_participants[['City','Country','Edition']], how='outer', on='Country')
    df.fillna('No host', inplace=True)
    
    df = df.groupby('Country').agg({'Gold':'first','Silver':'first','Bronze':'first','Total':'first',
                                   'ISO3':'first','City': ', '.join, 'Edition': ', '.join}).reset_index()
    
    return df
    

df = countries(year, sport, team)

# MAP

trace1 = go.Choropleth(locations=df['ISO3'],
                     locationmode='ISO-3',
                     z=df['Total'],
                     text=np.array(df),
                     name='Total',
                     hovertemplate="<b>%{text[0]}</b><br>" +
                                   "Host City: %{text[6]}<br>" +
                                   "Edition: %{text[7]}<br>" +
                                     "Total Number of Medals: %{text[4]:.0f}<br>"+
                                     "     Gold:  %{text[1]:.0f}"+
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
                       #showframe=False,
                       framewidth=0,
                       framecolor='rgb(30, 30, 30)',
                       coastlinecolor='rgb(43, 43, 43)',
                       showcoastlines=True,
                       showland=True,
                       showocean=True,
                       oceancolor='rgb(30, 30, 30)',
                       showlakes=True,
                       lakecolor='rgb(30, 30, 30)',                          
                       projection={'type': 'equirectangular'}),         
                  #autosize=False,
                  #width=1000,
                  #height=700,
                  margin=dict(autoexpand=False,
                              l=10,r=150,t=10,b=40
                           ),
                 paper_bgcolor='rgb(30, 30, 30)',
                 plot_bgcolor='rgb(30, 30, 30)',
             updatemenus=[
                go.layout.Updatemenu(
                    visible=True,
                    type='buttons',
                    direction="right",
                    active=-1,
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
                                     x=0, y=0, yref="paper", align="left",font=dict(color='white'))
                        ]
            )


map = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)

pyo.plot(map)

# -----------------------------------------------------------------------------
# LINE CHART
# -----------------------------------------------------------------------------

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
                                        
                                        tickvals=[1896,1904,1912,1920,1928,1936,1948,1956,1964,
                                                  1972,1980,1988,1996,2004,2012],
                                        dtick = 4,
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
                                       #tick0 = 0,
                                       dtick = 50,
                                       range=[0,250],
                                       ),         
                            autosize=False,
                            width=530,
                            height=400,
                            margin=dict(autoexpand=False,
                                        l=50,r=5,t=10,b=70
                                       ),
                            showlegend=False,
                            paper_bgcolor='rgba(0, 0, 0)',
                            plot_bgcolor='rgba(0, 0, 0)',
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

pyo.plot(line)

# -----------------------------------------------------------------------------
# AREA CHART
# ----------------------------------------------------------------------------- 

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
              plot_bgcolor='rgba(0, 0, 0)',
              )

area = go.Figure(data=[trace1, trace2], layout=layout)

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

pyo.plot(area)


# -----------------------------------------------------------------------------
# STACKED BAR FOR SPORTS
# -----------------------------------------------------------------------------

years=df_participants['Year']

df_participants['New Sports']=""
df_participants['Returning Sports']=""
df_participants['Maintained Sports']=""
df_participants['Lost Sports']=""

all_sports = []
previous_list=[]
for idx, x in enumerate(years):
    if (idx!=0):
        previous_list.extend(df_participants.at[idx-1,'New Sports'])
        previous_list.extend(df_participants.at[idx-1,'Returning Sports'])
        previous_list.extend(df_participants.at[idx-1,'Maintained Sports'])
        df_participants.at[idx, 'Lost Sports'] = [a for a in previous_list
                                                  if a not in df_athletes[
                                                      df_athletes['Year'] == x].Sport.unique().tolist()]

    if (idx == 0):
        df_participants.at[idx, 'New Sports'] = df_athletes[df_athletes['Year'] == years[0]].Sport.unique().tolist()
        df_participants.at[idx, 'Returning Sports'] = []
        df_participants.at[idx, 'Maintained Sports'] = []
        df_participants.at[idx, 'Lost Sports'] = []
    elif (idx == 1):
        df_participants.at[idx, 'New Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist() if a not in df_participants['New Sports'][idx - 1]]
        df_participants.at[idx, 'Returning Sports'] = []
        df_participants.at[idx, 'Maintained Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist() if a in df_participants['New Sports'][idx - 1]]
    else:
        df_participants.at[idx, 'New Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist() if a not in all_sports]
        df_participants.at[idx, 'Returning Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist()
                                                        if a not in df_participants['New Sports'][idx - 1] and a in all_sports and
                                                             a not in df_participants['Maintained Sports'][idx - 1] and a not in
                                                             df_participants['Returning Sports'][idx - 1]]
        df_participants.at[idx, 'Maintained Sports'] = [a for a in df_athletes[df_athletes['Year'] == x].Sport.unique().tolist()
                                                       if a in df_participants['New Sports'][idx - 1]
                                                       or a in df_participants['Returning Sports'][idx - 1]
                                                       or a in df_participants['Maintained Sports'][idx - 1]]

    previous_list=[]
    all_sports.extend(df_participants.at[idx,'New Sports'])

df_participants['New Sports_Count']=""
df_participants['Returning Sports_Count']=""
df_participants['Maintained Sports_Count']=""

for idx, x in enumerate(years):
    df_participants.at[idx,'New Sports_Count'] = len(df_participants.at[idx,'New Sports'])
    df_participants.at[idx,'Returning Sports_Count'] = len(df_participants.at[idx,'Returning Sports'])
    df_participants.at[idx,'Maintained Sports_Count'] = len(df_participants.at[idx,'Maintained Sports'])

for idx, x in enumerate(years):
    df_participants.at[idx,'New Sports'] = [' {0}'.format(elem) if idx!=0 else '{0}'.format(elem) for idx, elem in enumerate(df_participants.at[idx,'New Sports'])]
    df_participants.at[idx,'Returning Sports'] = [' {0}'.format(elem) if idx!=0 else '{0}'.format(elem) for idx, elem in enumerate(df_participants.at[idx,'Returned Sports'])]
    df_participants.at[idx,'Maintained Sports'] = [' {0}'.format(elem) if idx!=0 else '{0}'.format(elem) for idx, elem in enumerate(df_participants.at[idx,'Maintained Sports'])]
    df_participants.at[idx,'Lost Sports'] = [' {0}'.format(elem) if idx!=0 else '{0}'.format(elem) for elem in df_participants.at[idx, 'Lost Sports']]

for idx, x in enumerate(years):
    if df_participants.at[idx,'Lost Sports'] == []:
        df_participants.at[idx, 'Lost Sports'] = 0


layout= dict(xaxis=dict(title=dict(text="Year",
                                   font=dict(family='Arial',
                                             size=13,
                                             color='white',
                                           ),
                                   ),
                        showline=True,
                        showgrid=False,
                        showticklabels=True,
                        linecolor='white',
                        linewidth=2,
                        ticks='outside',
                         tickcolor='white',
                        range=[1894,2018],
                        tickfont=dict(
                                family='Arial',
                                size=12,
                                color='white',
                                ),
                        tickvals=[1896,1904,1912,1920,1928,1936,1948,1956,1964,
                                                  1972,1980,1988,1996,2004,2012],
                        dtick = 4,
                        tickangle=45
                        ),
              yaxis=dict(title=dict(text="Number of Sports",
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
                         tick0 = 0

                       ),
                     
              autosize=False,
              width=600,
              height=450,
              margin=dict(autoexpand=False,
                          l=50,r=10,t=10,b=70
                       ),
              showlegend=False,
              paper_bgcolor='rgba(0, 0, 0)',
              plot_bgcolor='rgba(0, 0, 0)',
              legend=dict(uirevision=False))


bar = go.Figure(data=[
    go.Bar(name='Maintained Sports', x=df_participants['Year'], y=df_participants['Maintained Sports_Count'],
           text=df_participants['Lost Sports'], marker=dict(color='rgb(0, 34, 102)', line_color='rgb(0, 34, 102)'),
           hovertemplate="<b>Maintained Sports:</b> %{y:.0f}<br><b>Lost Sports:</b> %{text}",
           hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(242, 242, 242)',
                                    font=dict(size=13,
                                              color='rgb(0, 0, 0)',
                                              ),
                                    namelength=0,
                                    )),

    go.Bar(x=df_participants['Year'], y=df_participants['Returning Sports_Count'], name='Returning Sports',
           text= df_participants['Returning Sports'], marker=dict(color='rgb(230, 230, 230)'),
           line=dict(color='rgb(230, 230, 230)'),
           hovertemplate="<b>Returning Sports:'</b> %{y:.0f}<br>%{text}", #Total Sports: %{text}<br>
           hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(242, 242, 242)',
                                    font=dict(size=13,
                                              color='rgb(0, 0, 0)',
                                              ),
                                    namelength=0,
                                    )),
    go.Bar(name='New Sports', x=df_participants['Year'], y=df_participants['New Sports_Count'],
           text=df_participants['New Sports'], marker=dict(color='rgb(244, 212, 77)'),#color='time',
           line=dict(color='rgb(244, 212, 77)'),
           hovertemplate="<b>New Sports:</b> %{y:.0f}<br>%{text}", #Total Sports: %{text}<br>
           hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(255, 89, 89)',
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
     textfont=dict(color="white", size=11),
    textposition="top center",
    showlegend=False,
    hoverinfo='skip',
    
))

pyo.plot(bar)



# -----------------------------------------------------------------------------
# Top 5 Winners
# -----------------------------------------------------------------------------

df = pd.read_excel('data/athlete_events.xlsx', sheet_name='athlete_events')

athletes_medals = df[['Name', 'Medal']]
athletes_medals['c'] = 1
a_m = athletes_medals.groupby(by=['Name', 'Medal']).c.sum()
a_m = a_m.to_frame().reset_index()

athletes_names = a_m.Name.unique()

athletes_names_ordered = a_m.groupby(by='Name').c.sum()
athletes_names_ordered = athletes_names_ordered.to_frame().reset_index()
athletes_names_ordered = athletes_names_ordered.sort_values(by=['c'], ascending=False)
top_5_winners = athletes_names_ordered.head()



# final_fig = make_subplots(rows=5, cols=1)
# i = 1
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
            series.append(go.Scatter(x=x, y=y, mode='markers',
                                     marker={'symbol': 'circle', 'size': 6, 'color': 'rgb(255, 215, 0)'},
                                     name=f'{medal} ({count})'))
        elif (medal == 'Silver'):
            series.append(go.Scatter(x=x, y=y, mode='markers',
                                     marker={'symbol': 'circle', 'size': 6, 'color': 'rgb(192, 192, 192)'},
                                     name=f'{medal} ({count})'))
        elif (medal == 'Bronze'):
            series.append(go.Scatter(x=x, y=y, mode='markers',
                                     marker={'symbol': 'circle', 'size': 6, 'color': 'rgb(205, 127, 50)'},
                                     name=f'{medal} ({count})'))

    fig = go.Figure(dict(data=series, figsize=[6, 6], layout=go.Layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False, showline=False, visible=False, showticklabels=False,
                   range=[0.5, 30]),
        yaxis=dict(showgrid=False, zeroline=False, showline=False, visible=False, showticklabels=False, tickvals=[1])
    )))
    fig.update_layout(showlegend=False,
                      autosize=False,
                      width=500,
                      height=190,
                      margin={'t': 0}
                      )
    # final_fig.append_trace(fig, i, 1)
    # i = i + 1
    fig.show()
    
# final_fig.show()


# -----------------------------------------------------------------------------
# Top 5 Countries
# -----------------------------------------------------------------------------

df = pd.read_excel('data/athlete_events.xlsx', sheet_name='athlete_events')

countries_medals = df[['Country', 'Medal']]
countries_medals['c'] = 1
c_m = countries_medals.groupby(by=['Country', 'Medal']).c.sum()
c_m = c_m.to_frame().reset_index()

countries_names = c_m.Country.unique()