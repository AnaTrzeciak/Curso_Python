#ecoding:utf-8
#Programa feito em 05/11/2019
#Feito por: Ana Maria

#Exercício: A probabilidade de dar um valor em um dado é 1/6 (uma em 6). Faça um script em Python que simule 1 milhão de lançamentos de dados e mostre a frequência que deu para cada número.

import random 

def gera():
  return random.randint(1,6)

def repete(n):
  t1=t2=t3=t4=t5=t6=0
  for val in range(n):
      test=gera()
      
      if(test==1):
       t1+=1
      elif(test==2):
       t2+=1
      elif(test==3):
       t3+=1
      elif(test==4):
       t4+=1
      elif(test==5):
       t5+=1
      else:
       t6+=1
  
  print("Numero 1 saiu",t1," vezes = ",round((t1/n)*100,2),"%")
  print("Numero 2 saiu",t2," vezes = ",round((t2/n)*100,2),"%")
  print("Numero 3 saiu",t3," vezes = ",round((t3/n)*100,2),"%")
  print("Numero 4 saiu",t4," vezes = ",round((t4/n)*100,2),"%") 	
  print("Numero 5 saiu",t5," vezes = ",round((t5/n)*100,2),"%")
  print("Numero 6 saiu",t6," vezes = ",round((t6/n)*100,2),"%")


N=int(input("Quantos lançamentos de dados?"))
repete(N)
