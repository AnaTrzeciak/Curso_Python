#ecoding:utf-8
#Crie uma função que recebe 4 notas de um aluno, e exiba a média dele

def media(x,y,z,a):
	return (x+y+z+a)/4

nota1=float(input("Nota 1: "))
nota2=float(input("Nota 2: "))
nota3=float(input("Nota 3: "))
nota4=float(input("Nota 4: "))

print("A media do aluno foi ",media(nota1,nota2,nota3,nota4))
