#ecoding:utf-8
#Serie de Fibonacci
#Feito em 02/09/2019 por Ana Maria

def fibonacci(x):
 if(x==1):
   return 0
 elif(x==2):
   return 1
 else: 
   return fibonacci(x-1) + fibonacci(x-2)

def menu():
  n=int(input("Exibir ate o termo (maior que 2): "))
 
  for val in range(1,n+1):
     print(fibonacci(val))


while True:
  menu()


