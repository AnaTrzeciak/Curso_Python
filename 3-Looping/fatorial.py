#ecoding:utf-8
#Fatorial de um numero inteiro

#while
#numero= int(input("Digite o inteiro que desejar calcular o fatorial: "))
#resultado= 1
#count= 1

#while count <= numero:
#  resultado *= count    #resultado=resultado*count
#  count+= 1

#print(resultado) 

#============================================================
#for

numero= int(input("fatorial de: "))
resultado= 1

for n in range(1,numero+1):
  resultado *= n

print(resultado)
