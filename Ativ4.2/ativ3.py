num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
while num2  == num1:
    print("Escreva de novo.")
    num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"O maior foi {num1}")
else:
    print(f"O maior foi {num2}")