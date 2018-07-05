#Exercicio de mostrar o mês de nascimento
meses = ('janeiro', 'fevereiro')
nasc = input('Digite a data de nascimento no formato DD-MM-AAAA:')

indice = int(nasc[3:5])-1

mes = meses[indice]

print('Nascimento em : ', mes)
