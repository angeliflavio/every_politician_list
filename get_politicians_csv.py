import requests
import json
import pandas as pd

#download list of countires JSON
countries_file=requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json').text
countries_file=json.loads(countries_file)

#create the empty dataframe that will store the list of politicians and their details
df=pd.DataFrame()    #initialize master data frame
column_names=['Country','Legislature','Politicians', 'URLjson', 'Politician','Link']

#loop through countries json
for x in range(len(countries_file)-1):
    name=countries_file[x]['name']
    print(x,name)
    for z in range(len(countries_file[x]['legislatures'])):         #loop through the countries
                       legislatures_name=countries_file[x]['legislatures'][z]['name']
                       person_count=countries_file[x]['legislatures'][z]['person_count']
                       url_json=countries_file[x]['legislatures'][z]['popolo_url']
                       country=requests.get(url_json).text
                       country=json.loads(country)
                       for y in range(len(country['persons'])-1):       #loop through the politicians
                           politician=country['persons'][y]['name']
                           try:
                               politician_link=country['persons'][y]['links'][0]['url']
                           except:
                               politician_link='no link'
                           details=[[name, legislatures_name, person_count, url_json, politician, politician_link]]
                           df2=pd.DataFrame(details, columns=column_names)  #dataframe with politician's details to be appended
                           df=df.append(df2, ignore_index=True)   #append to the master data frame

#print brief summary describing the data downloaded
print('Downloaded %d politicians.' %(len(df.index)))                   #number of politicians
print('Data from %d countries.' %(len(df.Country.unique())))          #number of countries

#write data into a csv file
df.to_csv('list_politicians.csv', sep=',', index_label='index')
print('Data saved to csv file (list_politicians.csv).')