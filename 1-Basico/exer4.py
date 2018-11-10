#ecoding:utf-8
#Você vai perguntar o valor inicial investido na poupança, a rentabilidade mensal, quantos meses o cliente deseja deixar o dinheiro investido e mostrar o valor final na conta do cliente do banco.

#equação da poupança: Vf=Vi*(1+i)^(m)
#Vf:valor final na poup
#Vi: valor inicial investido
#i:rentabilidade da poupança
#m:tanto de meses que o dinheiro vai ficar rendendo

print 'Bem vindo a poupança do Banco Poupedi.\n'
vi=float(input('Valor inicial:R$'))
i=float(input('Rentabilidade mensal (%):'))
i=i/100
m=int(input('Meses de rendimento:'))

vf=vi*(1+i)**m

print 'Valor rendido apos ',m,' meses com uma rentabilidade mensal de ',i,':R$',vf
