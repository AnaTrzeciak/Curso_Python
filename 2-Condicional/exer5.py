#ecoding:utf-8
#Raizes de uma equação de segundo grau

import math

print "Forma geral da Eq. de 2° grau: ax^(2)+bx + c=0. Para achar as raízes voce precisa informar a, b e c."

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta=b*b - (4*a*c)
if a==0:
	print "Não é uma equação de 2° grau."
elif(delta<0):
	print "A equação possui raízes no campo dos complexos."
elif(delta==0):
	print "Possui apenas uma raiz real. x_1=",(-b)/(2*a)
else:
	print"Possui duas raízes reais. x_1=",((-b)/(2*a))+math.sqrt(delta)/(2*a),"\n x_2= ",((-b)/(2*a))-math.sqrt(delta)/(2*a)
		
