#ecoding:utf-8
#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
    #Triângulo Equilátero: três lados iguais;
    #Triângulo Isósceles: quaisquer dois lados iguais;
    #Triângulo Escaleno: três lados diferentes;

print "Oi meu querido, digita os lados do triângulo ai pra mim."

lado1=float(input("Lado 1: "))
lado2=float(input("Lado 2: "))
lado3=float(input("Lado 3: "))

if(lado1+lado2<lado3 or lado1+lado3<lado2 or lado2+lado3<lado1):
	print "Não é triângulo"

elif(lado1==lado2 and lado1==lado3 and lado2==lado3):
	print "O triângulo é equilátero."

elif(lado1==lado2 or lado1==lado3 or lado2==lado3):
	print "O triângulo é isóceles."

else: #lado1!=lado2 and lado1!=lado3 and lado2!=lado3:
	print "O triângulo é escaleno."
