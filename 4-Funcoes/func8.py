#ecoding:utf-8
#Crie uma função que receba um numero e exiba seu quadrado e o seu cubo.

def quadrado(x):
	return x*x

def cubo(x):
	return x*x*x

numero=float(input("Digite um numero: "))
print("Quadrado de ",numero," é: ",quadrado(numero))
print("O cubo de ",numero," é: ",cubo(numero))
