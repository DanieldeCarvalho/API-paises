import requests

URL_ALL = 'https://restcountries.eu/rest/v2/all'

respota = requests.get(URL_ALL)


print(respota)
'''a respota e um objeto do <class 'requests.models.Response'>
 print(type(resposta))
 se eu der um resposta.text ele vai puxar as informacoes de todos os paises
 
 '''

'''
1:34:10
'''

