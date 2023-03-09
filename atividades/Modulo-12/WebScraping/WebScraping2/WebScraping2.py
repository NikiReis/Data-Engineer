from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.climatempo.com.br').content
soup = BeautifulSoup(url, 'html.parser')

temperature = soup.find("span", class_="block _margin-b-5 -gray")
print(temperature.string)
print(soup.find('admin'))

