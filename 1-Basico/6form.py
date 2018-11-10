#ecoding:utf-8
#operador: %f (float), representa o tanto de casas decimais apos a virgula
#para inteiro usar %d 

total=float(input("Premio da Mega:"))
num=int(input("Numero de ganhadores: "))

print 'Cada uma vai receber R$ %.2f' %(total/num)
