# 1- Conversor de Moeda
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

# * Valor em reais: R$ 100.00
# * Taxa do dólar: R$ 5.20
# * Taxa do euro: R$ 6.15
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

conversao_dolar = valor_reais * taxa_dolar
conversao_euro = valor_reais * taxa_euro

print(f"Valor em reais: {valor_reais}")
print(f"Valor convertido em dólar: {conversao_dolar}")
print(f"Valor convertido em euro: {conversao_euro}")