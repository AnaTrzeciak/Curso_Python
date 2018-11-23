#ecoding:utf-8
#Programa que converte notas.

nota=float(input("Aluno, digite sua nota: "))

if nota<6.0:
	print "NOTA F"
elif nota<7.0:
	print "NOTA D"
elif nota<8.0:
	print "NOTA C"
elif nota<9.0:
	print "NOTA B"
else: 
	print "NOTA A"

