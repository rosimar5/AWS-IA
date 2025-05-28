"""3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

temperatura = float (input("Informe a temperatura: "))
unidade_origem = input("Informe a unidade de origem - C, K ou F: ")
unidade_destino = input("Informe o destino - C, K ou F")

if unidade_origem == unidade_destino:
    resultado = temperatura
    print(f"{temperatura}°{unidade_origem} = {resultado:.2f}°{unidade_destino}")

elif unidade_origem == "C" and unidade_destino == "F":
    resultado = (temperatura * 9/5) + 32
    print(f"{temperatura}°C = {resultado:.2f}°F")

elif unidade_origem == "C" and unidade_destino == "K":
    resultado = temperatura + 273.15
    print(f"{temperatura}°C = {resultado:.2f}°K")

elif unidade_origem == "F" and unidade_destino == "C":
    resultado = (temperatura - 32) * 5/9
    print(f"{temperatura}°F = {resultado:.2f}°C")

elif unidade_origem == "F" and unidade_destino == "K":
    resultado = (temperatura - 32) * 5/9 + 273.15
    print(f"{temperatura}°F = {resultado:.2f}°K")

elif unidade_origem == "K" and unidade_destino == "C":
    resultado = temperatura - 273.15
    print(f"{temperatura}°K = {resultado:.2f}°C")

elif unidade_origem == "K" and unidade_destino == "F":
    resultado = (temperatura - 273.15) * 9/5 + 32
    print(f"{temperatura}°K = {resultado:.2f}°F")

