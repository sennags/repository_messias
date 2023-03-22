mp = int(input("Digite o número das maçãs compradas: "))
if mp >= 12:
    print(f"Você comprou mais maçãs! Ganhou uma promoção, você irá pagar apenas {mp}")
elif mp < 12:
    sdesconto = mp * 1.30
    print(f"Você comprou {mp} maçãs, logo irá pagar {sdesconto}.")