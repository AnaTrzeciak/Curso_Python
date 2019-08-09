#ecoding:utf-8
#Faça um programa que leia 5 números e informe a soma e a média dos números. 

print("Informe 5 numeros.")

num1= int(input("numero 1: "))
num2= int(input("numero 2: "))
num3= int(input("numero 3: "))
num4= int(input("numero 4: "))
num5= int(input("numero 5: "))

soma=(num1 + num2 + num3 + num4 + num5)
media= (soma/5)

print("A soma de todos eles é:", soma)
print("A media entre eles é: ",media)
