import csv
from bs4 import BeautifulSoup
import requests

url = requests.get('https://scholar.google.com/scholar?q=python&hl=en&as_sdt=0,5').text

soup = BeautifulSoup(url, 'html.parser')
lista = soup.find_all('div', class_="gs_ri")

book = authors = journal = year = publisher = []
data = dict()

for i in lista:
  book.append(i.find("h3", a_='').text.strip().replace('[PDF][PDF]', '').replace('[BOOK][B]', '').replace('[HTML][HTML]', ''))
  authors.append(i.find("div", class_="gs_a").text.split('-')[0])
  journal.append(i.find("div", class_="gs_a").text.split('-')[1])
  year.append(i.find("div", class_="gs_a").text.split("-")[1].strip().split()[0])
  publisher.append(i.find("div", class_="gs_a").text.split("-")[2].strip().split()[0])

data['Book'] = book
data['Authors'] = authors
data['Journal'] = journal
data['Year'] = year
data['Publisher'] = publisher

print(data)

# with open('data_set.csv','w',encoding='utf8b') as archive:
