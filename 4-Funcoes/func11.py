#Curso Python: Passagem de argumentos por valor em funções
#Feito em 01/09/2019

#ecoding:utf-8

def muda(var):
 var=0
 print("Valor de x dentro da função: ",var)

var=1
print("Valor de x antes da funcao: ",var)
muda(var)
print("Valor de x ao sair da funcao: ",var)


#Quando enviamos um argumento para uma função, ela vai ficar apenas com o valor dessa variável.
