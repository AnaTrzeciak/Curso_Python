#ecoding:utf-8
#Faça um programa que leia 5 números e informe o maior número.

print("Informe 5 numeros.")

num1= int(input("numero 1: "))
num2= int(input("numero 2: "))
num3= int(input("numero 3: "))
num4= int(input("numero 4: "))
num5= int(input("numero 5: "))

if(num1>num2 and num1>num3 and num1>num4 and num1>num5):
	print("O numero", num1, "é o maior de todos")
	
if(num2>num1 and num2>num3 and num2>num4 and num2>num5):
	print("O numero", num2, "é o maior de todos")
	
if(num3>num1 and num3>num2 and num3>num4 and num3>num5):
	print("O numero", num3, "é o maior de todos")
	
if(num4>num1 and num4>num2 and num4>num3 and num4>num5):
	print("O numero", num4, "é o maior de todos")

if(num5>num1 and num5>num2 and num5>num3 and num5>num4):
	print("O numero", num5, "é o maior de todos")
	


