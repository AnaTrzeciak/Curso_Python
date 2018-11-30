#ecoding:utf-8
#função round(): arredonda um numero
#se o número flutuante estiver igual distância entre o inteiro de cima e o inteiro de baixo, ela arredonda pro número par mais proximo
#arrendondar um float com casa decimais, sintaxe: round( numero, n ) onde numero é a variavel e n é o numero de casas decimais

#arredondar para cima: round(num - 0.5)
#arredondar para baixo: round(num + 0.5)

#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero=input("digite um numero:")

print(type(numero))
print "Arredondado: ",round(numero)
print "Aproximacao por casas decimais: ",round(numero,3)
print "Arredondado para cima: ",round(numero+0.5)
print "Arredondado para baixo: ",round(numero-0.5)
