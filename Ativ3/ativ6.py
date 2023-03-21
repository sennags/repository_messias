qae = int(input("Digite a quantidade atual em estoque: "))
qmaxe = int(input("Digite a quantidade máxima em estoque: "))
qmine = int(input("Digite a quantidade mínima em estoque: "))
media = (qmaxe + qmine)/2
if qae >= media:
    print("Não eferuar a compra.")
else:
    print("Efetuar a compra.")