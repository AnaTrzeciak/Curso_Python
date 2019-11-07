#ecoding:utf-8
#Programa criado em 07/11/2019           
#Feito por Ana Maria

#Exemplo de lista. Recebe dados da pessoa, guarda em uma lista e imprime na tela.

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))
altura = float(input("Qual sua altura? "))
peso = float(input("Qual o seu peso? "))

op = int(input("Estado Civil: 1-Casado 2-Solteiro \n"))

if op==1:
 op = True
else:
 op = False

eu = [nome,idade,altura,peso,op]

print("Nome: ",eu[0])
print("Idade: ",eu[1]," anos")
print("Altura: ",eu[2],"m")
print("Peso: ",eu[3],"kg")
print("Casado: ",eu[4])
