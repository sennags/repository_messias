num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
while num2  == num1:
    print("Escreva de novo.")
    num2 = int(input("Digite outro número: "))
ord = [num1, num2]
ord.sort()
print("A ordem é {}".format(ord))