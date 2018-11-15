#ecoding: utf-8

#if True:
#    [codigo]    Se a condição for verdadeira
#    [codigo]     o codigo indentado abaixo do if
#    [codigo]     será executado
#else:
#    [codigo]    Este bloco de código só funciona
#    [codigo]    se a condição for falsa

#if 1:
#	print"estou no if"
#else:
#	print"nao vou ser printado"

#O código acima vai sempre executar o IF, pois o número 1 retorna TRUE.

#========================================================

print"1-Londrina \n 2-Maringá\n"

time=int(input("Qual time voce torce? (digite o numero correspondente)\n"))

if time==1:
	print"Voce é londrinense"
else:
	if time==2:
	 print"Voce é maringaense."
	else:
	 print"Voce não torce pra nenhum dos dois."



