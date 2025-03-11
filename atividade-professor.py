import os

os.system("cls")

print("-----COLÉGIO APRENDER-----")

nivel_prof = int(input("Digite o nivel do professor: "))
hora_aula = int(input("Digite a quantidade de aulas por semana: "))

os.system("cls")

print("-----COLÉGIO APRENDER-----")

if nivel_prof == 1:
    salario = (12 * hora_aula) * 4
    print("|SALÁRIO: ", salario)
    print("|PAGAMENTO EFETUADO COM SUCESSO")

elif nivel_prof == 2:
    salario = (17 * hora_aula) * 4
    print("|SALÁRIO: ", salario)
    print("|PAGAMENTO EFETUADO COM SUCESSO")

elif nivel_prof == 3:
    salario = (25 * hora_aula) * 4
    print("|SALÁRIO: ", salario)
    print("|PAGAMENTO EFETUADO COM SUCESSO")

else:
    print("|NIVEL DE PROFESSOR INVALIDO")
    print("|PAGAMENTO NAO EFETUADO")
