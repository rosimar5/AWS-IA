#Crie uma função que calcule a idade de uma pessoa em dias, baseado no ano de nascimento

from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = int(ano_atual) - ano_nascimento
    return idade * 365

print(calcular_idade(2004))