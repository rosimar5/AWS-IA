# 2- Calculadora de Desconto

# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

# * Nome do produto: "Camiseta"
# * Preço original: R$ 50.00
# * Porcentagem de desconto: 20%
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_produto = "Camiseta"
preco_produto = 50.00
porcentagem_desconto_produto = 20

desconto_produto = preco_produto * (porcentagem_desconto_produto / 100)
valor_final = preco_produto - desconto_produto

print(f"Nome do Produto: {nome_produto}")
print(f"Preço do Produto: {preco_produto}")
print(f"Desconto: {porcentagem_desconto_produto}")
print(f"Valor Final do Produto: {valor_final}")