#ecoding:utf-8
#Fatorial com recursividade
#Feito em 02/09/2019 por Ana Maria

#n!=n*(n-1)!

def fatorial(x):
  if x==1:
     return 1
  else:
     return x*fatorial(x-1)

while True:
   x=int(input("Fatorial de: "))
   print("Fatorial:  ",fatorial(x))
