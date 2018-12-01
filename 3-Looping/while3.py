#ecoding:utf-8
#Crie um programa que peça um número ao usuário e imprima todos os números pares de 1 até o número fornecido.

numero= 1
maximo= int(input("Digite um inteiro maior que 1:"))

print ("Numero pares entre 1 e", maximo,":")

while numero <= maximo:
	if numero%2==0:
	  print (numero)
	numero+= 1


