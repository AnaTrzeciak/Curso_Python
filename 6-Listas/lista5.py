#Programa feito 07/11/2019
#Feito por Ana Maria Trzeciak

#Laço for com listas

#ecoding:utf-8

numeros=[]

for count in range(10):
  numeros+=[count]

#imprime lista
#print(numeros)   

#imprime item por item da lista e mostra a soma de todos os numeros.

soma=0
for count in numeros:
  print(count)
  soma+=count

print("Soma: ",soma)
