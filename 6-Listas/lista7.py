#Programa feito 07/11/2019
#Feito por Ana Maria Trzeciak

#Laço for com listas. Programa que pede o numero de matérias de um aluno, suas notas e da a média final.

#ecoding:utf-8

n = int(input("Numero de matérias: "))
notas = []
soma = 0

for count in range(n):
  nota = float(input("Nota da matéria %2d: "% (count+1)))
  notas+= [nota]
  soma+= nota

print("Notas: ",notas)
print("Media: ",round((soma/n),2))
