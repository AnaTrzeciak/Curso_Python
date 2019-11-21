#Curso Python Progressivo: Listas
#Programa feito em: 21/11/2019
#Feito por: Ana Maria

#ecoding: utf-8

#Copiar uma lista
#Jeito errado:
list1 = [1,2,3,4]
list2 = list1
list1[0] = 0

#Jeito certo:
list2 = []
for item in list1:
  list2.append(item)

#Jeito certo 2:
list2 = [] + list1

