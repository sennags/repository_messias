palavra = str(input("Me diga uma palavra: "))
if palavra[::-1] == palavra:
    print(f"Esta palavra é palíndromo. {palavra[::-1]}")
else:
    print(f"Esta palavra não é palídromo. {palavra[::-1]}")