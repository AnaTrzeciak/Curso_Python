#ecoding:utf-8

def soma():
 x= float(input("Primeiro numero: "))
 y= float(input("Segundo numero: "))
 soma= x + y
 print("Soma: ",soma)

continuar=1


while continuar:
	if(continuar):
	 soma()
	continuar=int(input("digite 0 se desejar encerrar ou qualquer outro numero para continuar \n"))
