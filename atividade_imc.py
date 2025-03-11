import os

os.system("cls")

print("-----CALCULO IMC-----")

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / (altura * altura)

os.system("cls")

print("-----CALCULO IMC-----")

print("|IMC: ", imc)

if imc < 16.9:
    print("|MUITO ABAIXO DO PESO")

elif imc >= 17 and imc <= 18.9:
    print("|ABAIXO DO PESO")

elif imc >= 18.5 and imc <= 24.9:
    print("|PESO NORMAL")

elif imc >= 25 and imc <= 29.9:
    print("|ACIMA DO PESO")

elif imc >= 30 and imc <= 34.9:
    print("|OBESIDADE GRAU I")

elif imc >= 35 and imc <= 40:
    print("|OBESIDADE GRAU II")

else:
    print("|OBESIDADE GRAU III")