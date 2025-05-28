# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400


ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")






"""Um ano é bissexto se for divisível por 4.
Mas, se for divisível por 100 (anos terminados em 00), não é bissexto.
Exceto se for divisível por 400, aí é bissexto."""