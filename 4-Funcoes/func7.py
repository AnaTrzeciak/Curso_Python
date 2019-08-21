#ecoding:utf-8
#Crie um script em Python que pede uma frase (string) ao usuário e em seguida um#caractere. Em seguida, seu script deve dizer quantas vezes aquele caractere apa#receu na frase digitar. Use função com parâmetros.

def conta_caractere(texto,char):
  count=0
  for letra in texto:
   if(letra==char):
     count+=1
  print(char," apareceu ",count," vezes na string")

string=input("Digite um texto qualquer: ")
caractere=input("Digite um caractere: ")

conta_caractere(string,caractere)
