import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

answr = urlopen(url)

dados = json.load(answr)

ip = dados['ip']
org = dados['org']
city = dados['city']
country = dados['country']
region = dados['region']

print('Detalhes do IP externo\n')
print(f'IP: {ip}\nRegiao: {region}\nPais: {country}\nCidade: {city}\nOrg.: {org}')