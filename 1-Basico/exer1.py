#encoding: utf-8

#Exercicio 1: Sua primeira tarefa é criar um programa em Python que pede o preço original de um produto e dá 20% de desconto.

print 'Bem Vindo a Lojas Havan. Voce ganhou 20% de Descontos na sua compra.'
preco_original=float(input("Digite o valor do produto: "))

valor_desconto=float(preco_original*0.20)

print '\nO desconto foi de R$',valor_desconto
valor_final=preco_original-valor_desconto

print '\nO valor do produto era:R$',preco_original,'. Com o desconto ficou em R$',valor_final
 
