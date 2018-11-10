#encoding: utf-8
#criar um programa em Python que pede o preço original de um produto e dá 20% de desconto.

valor_original=float(input("Informe o valor do produto: "))
print valor_original

print'\nVocê ganhou 20% de desconto, portanto o valor da sua compra final é: '

desconto=float(valor_original*0.20)
valor_desconto=float(valor_original-desconto)

print 'VALOR ORIGINAL:R$',valor_original
print 'DESCONTO:R$',desconto
print 'VALOR FINAL:R$',valor_desconto
