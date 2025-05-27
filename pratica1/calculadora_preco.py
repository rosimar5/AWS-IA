"""Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final."""

nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade_produtos = 3
total_compra = preco_unitario * quantidade_produtos

print(f"Nome do Produto: R$ {nome_produto}")
print(f"Preço da Unidade: R$ {preco_unitario}")
print(f"Quantidade de produtos comprados: {quantidade_produtos}")
print(f"Valor Total da Compra: R$ {total_compra}")