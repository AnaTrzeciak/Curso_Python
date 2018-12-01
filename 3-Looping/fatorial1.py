#ecoding:utf-8

num= 1

while True:
  numero=int(input("fatorial de:"))
  resultado= 1
  for i in range(1,numero+1):
    resultado*= i
  print (resultado)
