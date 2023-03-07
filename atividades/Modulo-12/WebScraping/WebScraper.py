import csv
from bs4 import BeautifulSoup
import requests

url = requests.get('https://scholar.google.com/scholar?q=python&hl=en&num=20&as_sdt=0,5').text

soup = BeautifulSoup(url, 'html.parser')
lista = soup.find_all('div', class_="gs_ri")

datalist = list()
data = dict()

for i in lista:
  data['Book'] = i.find("h3", a_='').text.strip().replace('[PDF][PDF]', '').replace('[BOOK][B]', '').replace('[HTML][HTML]', '')
  data['Authors'] = i.find("div", class_="gs_a").text.split('-')[0]
  data['Journal'] = i.find("div", class_="gs_a").text.split('-')[1]
  data['Year'] = i.find("div", class_="gs_a").text.split("-")[1].strip().split()[0]
  data['Publisher'] = i.find("div", class_="gs_a").text.split("-")[2].strip().split()[0]

  datalist.append(data.copy())
  data.clear()

fields = ['Book','Authors','Journal','Year','Publisher']
with open('data_set.csv', 'a', newline='') as archive:
  writer = csv.DictWriter(archive, fieldnames=fields)
  writer.writeheader()
  writer.writerows(datalist)

