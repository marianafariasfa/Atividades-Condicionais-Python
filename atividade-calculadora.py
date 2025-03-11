import os

os.system('cls')

print("-----CALCULADORA-----")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operador = (input("Digite a operação desejada: "))

os.system('cls')

print("-----CALCULADORA-----")

if(operador == "+"):
    resultado = n1 + n2
    print("O resultado da soma de", n1, "e", n2, "é")
    print(resultado)

elif(operador == "-"):
    resultado = n1 - n2
    print("O resultado da subtração de", n1, "e", n2, "é")
    print(resultado)

elif(operador == "*"):
    resultado = n1 * n2
    print("O resultado da multiplicação de", n1, "e", n2, "é")
    print(resultado)

elif(operador == "/"):
    resultado = n1 / n2
    print("O resultado da divisão de", n1, "e", n2, "é")
    print(resultado)

else:
    print("Operação inválida")


