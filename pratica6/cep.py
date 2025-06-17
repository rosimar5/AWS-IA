"""Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado."""

import requests

cep = input("Digite o seu CEP: ")

try:
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    resposta.raise_for_status() 
    dados = resposta.json()

    if "erro" in dados:
        print("CEP inválido. Tente novamente.")
    else:
        print("Logradouro:", dados["logradouro"])
        print("Bairro:", dados["bairro"])
        print("Cidade:", dados["localidade"])
        print("Estado:", dados["uf"])

except requests.exceptions.RequestException as e:
    print("Erro ao conectar à API:", e)
except ValueError:
    print("Erro ao processar a resposta JSON.")





