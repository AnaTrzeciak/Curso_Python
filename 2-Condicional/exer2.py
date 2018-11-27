#ecoding:utf-8
#Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

num1=int(input("Digite o primeiro inteiro: "))
num2=int(input("Digite o segundo inteiro: "))

print "variavel 1:",num1,"\nvariavel 2:",num2
print "invertendo..."

aux=num2
num2=num1
num1=aux

print "variavel 1:",num1,"\nvariavel 2:",num2
