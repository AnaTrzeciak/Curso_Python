#ecoding:utf-8
#Programa feito em: 05/11/2019
#Por Ana Maria

#Exercícios Python: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos através de uma função. Seu script também deve fornecer a média dos três números, através de uma segunda função que chama a primeira.

def soma(x,y,z):
 return x+y+z

def media(x,y,z):
 return soma(x,y,z)/3

primeiro=float(input("Primeiro numero: "))
segundo=float(input("Segundo numero: "))
terceiro=float(input("Terceiro numero: "))

print("A soma é ",soma(primeiro,segundo,terceiro)," e a média é ",round(media(primeiro,segundo,terceiro),3),"\n")
