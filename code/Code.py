import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

# DATAFRAMES
df_athletes = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'athlete_events')
df_participants = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'participants')

df_participants['Edition'] = df_participants['Edition'].astype(str)

medals_country = pd.DataFrame(data=df_athletes.groupby(["ISO3", "Medal"])["Medal"].count())
medals_country = medals_country.unstack(level=['Medal'])
medals_country.columns = medals_country.columns.droplevel()
medals_country['ISO3'] = medals_country.index
medals_country.reset_index(drop=True, inplace=True)
medals_country['Total'] = medals_country.iloc[:,0:3].sum(axis=1)

medals_country = medals_country.merge(df_athletes[['ISO3','City','Country','Edition','Year']], on='ISO3')
medals_country.drop_duplicates(inplace=True)

# -----------------------------------------------------------------------------
# CHOROPLETH
# -----------------------------------------------------------------------------
medals_country['Hosting_City'] = medals_country['City']
medals_country['Hosting_Edition'] = medals_country['Edition']
medals_country['Hosting_Year'] = medals_country['Year']

uniques = df_participants['ISO3'].unique().tolist()

medals_country.reset_index(drop=True, inplace=True)

row = 0
for i in medals_country['ISO3']:
    if i not in uniques:
        medals_country.loc[row, 'Hosting_City'] = 'No host'
        medals_country.loc[row, 'Hosting_Edition'] = 'No host'
        medals_country.loc[row, 'Hosting_Year'] = 'No host'
    
    row+=1
    
del row, i, uniques
    
medals_country.fillna(0, inplace=True)
customdata = df_participants[['ISO3','City','Edition','Year']].copy()


#map = go.Figure(data=go.Choropleth(locations=medals_country['ISO3'],
#                                   locationmode='ISO-3',
#                                   z=medals_country['Total'], # Gold, Silver, Bronze
#                                   text=np.array(medals_country),
#                                   customdata=np.array(customdata),
#                                   hovertemplate="<b>%{text[6]}</b><br><br>" +
#                                                 "Host City: %{customdata}<br>"
##                                               "Host City: %{customdata[1]}<br>" +
##                                               "Edition: %{customdata[2]}<br>" +
##                                               "Hosting Year: %{customdata[3]:.0f}<br>" +
#                                               "Total Number of Medals: %{text[4]:.0f}<br>" +
#                                               "    Gold: %{text[1]:.0f}<br>" +
#                                               "    Silver: %{text[2]:.0f}<br>" +
#                                               "    Bronze: %{text[0]:.0f}<br>",
#                                   hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
#                                                 bordercolor='rgb(242, 242, 242)',
#                                                 font=dict(size=15,
#                                                           color='rgb(0, 0, 0)',
#                                                           ),
#                                                 namelength=0,
#                                                ),
#                                   colorscale='fall',
#                                   colorbar={'title': 'Total Number<br>of Medals'}
#                                   ),
#                layout=dict(geo=dict(landcolor='rgb(255, 255, 255)',
#                                     showframe=False,
#                                     projection={'type': 'equirectangular'})
#                            )
#                )
#
#pyo.plot(map)

fig = go.Figure()

# Add Traces
fig.add_trace(go.Choropleth(locations=medals_country['ISO3'],
                             locationmode='ISO-3',
                             z=medals_country['Total'],
                             text=np.array(medals_country),
                             name='Total',
                             hovertemplate="<b>%{text[6]}</b><br>" +
                                             "Total Number of Medals: %{text[4]:.0f}<br>",
                             hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                             bordercolor='rgb(242, 242, 242)',
                                             font=dict(size=15,
                                                       color='rgb(0, 0, 0)',
                                                       ),
                                             namelength=0,
                                            ),
                             colorscale='fall',
                             colorbar={'title': '<b>Total Number<br>of Medals'}))
fig.add_trace(go.Choropleth(locations=medals_country['ISO3'],
                             locationmode='ISO-3',
                             z=medals_country['Gold'],
                             text=np.array(medals_country),
                             name='Gold',
                             hovertemplate="<b>%{text[6]}</b><br>" +
                                             "Total Number of Medals: %{text[4]:.0f}<br>" +
                                            "   Gold:  %{text[1]:.0f}",
                             hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                             bordercolor='rgb(242, 242, 242)',
                                             font=dict(size=15,
                                                       color='rgb(0, 0, 0)',
                                                       ),
                                             namelength=0,
                                            ),
                             colorscale='fall',
                             colorbar={'title': '<b>Total Number<br>of Golden Medals \n' }))

