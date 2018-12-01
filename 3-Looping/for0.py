#ecoding:utf-8
#Laço for sintaxe: for variavel in [val1, val2, val3, etc]:
    			#codigo
    			#codigo
    			#codigo
#==============================================================
#Crie um script em Python que imprima os números de 1 até 5 na tela

#for val in [1, 2 , 3, 4, 5]:
#  print val

#==============================================================

elementos= []

for i in range(0,6):   #so vai ate o 5 porque nao inclui o ultimo
  print ("Adicione", i," na lista.")
  elementos.append(i)

for i in elementos:
  print ("Elementos contem:",i)
