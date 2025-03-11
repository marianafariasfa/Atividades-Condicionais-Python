import os

os.system("cls")

print("-----NOTA FISCAL-----")

produto = input("Nome do produto: ")
quantidade = int(input("Quantidade do produto: "))
preco = float(input("Preço do produto: "))

total = quantidade * preco

os.system("cls")

print("-----NOTA FISCAL-----")

if quantidade <= 5:
    desconto1 = 0.2
    print("|Produto: ", produto)
    print("|Quantidade: ", quantidade)
    print("|Preço: ", preco)
    print("\n|Desconto de 2%")
    total_pagar1 = (total - desconto1)
    print("|Total a pagar: ", total_pagar1)

elif quantidade > 5 and quantidade <= 10:
    desconto2 = 0.3
    print("|Produto: ", produto)
    print("|Quantidade: ", quantidade)
    print("|Preço: ", preco)
    print("\n|Desconto de 3%")
    total_pagar2 = (total - desconto2)
    print("|Total a pagar: ", total_pagar2)
 
else: 
    desconto3 = 0.5
    print("|Produto: ", produto)
    print("|Quantidade: ", quantidade)
    print("|Preço: ", preco)
    print("\n|Desconto de 5%")
    total_pagar3 = (total - desconto3)
    print("|Total a pagar: ", total_pagar3)
    