fig.add_trace(go.Choropleth(locations=medals_country['ISO3'],
                             locationmode='ISO-3',
                             z=medals_country['Silver'],
                             text=np.array(medals_country),
                             name='Silver',
                             hovertemplate="<b>%{text[6]}</b><br>" +
                                             "Total Number of Medals: %{text[4]:.0f}<br>" +
                                            "   Silver:  %{text[2]:.0f}",
                             hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                             bordercolor='rgb(242, 242, 242)',
                                             font=dict(size=15,
                                                       color='rgb(0, 0, 0)',
                                                       ),
                                             namelength=0,
                                             ),
                             colorscale='Geyser',
                             colorbar={'title': '<b>Total Number<br>of Silver Medals'}))

fig.add_trace(go.Choropleth(locations=medals_country['ISO3'],
                             locationmode='ISO-3',
                             z=medals_country['Bronze'],
                             text=np.array(medals_country),
                             name='Bronze',
                             hovertemplate="<b>%{text[6]}</b><br>" +
                                             "Total Number of Medals: %{text[4]:.0f}<br>" +
                                            "   Bronze:  %{text[0]:.0f}",
                             hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                             bordercolor='rgb(242, 242, 242)',
                                             font=dict(size=15,
                                                       color='rgb(0, 0, 0)',
                                                       ),
                                                       namelength=0,
                                            ),
                             colorscale='Geyser',
                             colorbar={'title': '<b>Total Number<br>of Bronze Medals'}))

fig.update_layout(geo=dict(landcolor='rgb(255, 255, 255)',
                    showframe=False,
                    projection={'type': 'equirectangular'})
           )

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            visible=True,
            type='buttons',
            direction="right",
            active=None,
            buttons=list([
                dict(args=[{"visible": [True, False, False, False]}],
                     label="Total",method="update"),
                dict(args=[{"visible": [False, True, False, False]}],
                     label="Gold",method="update"),
                dict(args=[{"visible": [False, False, True, False]}],
                     label="Silver",method="update"),
                dict(args=[{"visible": [False, False, False, True]}],
                     label="Bronze",method="update"),
            ]),
            showactive=True,
            x=0,
            xanchor="left",
            y=0,
            yanchor="top"
        )
    ])
                
fig.update_layout(
    annotations=[
        go.layout.Annotation(text="<b>Medals Type", showarrow=False,
                             x=0, y=0, yref="paper", align="left")
    ]
)

pyo.plot(fig)

# -----------------------------------------------------------------------------
# LINE CHART - DONE
# -----------------------------------------------------------------------------

line = go.Figure(data=go.Scatter(x=df_participants['Year'],
                                 y=df_participants['Countries'],
                                 mode="lines+markers",
                                 text=df_participants['Edition'],
                                 hovertemplate="<b>%{y:,.0f}</b> countries participated in the %{text} Summer Olympics",
                                 hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                                 bordercolor='rgb(242, 242, 242)',
                                                 font=dict(size=15,
                                                           color='rgb(0, 0, 0)',
                                                           ),
                                                 namelength=0,
                                                ),
                                 line=dict(color='cadetblue',
                                           width=3,
                                           dash='solid'),
                                 marker=dict(symbol="diamond",
                                             size=12, color='rgb(61, 92, 92)'),
                                 showlegend=False
                                 ),
                 layout=dict(title=dict(text="<b><i> Olympics getting Popular",
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
                                        tickfont=dict(
                                                family='Arial',
                                                size=14,
                                                color='rgb(0, 0, 0)',
                                                ),
                                        
                                        tickvals=df_participants['Year'].unique().tolist(),
                                        dtick = 4,
                                        tickangle=45,
                                        showspikes=True,
                                        spikecolor='rgb(179, 203, 203)'
                                        ),
                            yaxis=dict(title=dict(text="<b>Number of Countries",
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
                                       tick0 = 0,
                                       dtick = 50,
                                       ),
#                            autosize=False,
#                            margin=dict(autoexpand=False,
#                                        l=100,
#                                        r=20,
#                                        t=110,
#                                        ),
                            showlegend=False,
                            plot_bgcolor='white'
                            )
                 )

pyo.plot(line)

# -----------------------------------------------------------------------------
# LINE POINT CHART WITH NUMBER ON POINTS
# -----------------------------------------------------------------------------

