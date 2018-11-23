#ecoding: utf-8
#Operadores lógicos and, or e o not

#operador and
#Todos os testes devem ser true, para o resultado ser true. Se um deles for false, o resultado é falso.

resposta=int(input("Qual a sua idade: "))

if resposta>=18 and resposta<=65:
	print "Voce é obrigado a votar! \n"
else:
	print "Voce não é obrigado a votar! \n"

