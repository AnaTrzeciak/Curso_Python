#ecoding:utf-8

#Curso Python: Recursividade: somatório e fatorial usando função recursiva
#Feito em 01/09/2019 por Ana Maria

#f(x)= f(x-1) + x

#===================================================================
#soma de um inteiro

def somatorio(x):
  if x==1:
     return 1
  else:
     return x + somatorio(x-1)

while True:
  x= int(input("Somatorio de 1 até: "))
  print("Soma: ",somatorio(x))
