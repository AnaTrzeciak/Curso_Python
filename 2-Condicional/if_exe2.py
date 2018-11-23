#ecoding:utf-8

#Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor= int(input("Digite um numero (positivo ou negativo): "))

if (valor>0):
	print"O valor é positivo."
else:
	if valor==0:
		print"O numero não é nem positivo nem negativo é zero"
	else:
		print"O valor é negativo."

