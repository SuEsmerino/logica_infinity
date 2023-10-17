# Faça um programa para contar quantas vogais existem em uma palavra.
# Utilize a condicional IF dentro do laço FOR.

numvogais = str(input("Digite uma frase: ")).lower
vogais = "aeiou"
contador = 0

for letra in numvogais:
    if letra in vogais:
        contador += 1
print(f"A palavra tem {contador} vogais.")