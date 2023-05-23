print("        ///Menu ///\n")
print("Comida////Código////Valor  ")
print("Cachorro-quente = 100 = R$1,20")
print("Bauru = 101 = R$1,30")
print("Hambúrguer = 102 = R$1,20")
print("Cheeseburguer = 103 = R$1,30")
print("Refrigerante = 104 = R$1,00")
p = int(input("Insira seu pedido:"))
if p == 100:
    print("\nDeu o valor de R$1,20")
elif p == 101:
    print("\nDeu o valor de R$1,30")
elif p == 102:
    print("\nDeu o valor de R$1,20")
elif p == 103:
    print("\nDeu o valor de R$1,30")
elif p == 104:
    print("\nDeu o valor de R$1,00")
else:
    print("\nEste código não está registrado na tabela")
