import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go

# DATAFRAMES
df_athletes = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'athlete_events')
df_participants = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'participants')

medals_country = pd.DataFrame(data=df_athletes.groupby(["ISO3", "Medal"])["Medal"].count())
medals_country = medals_country.unstack(level=['Medal'])
medals_country.columns = medals_country.columns.droplevel()
medals_country['ISO3'] = medals_country.index
medals_country.reset_index(drop=True, inplace=True)
medals_country['Total'] = medals_country.iloc[:,0:3].sum(axis=1)

df_athletes = df_athletes.merge(medals_country, on='ISO3')

# -----------------------------------------------------------------------------
# CHOROPLETH
# -----------------------------------------------------------------------------

df_athletes['text'] = 'Country: ' + df_athletes['Country'] + '<br>' + \
                      'Host City: ' + df_athletes['City'] + '<br>' + \
                      'Edition ' + df_athletes['Edition'] + '<br>' + \
                      'Hosting Year: ' + df_athletes['Year'].astype(str) + '<br>' + \
                      '  ' + '<br>' + \
                      'Total Number of Medals ' + df_athletes['Total'].astype(int).astype(str) + '<br>' + \
                      '    Gold: ' + df_athletes['Gold'].astype(str) + '<br>' + \
                      '    Silver: ' + df_athletes['Silver'].astype(str) + '<br>' + \
                      '    Bronze: ' + df_athletes['Bronze'].astype(str)

map = go.Figure(data=go.Choropleth(locations=df_athletes['ISO3'],
                                   locationmode='ISO-3',
                                   z=df_athletes['Total'], # Gold, Silver, Bronze
                                   text=[zval for zval in df_athletes['Country']],
                                   hovertemplate="<b>%{text}</b><br><br>" +
                                               "Host City: {df_athletes['City']}<br>" +
                                               "Edition: {df_athletes['Edition']}<br>" +
                                               "Hosting Year: {df_athletes['Year'].astype(str)}<br>" +
                                               "Total Number of Medals: {df_athletes['Total'].astype(int).astype(str)}<br>" +
                                               "    Gold: {df_athletes['Gold'].astype(str)}<br>" +
                                               "    Silver: {df_athletes['Silver'].astype(str)}<br>" +
                                               "    Bronze: {df_athletes['Bronze'].astype(str)}<br>" +
                                               "<extra></extra>",
                                   hovertext=df_athletes['text'],
                                   hoverinfo='text',
                                   colorscale='fall',
                                   colorbar={'title': 'Total Number<br>of Medals'}
                                   ),
                layout=dict(geo=dict(landcolor='rgb(255, 255, 255)',
                                     showframe=False,
                                     projection={'type': 'equirectangular'})
                            )
                )

pyo.plot(map)

fig = go.Figure()

# Add Traces
fig.add_trace(
    go.Choropleth(locations=df_athletes['ISO3'],
                  locationmode='ISO-3',
                  z=df_athletes['Total'],
                  name='Total',
                  hovertemplate="<b>%{df_athletes['Country']}</b><br><br>" +
                                "Host City: {df_athletes['City']}<br>" +
                                "Edition: {df_athletes['Edition']}<br>" +
                                "Hosting Year: {df_athletes['Year'].astype(str)}<br>" +
                                "Total Number of Medals: {df_athletes['Total'].astype(int).astype(str)}<br>" +
                                "    Gold: {df_athletes['Gold'].astype(str)}<br>" +
                                "    Silver: {df_athletes['Silver'].astype(str)}<br>" +
                                "    Bronze: {df_athletes['Bronze'].astype(str)}<br>" +
                                "<extra></extra>",
                  colorscale='fall',
                  colorbar={'title': 'Total Number<br>of Medals'}))
fig.add_trace(
    go.Choropleth(locations=df_athletes['ISO3'],
                  locationmode='ISO-3',
                  z=df_athletes['Gold'],
                  name='Gold',
                  hovertemplate="<b>%{df_athletes['Country']}</b><br><br>" +
                                "Host City: {df_athletes['City']}<br>" +
                                "Edition: {df_athletes['Edition']}<br>" +
                                "Hosting Year: {df_athletes['Year'].astype(str)}<br>" +
                                "Total Number of Medals: {df_athletes['Total'].astype(int).astype(str)}<br>" +
                                "    Gold: {df_athletes['Gold'].astype(str)}<br>" +
                                "    Silver: {df_athletes['Silver'].astype(str)}<br>" +
                                "    Bronze: {df_athletes['Bronze'].astype(str)}<br>" +
                                "<extra></extra>",
                  colorscale='fall',
                  colorbar={'title': 'Total Number<br>of Golden Medals \n' }))

fig.add_trace(
    go.Choropleth(locations=df_athletes['ISO3'],
                  locationmode='ISO-3',
                  z=df_athletes['Silver'],
                  name='Silver',
                  hovertemplate="<b>%{df_athletes['Country']}</b><br><br>" +
                                "Host City: {df_athletes['City']}<br>" +
                                "Edition: {df_athletes['Edition']}<br>" +
                                "Hosting Year: {df_athletes['Year'].astype(str)}<br>" +
                                "Total Number of Medals: {df_athletes['Total'].astype(int).astype(str)}<br>" +
                                "    Gold: {df_athletes['Gold'].astype(str)}<br>" +
                                "    Silver: {df_athletes['Silver'].astype(str)}<br>" +
                                "    Bronze: {df_athletes['Bronze'].astype(str)}<br>" +
                                "<extra></extra>",
                  colorscale='fall',
                  colorbar={'title': 'Total Number<br>of Silver Medals'}))

