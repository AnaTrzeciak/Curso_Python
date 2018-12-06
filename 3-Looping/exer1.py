#ecoding:utf-8
#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 

nota=0
while True:
  nota= int(input("Digite uma nota:"))
  if nota>10:
    print("A nota não é um valor aceitavel. Tente novamente")

#======================================================
#Solução do Python Progressivo

#nota = float(input("Insira uma nota 0 até 10: "))

#while (nota < 0) or (nota > 10):
#    nota = float(input("Não pode ser menor que 0 ou maior que 10 meu jovem!\n \
#    Tente novamente:"))
#print("Nota válida")
