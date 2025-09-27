import csv

dados = "veiculos.csv" #armazena o endereço do csv  em uma variavel
with open(dados, "r") as arquivo: 
    leitor = csv.DictReader(arquivo, delimiter=",")

    for linha in leitor:
        print(linha)



