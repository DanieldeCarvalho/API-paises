import json

import requests

URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME = 'https://restcountries.eu/rest/v2/name/'

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text #se nao cair nesse return a funcao retorna none por padrao.
    except:
        print('erro ao fazer requisicao em:',url)

def parsing(resposta):
    try:
        return json.loads(resposta) #nota-se que nem precisa adicionar numa variavel

    except Exception as error:
        print('erro ao fazer parsing')
        print(error)

def contagem_de_paises(lista_todos_paises):
    return len(lista_todos_paises)

def listar_paises(lista_paises):
    for pais in lista_paises:
        print(pais['name'])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao(URL_NAME + nome_do_pais)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('{}{}'.format(pais['name'], pais['population']))
        else:
            print('Pais nao encontrado')

def mostrar_moeda(nome_do_pais):
    resposta = requisicao(URL_NAME + nome_do_pais)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                moedas = pais['currencies']
                for moeda in moedas:
                    print('')
        else:
            print('Pais nao encontrado')

if __name__ == '__main__':
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            listar_paises(lista_de_paises)

'''24:05
a
'''