fig.add_trace(
    go.Choropleth(locations=df_athletes['ISO3'],
                  locationmode='ISO-3',
                  z=df_athletes['Bronze'],
                  name='Bronze',
                  hovertemplate="<b>%{df_athletes['Country']}</b><br><br>" +
                                "Host City: {df_athletes['City']}<br>" +
                                "Edition: {df_athletes['Edition']}<br>" +
                                "Hosting Year: {df_athletes['Year'].astype(str)}<br>" +
                                "Total Number of Medals: {df_athletes['Total'].astype(int).astype(str)}<br>" +
                                "    Gold: {df_athletes['Gold'].astype(str)}<br>" +
                                "    Silver: {df_athletes['Silver'].astype(str)}<br>" +
                                "    Bronze: {df_athletes['Bronze'].astype(str)}<br>" +
                                "<extra></extra>",
                  colorscale='fall',
                  colorbar={'title': 'Total Number<br>of Bronze Medals'}))

fig.update_layout(
    updatemenus=[
        go.layout.Updatemenu(
            visible=True,
            type='buttons',
            #active=0,
            buttons=list([
                dict(label="Total",
                     method="update"),
                dict(label="Gold",
                     method="update"),
                dict(label="Silver",
                     method="update"),
                dict(label="Bronze",
                     method="update"),
            ]),
        )
    ])

pyo.plot(fig)

# -----------------------------------------------------------------------------
# LINE CHART
# -----------------------------------------------------------------------------

#temp = df_participants.copy()
#temp['Year'] = temp['Year'].astype(str)
#temp['Countries'] = temp['Countries'].astype(str)
#temp['concat'] = temp[['Year', 'Countries']].apply(lambda x: '<br>'.join(x), axis=1)

line = go.Figure(data=go.Scatter(x=df_participants['Year'],
                                 y=df_participants['Countries'],
                                 mode="lines+markers",
#                                 text=[val for val in df_participants['Countries']],
#                                 hoverinfo='text',
                                 hovertemplate="<b>%{y:,.0f}</b> different countries participated in the Olympic Summer Games of %{x:.0f}.",
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
                              yaxis=dict(title=dict(text="<b>Number of Countries",
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
# AREA CHART
# -----------------------------------------------------------------------------

trace1 = go.Scatter(x=df_participants['Year'],
                    y=df_participants['Men'],
                    mode="lines+markers",
                    fill="tozeroy", # "none" | "tozeroy" | "tozerox" | "tonexty" | "tonextx" | "toself" | "tonext"
                    fillcolor='rgb(255, 159, 128)'
#                    text=df_participants['Sports'],
#                    textposition="top center",
#                    textfont=dict(family="Arial",
#                                   size=18,
#                                   color="rgb(0, 0, 0)"),
#                     hovertemplate="In %{x:.0f} the Olympic Summer Games featured <b>%{y:,.0f}</b> different sports.",
#                     hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
#                                     bordercolor='rgb(242, 242, 242)',
#                                     font=dict(size=15,
#                                               color='rgb(0, 0, 0)',
#                                               ),
#                                     namelength=0,
#                                    ),          
                     line=dict(color='rgb(255, 159, 128)',
                               width=3,
                               dash='solid',
                               shape="spline"), #"linear" | "spline" | "hv" | "vh" | "hvh" | "vhv" 
                     marker=dict(symbol=200,
                                 size=10, color='rgb(51, 51, 51)'),
                     showlegend=False,
                     )
                                             
trace2 = go.Scatter(x=df_participants['Year'],
                    y=df_participants['Women'],
                    mode="lines+markers",
                    fill="tozeroy", # "none" | "tozeroy" | "tozerox" | "tonexty" | "tonextx" | "toself" | "tonext"
                    fillcolor='rgb(255, 159, 128)'
#                    text=df_participants['Sports'],
#                    textposition="top center",
#                    textfont=dict(family="Arial",
#                                   size=18,
#                                   color="rgb(0, 0, 0)"),
#                     hovertemplate="In %{x:.0f} the Olympic Summer Games featured <b>%{y:,.0f}</b> different sports.",
#                     hoverlabel=dict(bgcolor='rgb(242, 242, 242)',
#                                     bordercolor='rgb(242, 242, 242)',
#                                     font=dict(size=15,
#                                               color='rgb(0, 0, 0)',
#                                               ),
#                                     namelength=0,
#                                    ),          
                     line=dict(color='rgb(255, 159, 128)',
                               width=3,
                               dash='solid',
                               shape="spline"), #"linear" | "spline" | "hv" | "vh" | "hvh" | "vhv" 
                     marker=dict(symbol=200,
                                 size=10, color='rgb(51, 51, 51)'),
                     showlegend=False,
                     )
                     
layout= layout=dict(title=dict(text="<b><i> Even Sports need to qualify?",
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
                                tick0 = 1896,
                                dtick = 4,
                                nticks=14,
                                tickangle=45,
                                showspikes=True,
                                spikecolor='rgb(0, 0, 0)',
                                spikethickness=2,
                                ),
                      yaxis=dict(title=dict(text="<b>Number of Countries",
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

pyo.plot(area)