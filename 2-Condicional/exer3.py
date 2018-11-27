#ecoding:utf-8
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1=int(input("Digite o primeiro numero:"))
num2=int(input("Digite o segundo numero:"))
num3=int(input("Digite o terceiro numero:"))

print num1,",",num2,",",num3

if(num1<num2 and num2<num3):
	print num3,",",num2,",",num1

if(num1<num2 and num3<num2):
	print num2,",",num2,",",num3
