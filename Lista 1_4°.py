p = float(input("Qual é seu peso? --> "))
h = float(input("Qual é a sua altura? --> "))
imc = p/(h**2)
print("Seu imc é: ", imc)
if (imc <= 18.5):
    print("baixo peso!")
elif(imc <= 18.5 and imc >= 24.9):
    print("Intervalo normal")
elif(imc <= 25 and imc >= 29.9):
    print("sobrepeso")
elif(imc <= 30 and imc >= 34.9):	
    print("Obesidade classe I")
elif(imc <= 35 and imc >= 39.9):
    print("Obesidade classe II")
elif(imc >= 34.9):
    print("Obesidade classe III")
