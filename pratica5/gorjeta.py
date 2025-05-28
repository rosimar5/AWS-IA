"""Crie uma  função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada.
Calcula o valor da gorjeta baseada no total a conta e na porcentagem desejada.

Parâmentros:
valor_conta(float): O valor total da conta 
porcentagem_gorjeta(float): A porcentagem da gorjeta (ex: 15 para 15%)

retorna:
float: O valor da gorjeta calculada"""

valor_conta = float(input("Informe o valor total da compra: "))
porcentagem_gorjeta = float(input("% da gorjeta: "))

def calculo_gorjeta (valor_conta, porcentagem_gorjeta):
    calculo = valor_conta * (porcentagem_gorjeta/100)
    print(f"O valor da gorjeta é de: {calculo:.2f}")
    return calculo

calculo_gorjeta (valor_conta, porcentagem_gorjeta)