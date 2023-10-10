import pandas as pd
import psycopg2 as pg
import csv as c
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import scipy.stats as stats
import mysql as sq
import os

list1 = pd.read_csv("data/spreadspoke_scores.csv")
Shape= list1.shape
print(Shape)
list2= list1.drop(['schedule_date',
          'stadium','stadium_neutral','weather_temperature',
          'weather_wind_mph','weather_humidity','weather_detail'],axis=1)
list3 = pd.DataFrame(list2)
list3.rename(columns ={'schedule_week': 'Game','schedule_season':'Year', 'over_under_line': 'OverUnder'
                       ,'spread_favorite': 'Spread', 'schedule_playoff': 'PostSeason'
                       , 'team_home': 'Home_Team', 'score_home':'Home_Score'
                       ,'score_away':'Away_Score','team_away': 'Away_Team'
                       ,'team_favorite_id':'Odds_Favorite'  }, inplace = True)
list4 = list3.dropna()
list5 = list4[list4['Year']>1990]
list6 = list5[list5['Game']== 'Superbowl']            
shape = list6.shape
print(shape)
print(list6)

spread_df= list6.loc[:, ['Year', 'Spread']]
spread = (list6['Spread'] == list6['Spread'].max()) | (list6['Spread'] == list6['Spread'].min())
print(f'\n{spread_df[spread]}')

overunder_df= list6.loc[:, ['Year', 'OverUnder']]
overunder= (list6['OverUnder'] == list6['OverUnder'].max()) | (list6['OverUnder'] == list6['OverUnder'].min())
print(f'\n{overunder_df[overunder]}')

home_df= list6.loc[:, ['Year', 'Home_Score']]
home = (list6['Home_Score'] == list6['Home_Score'].max()) | (list6['Home_Score'] == list6['Home_Score'].min())
print(f'\n{home_df[home]}')

away_df= list6.loc[:, ['Year', 'Away_Score']]
away = (list6['Away_Score'] == list6['Away_Score'].max()) | (list6['Away_Score'] == list6['Away_Score'].min()) 
print(f'\n{away_df[away]}')

list7 =list6.sort_values(by="Spread", ascending=True)
list7.plot(x="Year", kind="bar", color=['red', 'blue','orange'],rot=90, fontsize='50',figsize = (75,50))

x= list6['Home_Score']
y= list6['Away_Score']
s= list6['Spread']
o= list6['Odds_Favorite']
cont= (x+y)
cont.median()
s.median()
x.mean()
y.mean()

spreads_df =list7.loc[:,['Spread', 'OverUnder', 'Home_Score', 'Away_Score']]
sns.heatmap(spreads_df.corr(), annot=True, cmap=sns.diverging_palette(220,10,sep=1,n=30),vmin=-1,vmax=1)

fig, ax = plt.subplots(2,2, figsize=(50, 20))
sns.histplot(list7['Spread'], bins=10, kde=False, ax = ax[0,0])
sns.histplot(list7['OverUnder'], bins=10, kde=False, ax = ax[0,1])
sns.histplot(list7['Home_Score'], bins=10, kde=False, ax = ax[1,0])
sns.histplot(list7['Away_Score'], bins=10, kde=False, ax = ax[1,1])

fig, ax = plt.subplots(figsize=(30,20))
sns.boxplot(list7.loc[:, ['Spread','Home_Score','Away_Score','OverUnder']])
fig, ax = plt.subplots(figsize=(20, 8))
sns.violinplot(list7.loc[:,['Spread','OverUnder', 'Home_Score', 'Away_Score']])