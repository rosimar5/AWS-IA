"""Crie uma função que verifique se uma palavra ou frase é um palindromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda "Sim", se o resultado for False, responda "Não"""

def palindromo(texto):
    texto_formatado = ''.join(letra.lower() for letra in texto if letra.isalnum())
    
    if texto_formatado == texto_formatado[::-1]:
        return "Sim"
    else:
        return "Não"

frase = input("Digite uma palavra ou frase: ")
print(palindromo(frase))
