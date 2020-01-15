import pandas as pd
import numpy as np
from collections import Counter

# TOP COUNTRIES DATAFRAME

df_athletes = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'athlete_events')
df_participants = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\athlete_events.xlsx', 'participants')


countries_medals = df_athletes[['Country','Medal','Sport','Team Sport','Year']]
countries_medals['c'] = 1

medals_country= countries_medals.groupby(by=['Country','Medal','Year','Sport','Team Sport']).c.sum()
medals_country = medals_country.to_frame().reset_index()
temp = medals_country[['Country', 'Year','Sport','Team Sport']]
medals_country.drop(columns=['Country','Year'], inplace=True)
medals_country = medals_country.pivot(index=medals_country.index,columns='Medal')['c']
medals_country.fillna(0, inplace=True)

medals_country = medals_country.merge(temp, how='outer', left_index=True, right_index=True)

def count_rows_same_country(df):
    '''Check if rows are the same with different values in Gold, Silver, Bronze.'''
    
    contador = Counter(df['concat'].tolist())

    new_dict = {}
    for key, value in contador.items():
        if value > 1:
            new_dict.update({key:value})
    return new_dict

medals_country['Year'] = medals_country['Year'].astype(str)
medals_country['concat'] = medals_country[['Country','Year','Sport','Team Sport']].apply(lambda x: '_'.join(x), axis=1)


j=0
new=pd.DataFrame(columns=['Country','Gold','Silver','Bronze','Year', 'Sport','Team Sport'])
for idx,i in enumerate(medals_country['concat']):
    new.loc[j,'Country'] = medals_country.loc[idx,'Country']
    new.loc[j,'Gold'] = medals_country[medals_country['concat'] == i].Gold.sum() 
    new.loc[j,'Silver'] = medals_country[medals_country['concat'] == i].Silver.sum() 
    new.loc[j,'Bronze'] = medals_country[medals_country['concat'] == i].Bronze.sum() 
    new.loc[j,'Year'] = medals_country.loc[idx,'Year']
    new.loc[j,'Sport'] = medals_country.loc[idx,'Sport']
    new.loc[j,'Team Sport'] = medals_country.loc[idx,'Team Sport']
    j+=1

new.drop_duplicates(inplace=True) 

new['concat'] = new[['Country','Year','Sport','Team Sport']].apply(lambda x: '_'.join(x), axis=1)
count_rows_same_country(new)

new.drop(columns='concat', inplace=True)

new['Total'] = new['Bronze'] + new['Gold'] + new['Silver']


# PUT ISO3, CITY, YEAR, EDITION, SPORT, INDIVIDUAL

new = new.merge(df_athletes[['ISO3','Country']], on='Country', how='left')
new.drop_duplicates(inplace=True)

new['Year'] = new['Year'].astype(str)
df_participants['Year'] = df_participants['Year'].astype(str)
new = new.merge(df_participants[['City','Country','Year','Edition']], how='outer', on=['Country','Year'])
new.fillna('No host', inplace=True)

new.to_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\tops_countries.xlsx', sheet_name='Countries')

# TOTALS DATAFRAME

df_countries = pd.read_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\tops_countries.xlsx', 'Countries')

temp= df_countries[['Country','Sport','Team Sport','Gold','Silver','Bronze']]

temp['concat'] = temp[['Country','Sport','Team Sport']].apply(lambda x: '_'.join(x), axis=1)

j=0
totals=pd.DataFrame(columns=['Country','Sport','Team Sport','Gold','Silver','Bronze'])
for idx,i in enumerate(temp['concat']):
    totals.loc[j,'Country'] = temp.loc[idx,'Country']
    totals.loc[j,'Sport'] = temp.loc[idx,'Sport']
    totals.loc[j,'Team Sport'] = temp.loc[idx,'Team Sport']
    totals.loc[j,'Gold'] = temp[temp['concat'] == i].Gold.sum() 
    totals.loc[j,'Silver'] = temp[temp['concat'] == i].Silver.sum() 
    totals.loc[j,'Bronze'] = temp[temp['concat'] == i].Bronze.sum()
    j+=1

totals.drop_duplicates(inplace=True) 

totals['Total'] = totals['Bronze'] + totals['Gold'] + totals['Silver']

# PUT ISO3, CITY, YEAR, EDITION, SPORT, INDIVIDUAL

totals = totals.merge(df_athletes[['ISO3','Country']], on='Country', how='left')
totals.drop_duplicates(inplace=True)

totals = totals.merge(df_participants[['City','Country','Edition']], how='outer', on='Country')
totals.fillna('No host', inplace=True)

totals.to_excel(r'C:\Users\TITA\OneDrive\Faculdade\2 Mestrado\1º semestre\Data Visualization\Project\DataVisualization\code\data\total_countries.xlsx', sheet_name='Total')
