#ecoding:utf-8
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
  

print "Bem vindo ao site das Organizações Tabajara, vamos calcular o aumento de acordo com o salário recebido\n"
print "salários até R$ 280,00 (incluindo) : aumento de 20% \nsalários entre R$ 280,00 e R$ 700,00 : aumento de 15% \nsalários entre R$ 700,00 e R$ 1500,00 : aumento de 10% \nsalários de R$ 1500,00 em diante : aumento de 5%" 

salario=float(input("Digite o salário:R$ "))
reajuste=int(input("Digite o reajuste (%): "))



if(salario<=280 and reajuste==20):
	print"Salario atual:R$",salario,"\nReajuste (%):",reajuste,"\nAumento:R$",salario*(reajuste/100.0),"\nNovo salário:R$",salario+(salario*(reajuste/100.0))

if(salario<700 and reajuste==15):
	print"Salario atual:R$",salario,"\nReajuste (%):",reajuste,"\nAumento:R$",salario*(reajuste/100.0),"\nNovo salário:R$",salario+(salario*(reajuste/100.0))

if(salario<1500 and reajuste==10):
	print"Salario atual:R$",salario,"\nReajuste (%):",reajuste,"\nAumento:R$",salario*(reajuste/100.0),"\nNovo salário:R$",salario+(salario*(reajuste/100.0))

if(salario>=1500):
	print"Salario atual:R$",salario,"\nReajuste (%):",reajuste,"\nAumento:R$",salario*(reajuste/100.0),"\nNovo salário:R$",salario+(salario*(reajuste/100.0))
