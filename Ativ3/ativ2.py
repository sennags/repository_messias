nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
res = (nota1 + nota2)/2
if res >= 6:
    print(f"Parabéns, você passou! Com a nota {res}")
else:
    print(f"Infelizmente, você foi reprovado. Com a nota {res}")
