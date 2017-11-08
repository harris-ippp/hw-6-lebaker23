#!/usr/bin/env python
#Worked with Lauren Casillas on this hw

from bs4 import BeautifulSoup as bs
import requests

resp = requests.get("URL")
soup = bs(resp.content, "html.parser")

#Only want nested objects under election item class
x = soup.find_all("tr",{"class":"election_item})

#Get contents of each id tag, makea list of contents
ids = []
for tag in x:
  ids.append(tag.get("id"))
ids = [x.split("-")[2] for x in ids] #Split on dash and only take actual ID number

#Only want nested objects under year class
years = soup.find_all("td",{"class":"year"})
years = [x.text for x in years] #Strip the surrounding HTML to leave just year

#Put years and IDs together in a list
YEARS_IDS= list(zip(years, ids))

#Write to file
with open("ELECTION_ID.txt", "w") as f:
    f.write('\n'.join('{} {}'.format(x[0],x[1]) for x in YEARS_IDS))
