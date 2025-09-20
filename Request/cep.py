import requests

cep = input("Digite o seu cep: ")
via_cep = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(via_cep)

print(requisicao)

print (f"CEP: {requisicao.json()['cep']}")
print (f"Rua: {requisicao.json()['logradouro']}")
print (f"Bairro: {requisicao.json()['bairro']}")
print (f"Cidade: {requisicao.json()['localidade']}")
print (f"Estado: {requisicao.json()['estado']}")



