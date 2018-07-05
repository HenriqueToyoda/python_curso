#Exercicio 3
#Calcular a média ponderada
#
#multiplicar a nota 1 * peso 1 e dividir pela quantidade de pesos
peso1 = float(input('peso 1: '))
peso2 = float(input('peso 2: '))
nota1 = float(input('nota 1: '))
nota2 = float(input('nota 2: '))

media = ((peso1 * nota1) + (peso2 * nota2)) / (peso1 + peso2)

print('Média: ', media )
