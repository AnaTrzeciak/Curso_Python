#ecoding:utf-8
#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 

numero=int(input("Qual tabuada voce quer saber? Digite um numero de 1 a 10.\n"))

print(" Tabuada do ",numero,":\n")
for i in range(1,11):
 print(numero," X ",i," = ",numero*i, "\n")
 
