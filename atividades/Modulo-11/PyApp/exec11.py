import requests

def return_postalcode(cep):
    response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
    print(response.status_code)
    # print(response.text)
    # print(response.json())
    # print(type(response.json()))
    data = response.json()
    print(data['logradouro'])
    return data

def pokemons_data(pokemon):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
    # print(response.text)
    data = response.json()
    return data


def return_site(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    response = return_site('https://www.formula1.com/')
    print(response)
    # return_postalcode('22041001')
    # pokemon = pokemons_data('lucario')
    # print(pokemon['sprites']['front_shiny'])
