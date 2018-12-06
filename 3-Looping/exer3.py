#ecoding:utf-8
#Exercicio 3: validação de dados

nome= input("Nome= ")

if(len(nome)<=3):
 print("O nome deve ter mais que tres caracteres")
 nome= input("Nome= ")

idade= input("Idade=")
sexo= input("Sexo (f/m)=")
civil= input("Estado civil (s/c/v/d)= ")

print(nome,",",idade,",",sexo,",",civil,)


