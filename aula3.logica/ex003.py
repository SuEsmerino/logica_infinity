# Faça um programa para imprimir os números ímpares de 1 a 19. Utilize a
# função range() para criar a coleção de números.

# for numero in range (1, 20, 2):

#         print (numero)

# _____________________________________ a forma abaixo é a correta, em cima é "malandragem"

for num in range (1,21):
 if num % 2 != 0:
  print(num)