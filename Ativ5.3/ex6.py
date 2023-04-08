convidados = ["Angelina Jolie", "Brad Pitt", "Jennifer Aniston", "Tom Hanks", "Leonardo DiCaprio"]

nao_pode_comparecer = ["Brad Pitt"]
novos_convidados = ["George Clooney"]

for convidado in nao_pode_comparecer:
    convidados.remove(convidado)

print("Os seguintes convidados não poderão comparecer ao jantar:")
for nao_convidado in nao_pode_comparecer:
    print(nao_convidado)

print("\nOs seguintes convidados ainda estão confirmados para o jantar:")
for convidado in convidados:
    print(convidado)

for convidado in convidados:
    mensagem = f"Olá {convidado}! Você está convidado para um jantar em minha casa na próxima sexta-feira às 20h."
    print(mensagem)
for convidado in convidados:
    print("Olá, " + convidado + "! Você ainda está confirmado para o jantar em minha casa. Espero vê-lo lá!")