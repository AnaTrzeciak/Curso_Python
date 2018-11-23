#ecoding:utf-8

#Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o resultado aprovado/reprovado.

nota1=float(input("Digite sua primeira nota: "))
nota2=float(input("Digite sua segunda nota: "))

media=(nota1 + nota2)/2

print "MEDIA: ",media

if media<7.0:
	print media,"Você tirou menos que 7.0. REPROVADO\n"
else:
	if media<10.0:
		print media," APROVADO\n"
	else:
		print media, " APROVADO COM LAUREA!\n"
