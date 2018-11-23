#ecoding:utf-8

#Exercicio 3:Crie um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra=input("M ou F")

if letra=='F':
	print "F- Feminino\n"
else:
	if letra=='M':
		print "M-Masculino.\n"
	else:
		print "Genero desconhecido.\n"

