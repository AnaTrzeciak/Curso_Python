#ecoding: utf-8
#Operadores lógicos and, or e o not

#operador or
#Sintaxe: 
#if condição1 or condição2 or condição3 or ... :
#   [código]    Caso qualquer condição seja verdadeira
#   [código]    Esse código vai ser executado
#else:

#   [código]    Caso todas as condições sejam falsas
#   [código]    esse código vai ser executado

print "1-IDOSO\n2-GESTANTE\n3-CADEIRANTE\n"
resposta=int(input("Voce é: "))

if (resposta==1) or (resposta==2) or (resposta==3):
	print"Voce tem direito a fila preferencial.\n"
else:
	print"Vá para a fila normal.\n"
