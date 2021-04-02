import json
import sys

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

def contagem_de_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        return len(lista_de_paises)

def listar_paises(lista_paises):
    for pais in lista_paises:
        print(pais['name'])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao(URL_NAME + nome_do_pais)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('{}: {}'.format(pais['name'], pais['population']))
                print('')
    else:
        print('Pais nao encontrado')

def mostrar_moedas(nome_do_pais):
    '''retorna tudo que conter os caracteres passados como parametro,

    '''
    resposta = requisicao(URL_NAME + nome_do_pais)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('Moedas do ', pais['name'] + ':')
                moedas = pais['currencies']
                for moeda in moedas:
                    print('{} - {}'.format(moeda['name'], moeda['code']))
                print('')
    else:
        print('Pais nao encontrado')

def ler_nome_pais():
    try:
        nome_do_pais = sys.argv[2]
        mostrar_moedas(nome_do_pais)
        return nome_do_pais
    except:
        print('Eh preciso passar o nome do pais')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('## Bem vindo ao sistema de paises ##')
        print('como usar: python paises.py <funcao> <nome do pais>')
        print('Funcoes disponiveis: contagem, moeda, populacao')
    else:
        argumento1 = sys.argv[1]

        if argumento1 == 'contagem':
            print('Existem ', contagem_de_paises(), 'paises no mundo') #contagem retorna um numero

        elif argumento1 == 'moeda':
            pais = ler_nome_pais()
            if pais:
                mostrar_moedas(pais)

        elif argumento1 == 'populacao':
            pais = ler_nome_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print('Argumento invalido')
