#ecoding:utf-8
#Programe um script em Python que calcule a média de uma turma, não importa o número de alunos que ela tenha, seu único script serve para todos os casos

alunos= int(input("Numero de alunos na turma:"))
count= 1
soma= 0.0

while count <= alunos:
  print ("Nota do aluno", count,":")
  nota= float(input())
  soma+= nota
  count+= 1

print ("Media da turma:", (soma/alunos))


