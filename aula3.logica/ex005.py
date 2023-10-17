# # Faça um programa para calcular a média de uma lista de números.

# num1 = int(input("Digite o menor número da lista: "))
# num2 = int(input("Digite o maior número da lista: "))
# soma = 0

# for num in range(num1, num2):
#     soma += num


# media=(soma)/(num2 - num1)
# print(media)

# FAÇA UM PROGRAMA QUE PEDE PARA O USUARIO DIGITAR 10 NUMEROS E NO FINAL MOSTRE A MEDIA DESSES 10 NUMEROS

soma = 0
for i in range(1,11):
    numero = float(input(f"Digite o {i}º numero: "))
    soma += numero

media = soma/10
print(f'A media dos 10 números digitados é {media}.')