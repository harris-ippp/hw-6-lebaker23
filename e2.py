#!/usr/bin/env python
#Worked with Lauren Casillas on this hw

import requests

#Creating empty lists
ids = []
years = []

#Take out ids and years from txt file
with open("ELECTION_ID.txt") as f:
  for line in f.readlines():
    ids.append(line.split(" ")[1])
    years.append(line.split(" ")[0])
ids = [x.split("\n")[0] for x in ids]


#Got locked out of API
#for x in years:
#    for x in ids:
#        resp = requests.get("http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(x for x in ids))
#    file_name = x +".csv"
#    with open(file_name, "w") as out:
#        out.write(resp.text)

for x in range(len(years)):
    file_name = 'president_general_{}.csv'.format(years[x])
    url = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'.format(ids[x])
    resp = requests.get(url)
    with open(file_name, "w") as out:
        out.write(resp.text)
