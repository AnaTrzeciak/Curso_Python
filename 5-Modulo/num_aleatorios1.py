#ecoding:utf-8
#Programação Python: Programa que gera numeros aleatorios em py
#Criado em 14/09/2019 por Ana Maria

import random   #biblioteca de numeros aleatorios

#Funcao randrange(): define um intervalo
#random.randrange(x) - vai gerar um numero aleatorio de 0 ate x-1
#random.randrange(x,y) - vai gerar um numero de x ate y-1
#random.randrange(x,y,z) - pode gerar de x ate y-1, pulando de z em z
#random.random() - numero aleatorio decimal

#Crie um script em Python que gere 6 números aleatórios para a Mega-Sena (neste jogo, você pode escolher dezenas de 1 até 60). Não pode repetir dezena.


print("Numeros aleatorios da MEGA.\n")

continuar=1
while continuar:
	for i in range(1,7):
	  print("numero: ",random.randint(1,60))
	continuar=int(input("Novo jogo? 1-SIM, 2-NAO \n"))
