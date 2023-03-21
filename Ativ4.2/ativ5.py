numconta = float(input("Digite o número da sua conta: "))
saldo = float(input("Digite o seu saldo: "))
debito = float(input("Digite o seu débito: "))
credito = float(input("Digite o seu crédito: "))
saldo_atual =(saldo - debito) + credito
if saldo_atual >= 0:
    print("Saldo positivo.")
else:
    print("Saldo negativo")
