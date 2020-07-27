from bs4 import BeautifulSoup
import requests
import csv
page = requests.get("http://www.cpcb.gov.in/CAAQM/frmCurrentDataNew.aspx?StationName=IDA%20Pashamylaram&StateId=30&CityId=7")
print(page.status_code) #if it is 200 then success
soup = BeautifulSoup(page.content, 'html.parser')
c=soup.find("table")
rows = c.find_all(id='Td1')
pollution = {'date':0,'time':0,'Nitric Oxide':0,'Nitrogen Dioxide':0,'Oxides of Nitrogen':0,'Sulphur Dioxide':0,'Carbon Monoxide':0,'OZONE':0,'PM2.5':0, 'PM10':0,'Ammonia':0, 'Rack Temperature':0, 'Ambient Temperature':0, 'Relative Humidity':0,'Wind Speed':0,'Wind Direction':0, 'Solar Radiation':0,'Bar Pressure':0,'Benzene':0,'Toluene':0,'Xylene':0}
data =[]
for td in rows[0].find_all('td'):
    a = td.text
    data.append(a)
pollution['date'] = data[8]
pollution['time'] = data[9]
pollution['Nitric Oxide'] = data[10]+' '+data[11]
pollution['Nitrogen Dioxide'] = data[17]+' '+data[18]
pollution['Oxides of Nitrogen'] = data[24]+' '+data[25]
pollution['Sulphur Dioxide'] = data[31]+' '+data[32]
pollution['Carbon Monoxide'] = data[38]+' '+data[39]
pollution['Ozone'] = data[45]+' '+data[46]
pollution['PM2.5'] = data[52]+ ' '+data[53]
pollution['PM10'] = data[59]+' '+data[60]
pollution['Ammonia'] = data[66]+' '+data[67]
pollution['Rack Temperature'] = data[73]+' '+data[74]
pollution['Ambient Temperature'] = data[80]+' '+data[81]
pollution['Relative Humidity'] = data[87]+' '+data[88]
pollution['Wind Speed'] = data[94]+' '+data[95]
pollution['Vertical Wind Speed'] = data[101]+' '+data[102]
pollution['Wind Direction'] = data[108]+' '+data[109]
pollution['Solar Radiation'] = data[115]+' '+data[116]
pollution['Bar Pressure'] = data[122]+' '+data[123]
pollution['Rain Fall'] = data[129]+' '+data[130]
pollution['Benzene'] = data[136]+' '+data[137]
pollution['Toluene'] = data[143]+' '+data[144]
pollution['Xylene'] = data[150]+' '+data[151]

"""for key, value in pollution.items():
    print(f'{key}:{value}')"""

csv_file = 'IDA Pashamylaram, Hyderabad.csv'

print(pollution)

with open(csv_file,'a') as f:
    w = csv.DictWriter(f,pollution.keys(),)
    #w.writeheader()
    w.writerow(pollution)
