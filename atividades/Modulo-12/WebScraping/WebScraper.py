from bs4 import BeautifulSoup
import requests

data = requests.get('https://scholar.googleusercontent.com/scholar.bib?q=info:9OT7g3fE_OAJ:scholar.google.com/&output=citation&scisdr=CgUCgYmGENjzg576bBQ:AAGBfm0AAAAAZAP8dBTRV_N5UA-vtEJUU9aO5nlSi6Mx&scisig=AAGBfm0AAAAAZAP8dGq1igzSY_Iu5pwzC3QmkwOyyU-R&scisf=4&ct=citation&cd=0&hl=en').text

soup = BeautifulSoup(data, 'html.parser')
dados = list(soup)
print(dados[0:])
