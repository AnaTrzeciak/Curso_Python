#Curso Python Progressivo: Listas
#Programa feito em: 21/11/2019
#Feito por: Ana Maria

#ecoding: utf-8

#Matriz em Python: Lista dentro de lista

matriz = [[0 for i in range(4)] for j in range(4)]
count = 0

for linha in range(4):
  for coluna in range(4):
     matriz[linha][coluna] = count
     count +=1

for linha in range(4):
  for coluna in range(4):
    print("%4d" % matriz[linha][coluna], end='')
  print()
