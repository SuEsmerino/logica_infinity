# # FAÇA UM PROGRAMA QUE PRINT NA TELA TODAS AS LETRAS DO ALFABETO COM EXCESSÃO DAS VOGAIS

# alfabeto = "abcdefghijklmnopqrstuvwxyz"



# for letra in alfabeto:
#     if letra in "bcdfghjklmnpqrstvwxyz":
#         print(letra)


# ________________________


alfabeto = "abcdefghijklmnopqrstuvwxyz"
vogais ="aeiou"



for letra in alfabeto:
    if letra not in vogais:
        print(letra)
