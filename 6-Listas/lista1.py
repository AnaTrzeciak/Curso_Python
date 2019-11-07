#Programa feito 07/11/2019
#Feito por Ana Maria Trzeciak

#Adicionar itens em uma lista: append()
#sintaxe: nome_da_lista.append(item a ser adicionado)

#ecoding:utf-8

comida=[]

while True:
 op = int(input("1-Adicionar Comida Favorita 2-Exibir Comidas Favoritas \n"))
 
 if(op==1):
  comidafav=input("Digite nome da comida: ")
  comida.append(comidafav)
 if(op==2):
  print(comida)
