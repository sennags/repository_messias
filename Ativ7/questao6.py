salario = float(input("Digite o seu salário: "))
if salario > 1500:
    percentual = 10
elif salario < 1500:
    percentual = 15

percentual = percentual/100
aumento = percentual * salario
novo_salario = salario + aumento

print(f"Seu novo salário é: {novo_salario}")