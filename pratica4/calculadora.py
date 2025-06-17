"""Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

1. A calculadora deve solicitar ao usuário que insira dois números e uma operação.
2 As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
3. O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
4. Trate os seguintes erros:
- Entrada inválida (não numérica) para os números
- Divisão por zero
- Operação inválida
5. Use try/except para capturar e tratar os erros apropriadamente.
6. Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
7. Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa."""

def calcular():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida. Use apenas +, -, *, /.")
            
            print(f"Resultado: {resultado}")
            break
        
        except ValueError as e:
            print(f"Erro de valor: {e}")
        
        except ZeroDivisionError:
            print(f"Não é possível divisão por 0")
        
calcular()