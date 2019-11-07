#Programa feito 07/11/2019
#Feito por Ana Maria Trzeciak

#Tamanho de uma lista: len() 
#sintaxe: len(nome_da_lista) 

#ecoding:utf-8

comida=[]

while True:
 op = int(input("1-Adicionar Comida Favorita 2-Exibir Comidas Favoritas 3-Tamanho da lista\n"))
 
 if(op==1):
  comidafav=input("Digite nome da comida: ")
  comida.append(comidafav)
 if(op==2):
  print(comida)
 if(op==3):
  print("Tamanho da lista: ",len(comida))
