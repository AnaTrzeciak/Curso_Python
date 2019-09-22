#ecoding:utf-8
#Programa feito em 14/09/2019 por Ana Maria
#Conversão de radianos em graus e vice-versa

import math 

num=float(input("Digite o numero que voce quer converter "))

op=int(input("Converter 1-radianos->graus 2-graus->radianos"))

if(op==1):
  print(num," radianos é igual a ",math.degrees(num)," graus. \n")
elif(op==2):
  print(num," graus é igual a ",math.radians(num)," radianos. \n")
else:
  print("operação inválida.\n")
