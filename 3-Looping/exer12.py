#ecoding:utf-8
#Sequencia de Fibonacci em Python

#Forma 1

n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1


if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)

#=======================================================
#Forma 2

#valor = int(input("Digite o valor: "))
#a, b = 0, 1
#while (b < valor):
#       print (b)
#       a, b = b, a+b
#=======================================================

#=======================================================

