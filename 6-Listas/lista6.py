#Programa feito 07/11/2019
#Feito por Ana Maria Trzeciak

#Laço for com listas
#script que exibe uma lista de 10 elementos, contados de 1 até 10. Depois dobre cada valor dessa lista e exiba.

#ecoding:utf-8

numeros=[]

#colocando elementos na lista
for count in range(1,11):
  numeros+=[count]

#dobrando o valor
for count in range(len(numeros)):
  numeros[count]=numeros[count]*2

#exibindo itens
for count in numeros:
  print(count)
