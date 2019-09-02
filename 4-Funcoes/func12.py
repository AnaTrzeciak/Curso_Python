#ecoding:utf-8

#Curso Python: Argumento Posicional e Argumento Nomeado em funções (keyword arguments)
#Feito em 01/09/2019 por Ana Maria

def media(mat,fis,qui):
	media=(mat+fis+qui)/3
	print("Media: ",media)


#argumento posicional
media(8,9,10)

#argumento nominal
media(qui=10,mat=8,fis=9)

#========================================================================
#Variavel global (keyword global)
#definir fora da função e chamar na função usar global nome_variavel
#========================================================================
#Cosntante global

