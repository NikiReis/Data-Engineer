from bs4 import BeautifulSoup
import requests

data = requests.get('https://scholar.google.com/scholar?q=python&hl=en&as_sdt=0,5').text

soup = BeautifulSoup(data, 'html.parser')
lista = soup.find_all('div', class_="gs_ri")

datalist = []
newdata = {

}
for i in lista:

  newdata['book'] = i.find("h3", a_='').text.strip().replace('[PDF][PDF]', '').replace('[BOOK][B]', '').replace('[HTML][HTML]', '')
  newdata['authors'] = i.find("div", class_="gs_a").text.split('-')[0]
  newdata['journal'] = i.find("div", class_="gs_a").text.split('-')[1]
  newdata['year'] = publisher = i.find("div", class_="gs_a").text.split("-")[1].strip().split()[0]
  newdata['publisher'] = i.find("div", class_="gs_a").text.split("-")[2].strip().split()[0]

  datalist.append(newdata.copy())
  newdata.clear()

for x in datalist:
  print(x)
