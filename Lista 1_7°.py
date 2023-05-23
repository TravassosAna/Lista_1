n1 = float(input("Digite o Primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número:  "))
if n1 < n2 and n1 < n3:
    print(n1, n2, n3, " e o menor número é: ", n1)
elif n2<n1 and n2<n3:
    print(n1, n2, n3, " e o menor número é: ", n2)
elif n3<n1 and n3<n2:
    print(n1, n2, n3, " e o menor número é: ", n3)

