#ecoding:utf-8
#Loop dentro de loop

#Tabuleiro NxN

print("Vamos criar um tabuleiro de tamanho NxN.")
n= int(input("Digite N (tamanho do tabuleiro):"))

for linha in range(n):
  for coluna in range(n):
    print("x ",end= '')
  print()                     #quebra de linha
