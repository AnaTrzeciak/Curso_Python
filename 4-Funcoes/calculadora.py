#ecoding:utf-8

def soma():
 x= float(input("Primeiro numero: "))
 y= float(input("Segundo numero: "))
 soma= x + y
 print("Soma: ",soma)


def sub():
 x= float(input("Primeiro numero: "))
 y= float(input("Segundo numero: "))
 sub= x-y
 print("Subtração: ",sub)

def multiplicacao():
 x= float(input("Primeiro numero: "))
 y= float(input("Segundo numero: "))
 multiplicacao=x*y
 print("Multiplicação: ",multiplicacao)

def divisao():
 x= float(input("Primeiro numero: "))
 y= float(input("Segundo numero: "))
 divisao=x/y
 print("Divisão: ",divisao)

var=int(input("Escolha o tipo de operação que deseja fazer: 1-soma, 2-subtração, 3-multiplicação, 4-divisão: "))

while var:
 if(var==1):
 	 soma()
 elif(var==2): 
  	sub()
 elif(var==3):
  	multiplicacao()
 elif(var==4):
  	divisao()
 else:
  	print("Operação invalida.\n") 

