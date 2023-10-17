# FAÇA UM PROGRAMA QUE PEDE PARA O USUARIO DIGITAR UMA FRASE, PERCORRA ESSA FRASE E MOSTRA NA TELA UM PRINT PARA CADA VEZ QUE ENCONTRAR UM NÚMERO DENTRO DESSA FRASE


frase = str(input("Digite uma frase: "))

for caracter in frase:
    if caracter in "1234567890":
        print(f'Numero encontrado: {caracter}')