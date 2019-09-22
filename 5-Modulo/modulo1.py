#ecoding:utf-8
#Programa criado em 14/09/2019 por Ana Maria

import calculadora

while True:
	print("1-SOMA")
	print("2-SUBTRAÇÃO")
	print("3-MULTIPLICAÇÃO")
	print("4-DIVISÃO")
	op=int(input("Qual operação deseja fazer: "))
	x=float(input("Primeiro numero: "))
	y=float(input("Segundo numero: "))

	if(op==1):
	  print("Soma: ",calculadora.soma(x,y))
	elif(op==2):
	  print("Subtração: ",calculadora.subtracao(x,y))
	elif(op==3):
	  print("Multiplicação: ",calculadora.multiplicacao(x,y))
	elif(op==4):
	  print("Divisao: ",calculadora.divisao(x,y))
	else:
	  print("Operação inválida.") 



