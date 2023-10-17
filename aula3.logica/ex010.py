palavra = str(input("Digite uma palavra: "))

inversa = palavra[::-1]
if palavra==inversa:
    print("É palíndrono")
else: 
    print("Não é")