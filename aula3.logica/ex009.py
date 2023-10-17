# 9. Faça um programa para contar quantas consoantes existem em uma
# palavra. Utilize a condicional IF dentro do laço FOR.

numvogais = str(input("Digite uma frase: "))
conso = "bcdfghjklmnpqrstvxywz"
contador = 0

for letra in numvogais:
    if letra in conso:
        contador = contador + 1

print(f"A palavra tem {contador} consoantes.")