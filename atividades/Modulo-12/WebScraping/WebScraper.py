import csv
from bs4 import BeautifulSoup
import requests

url = requests.get('https://scholar.google.com/scholar?q=python&hl=en&as_sdt=0,5').text

soup = BeautifulSoup(url, 'html.parser')
lista = soup.find_all('div', class_="gs_ri")

book = list()
authors = list()
journal = list()
year = list()
publisher = list()
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



with open('data_set.csv', 'w', newline='') as archive:
  writer = csv.writer(archive)
  writer.writerow(data.keys())
  for iteration in range(len(data.keys())):
    writer.writerow([value[iteration].strip() for value in data.values()])

