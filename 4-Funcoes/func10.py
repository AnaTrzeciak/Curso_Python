#ecoding:utf-8
#Crie uma função que recebe 3 números e exiba o maior deles.

def maior(x,y,z):
 if(x>y and x>z):
  print("O maior numero é ",x)
 elif(y>x and y>z):
  print("O maior numero é ",y)
 elif(z>x and z>y):
  print("O maior numero é ",z)
 else:
  print(".")


numero1=float(input("Numero 1: "))
numero2=float(input("Numero 2: "))
numero3=float(input("Numero 3: "))

maior(numero1,numero2,numero3) 
