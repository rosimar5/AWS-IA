"""Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. """

import random
import string

def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation

    while True:
        try:
            tamanho = int(input("Informe a quantidade de caracteres da sua senha: "))
            if tamanho < 1:
                print("Digite um número maior que zero.")
                continue

            senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
            print(f"\nSenha gerada: {senha}")
            break

        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
            
gerar_senha()
