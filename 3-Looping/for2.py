#ecoding:utf-8

#Função range(): retorna uma lista de números inteiros.
#Sintaxe: range(n)
#Como vai fornecer 'n' elementos e começa do 0, o último elemento é sempre n-1
#range(inicio, fim), não imprime o numero 'fim' é sempre fim-1
#range(inicio, fim, pulo), pula de quantos em quantos
#==============================================================

#Crie um script em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada

tabuada= int(input("Qual tabuada fazer:"))

for var in range(1,11):
  print(tabuada*var)
