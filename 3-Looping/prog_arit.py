#ecoding:utf-8
#Uma progressão aritmética, também conhecida por PA, nada mais é que uma sequência de números que obedecem a um determinado número inicial e um número chamado de razão
#A sequência começa com o número inicial. O termo seguinte da sequência é o anterior, somado a razão. E assim sucessivamente.

#a_n= a_1 + (n-1)*r, onde n é a posição do termo geral

primeiro= int(input("Qual o primeiro elemento: "))
razao= int(input("Qual a razao da PA: "))
n= int(input("Quantos elementos exibir: "))

ultimo= primeiro + (n-1)*razao
ultimo= ultimo+1  #somando 1 para que o range inclua o valor de 'ultimo' e não ate 'ultimo-1'

for var in range(primeiro, ultimo, razao):
  print(var)  
