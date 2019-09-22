#ecoding:utf-8
#Programação Python: Programa que gera numeros aleatorios em py
#Criado em 14/09/2019 por Ana Maria

import random   #biblioteca de numeros aleatorios

#funcão de numero aleatorios inteiros: randint

continuar=1
while continuar:
	print("Numero aleatorio gerado: ",random.randint(1,6))
	continuar=int(input("Gerar novamente? 1-SIM, 2-NAO"))
