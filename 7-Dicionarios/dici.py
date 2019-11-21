#Curso Python Progressivo: Listas
#Programa feito em: 21/11/2019
#Feito por: Ana Maria

#ecoding: utf-8

loginSenha = {'joao':'rush','maria':'yes','zezinho':'genesis'}

login = input("Qual seu login: ")
senha = input("Senha: ")

if loginSenha[login] == senha:
  print("Acesso autorizado...")
else:
  print("Senha errada")
