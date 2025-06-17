"""Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado.
"""

import requests

def gerar_usuario_aleatorio():
    try:
        resposta = requests.get("https://randomuser.me/api/")
        resposta.raise_for_status() 

        dados = resposta.json()  
        usuario = dados['results'][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("\n Perfil Gerado Aleatoriamente:")
        print(f"Nome:  {nome}")
        print(f"E-mail: {email}")
        print(f"País:   {pais}")

    except requests.RequestException as e:
        print("Erro ao conectar à: ", e)

gerar_usuario_aleatorio()