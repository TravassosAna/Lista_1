vl = float(input("Digite o valor em dólar ou euro que deseja converter para reais: "))
moeda = input("Tecle 'D' para dólar ou 'E' para Euro: ")
if moeda == 'D':
    conversao = 5.01
elif moeda == 'E':
    conversao = 5.49
else:
    print("Essa moeda não foi declaradas acima.")
    exit(0)
resultado = vl * conversao
print(f"O valor de {vl:.2f} {moeda.upper()} em reais é de {resultado:.2f} reais.")
