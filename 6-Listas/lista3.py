#Programa feito 07/11/2019
#Feito por Ana Maria Trzeciak

#Mudar item em uma lista: 
#sintaxe:  

#ecoding:utf-8

comida=[]

while True:
 op = int(input("1-Adicionar Comida Favorita 2-Exibir Comidas Favoritas 3-Tamanho da lista 4-Mudar item na lista\n"))
 
 if(op==1):
  comidafav=input("Digite nome da comida: ")
  comida.append(comidafav)
 if(op==2):
  print(comida)
 if(op==3):
  print("Tamanho da lista: ",len(comida))
 if(op==4):
  index=int(input("Indice que vai alterar: "))
  if(index<len(comida)):
   temp=input("Nome da Comida: ")
   comida[index]=temp
  else:
   print("Esse indice não existe.") 
