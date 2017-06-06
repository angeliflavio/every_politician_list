import requests
import json
import xlsxwriter as xl

countries_file=requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json').text
countries_file=json.loads(countries_file)

#create an excel file to store the list of politicians
workbook=xl.Workbook('pep_politicians.xlsx')
worksheet=workbook.add_worksheet()
worksheet.write(0,0,'country')
worksheet.write(0,1,'legislatures name')
worksheet.write(0,2,'person count')
worksheet.write(0,3,'url json')
worksheet.write(0,4,'politician name')
worksheet.write(0,5,'politician link')
row=1

#loop through countries json
for x in range(len(countries_file)-1):
    name=countries_file[x]['name']
    print(x,name)
    for z in range(len(countries_file[x]['legislatures'])):
                       legislatures_name=countries_file[x]['legislatures'][z]['name']
                       person_count=countries_file[x]['legislatures'][z]['person_count']
                       url_json=countries_file[x]['legislatures'][z]['popolo_url']
                       country=requests.get(url_json).text
                       country=json.loads(country)
                       for y in range(len(country['persons'])-1):
                           politician=country['persons'][y]['name']
                           try:
                               politician_link=country['persons'][y]['links'][0]['url']
                           except:
                               politician_link='no link'
                           worksheet.write(row,0,name)
                           worksheet.write(row,1,legislatures_name)
                           worksheet.write(row,2,person_count)
                           worksheet.write(row,3,url_json)
                           worksheet.write(row,4,politician)
                           worksheet.write(row,5,politician_link)
                           row+=1
workbook.close()


#to be done
#add date of updating
#countdown
#cell limit in Excel, set the rows number to 80,000





