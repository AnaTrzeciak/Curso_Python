#ecoding:utf-8
#Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha

senha= '2112'
tentativa= input("Digite a senha:")

while (senha != tentativa):
   print ("Senha errada. Tente novamente!")
   tentativa= input("Digite a senha:")

print ("Senha correta. Entrando no sistema...")


