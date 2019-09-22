#ecoding:utf-8
#Programa feito em 14/09/2019 por Ana Maria
#Conversao de temperatura. 

def celsius(x):
 return (x-32)/(1.8)

def fahrenheit(x):
 return 1.8*x + 32

valor=float(input("Digite o valor para conversão. "))

op=int(input("1-CELSIUS->FAHRENHEIT 2-FAHRENHEIT->CELSIUS \n"))

if(op==1):
 print(valor,"graus celsius=",round(fahrenheit(valor),3),"fahrenheit. \n")
elif(op==2):
 print(valor,"fahrenheit=",round(celsius(valor),2),"graus celsius. \n")
else:
 print("operação invalida.")
