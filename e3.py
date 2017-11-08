#!/usr/bin/env python
#Worked with Elayne Stecher on this hw

import requests
import pandas as pd
import matplotlib as plt

df_list=[]
for line in open('ELECTION_ID.txt'):
    x = line.rstrip().split(' ')
    if len(x) == 2:
        years = x[0]
        file_name = 'president_general_{}.csv'.format(years)
        header = pd.read_csv(file_name,nrows=1).dropna(axis=1)
        df = pd.read_csv(file_name,index_col=0,thousands=",",skiprows=[1])
        df.rename(inplace=True,columns=header.iloc[0].to_dict())
        df.dropna(inplace=True,axis=1)
        #Only care about first 4 counties
        df = df.loc[['Accomack County','Albemarle County',
                     'Alexandria City','Alleghany County'],
                    ['Democratic','Republican','Total Votes Cast']]
        #Making Republican Share quotient
        df['Republican Share'] = df['Republican']/df['Total Votes Cast']
        df["Year"] = years
        df_list.append(df)
#Putting it all together
df = pd.concat(df_list)
df = df.reset_index()

#Accomack plot
mask_accomack = df["County/City"] == "Accomack County"
accomack = df[mask_accomack]
fig, ax = plt.subplots()
x = accomack["Year"]
y = accomack["Republican Share"]
ax.plot(x,y)
fig.suptitle('Accomack County')
ax.set_xlabel('Year')
ax.set_ylabel('Republican Share')
plt.draw()

#Albemarle plot
mask_albemarle = df["County/City"] == "Albemarle County"
albemarle = df[mask_albemarle]
fig, ax = plt.subplots()
x = albemarle["Year"]
y = albemarle["Republican Share"]
ax.plot(x,y)
fig.suptitle('Albemarle County')
ax.set_xlabel('Year')
ax.set_ylabel('Republican Share')
plt.draw()

#Alexandria plot
mask_alexandria = df["County/City"] == "Alexandria County"
alexandria = df[mask_alexandria]
fig, ax = plt.subplots()
x = alexandria["Year"]
y = alexandria["Republican Share"]
ax.plot(x,y)
fig.suptitle('Alexandria County')
ax.set_xlabel('Year')
ax.set_ylabel('Republican Share')
plt.draw()

#Alleghany plot
mask_alleghany = df["County/City"] == "Alleghany County"
alleghany = df[mask_alleghany]
fig, ax = plt.subplots()
x = alleghany["Year"]
y = alleghany["Republican Share"]
ax.plot(x,y)
fig.suptitle('Alleghany County')
ax.set_xlabel('Year')
ax.set_ylabel('Republican Share')
plt.draw()