point = go.Figure(data=go.Scatter(x=df_participants['Year'],
                                 y=df_participants['Sports'],
                                 mode="lines+markers+text",
                                 text=df_participants['Sports'],
                                 textposition="top center",
                                 textfont=dict(family="Arial",
                                               size=18,
                                               color="rgb(0, 0, 0)"),
                                 hovertemplate="In %{x:.0f} the Olympic Summer Games featured <b>%{y:,.0f}</b> different sports.",
                                 hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                                 bordercolor='rgb(242, 242, 242)',
                                                 font=dict(size=15,
                                                           color='rgb(0, 0, 0)',
                                                           ),
                                                 namelength=0,
                                                ),          
                                 line=dict(color='rgb(255, 159, 128)',
                                           width=3,
                                           dash='solid'),
                                 marker=dict(symbol=200,
                                             size=10, color='rgb(51, 51, 51)'),
                                 showlegend=False,
                                 ),
                 layout=dict(title=dict(text="<b><i> Even Sports need to qualify?",
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
                                        tickfont=dict(
                                                family='Arial',
                                                size=14,
                                                color='rgb(0, 0, 0)',
                                                ),
                                        tickvals=df_participants['Year'].unique().tolist(),
                                        dtick = 4,
                                        tickangle=45,
                                        showspikes=True,
                                        spikecolor='rgb(0, 0, 0)',
                                        spikethickness=2,
                                        ),
                              yaxis=dict(title=dict(text="<b>Number of Sports",
                                                   font=dict(family='Arial',
                                                             size=16,
                                                             color='rgb(0, 0, 0)',
                                                           ),
                                                   ),
                                       showgrid=True,
                                       showline=True,
                                       showticklabels=False,
                                       linecolor='rgb(0, 0, 0)',
                                       linewidth=2,
                                       ),
                            showlegend=False,
                            plot_bgcolor='white'
                            )
                 )

pyo.plot(point)

# -----------------------------------------------------------------------------
# AREA CHART - DONE
# -----------------------------------------------------------------------------

trace1 = go.Scatter(x=df_participants['Year'],
                    y=df_participants['Men'],
                    mode="lines+markers",
                    fill="tonexty", # "none" | "tozeroy" | "tozerox" | "tonexty" | "tonextx" | "toself" | "tonext"
                    fillcolor='rgb(179, 204, 204)',
                    stackgroup='one',
                    text=df_participants['Participants'],
                    hovertemplate="Total: %{text:.0f}<br>Men: %{y:.0f}",
                    hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(242, 242, 242)',
                                    font=dict(size=15,
                                              color='rgb(0, 0, 0)',
                                           ),
                                    namelength=0,
                                    ),          
                     line=dict(color='rgb(102, 153, 153)',
                               width=3,
                               dash='solid',
                               shape="linear"), #"linear" | "spline"
                     marker=dict(symbol='x-dot',
                                 size=5, color='rgb(31, 46, 46)'),
                     showlegend=False,
                     )
                                             
trace2 = go.Scatter(x=df_participants['Year'],
                    y=df_participants['Women'],
                    mode="lines+markers",
                    fill="tonexty", # "tozeroy" |"tonexty" | "tonextx" | "toself" | "tonext"
                    fillcolor='rgb(255, 217, 179)',
                    stackgroup='one',
                    text=df_participants['Participants'],
                    hovertemplate="Total: %{text:.0f}<br>Women: %{y:.0f}",
                    hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
                                    bordercolor='rgb(242, 242, 242)',
                                    font=dict(size=15,
                                              color='rgb(0, 0, 0)',
                                              ),
                                    namelength=0,
                                    ),          
                    line=dict(color='rgb(255, 191, 128)',
                              width=3,
                              dash='solid',
                              shape="linear"), #"linear" | "spline"
                    marker=dict(symbol='x-dot',
                                size=5, color='rgb(153, 77, 0)'),
                    showlegend=False,
                    )
                     
layout= dict(title=dict(text="<b><i> Sports is only for Men?",
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
                        tickfont=dict(
                                family='Arial',
                                size=14,
                                color='rgb(0, 0, 0)',
                                ),
                        tickvals=df_participants['Year'].unique().tolist(),
                        dtick = 4,
                        tickangle=45,
                        showspikes=True,
                        spikecolor='rgb(0, 0, 0)',
                        spikethickness=2,
                        ),
              yaxis=dict(title=dict(text="<b>Number of Athletes",
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
                         tick0 = 0,
                         range=[0,12000],
                         side='right',
                       ),
            showlegend=False,
            plot_bgcolor='white'
            )
                                           
area = go.Figure(data=[trace1, trace2], layout=layout) 

pyo.plot(area)