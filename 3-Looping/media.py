#ecoding:utf-8
#Primeiro, pergunta a quem vai usar o script quantos alunos tem na sala.Depois, quantas matérias cada aluno estuda.
#Em seguida o usuário vai preenchendo a nota de cada matéria, de cada aluno.
#Seu programa deve fornecer a média de cada aluno e a média geral da turma. 

alunos= int(input("Quantos alunos tem na turma: "))
materias= int(input("Quantas materias eles estudam: "))

mediaTurma= 0

for aluno in range(alunos):
  print("Aluno",aluno+1,":")

  mediaAluno= 0
  for materia in range(materias):
    print("Nota da materia",materia+1,":",end='')
    nota= int(input())
    mediaAluno+= nota

  mediaAluno/= materias
  print("Media desse aluno:", mediaAluno,"\n")
  
  mediaTurma+= mediaAluno

mediaTurma /= alunos
print("Media da turma:",mediaTurma)
 
