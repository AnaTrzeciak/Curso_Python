#ecoding:utf-8
#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações

print("Vamos criar um login para você em nosso site, digite as informações solicitadas.\n")

nome= input("Digite seu nome: ")
senha= input("Digite uma senha: ")

if(senha==nome):
  while(senha==nome):
    print("A senha é igual ao nome, digite novamente:")
    senha= input("Digite uma senha: ")
  print("Login válido!")
else:
  print("Login válido!")
	
