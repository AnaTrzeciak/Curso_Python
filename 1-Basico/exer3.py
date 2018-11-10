#ecoding:utf-8
#A loja percebeu que não quer dar 20% em tudo. Quer dar 20% em algumas coisas, 10% em outra, nada em outro produto e até 30% em alguns outros produtos.
#Crie um script em Python que pergunte o preço original e o desconto que deve ser concedido.

#print 'Olá, bem vindo a nossa loja. Por favor informe o valor do produto e valo do desconto (não precisa por % para o valor desconto.'

# Vamos pedir o valor original do produto
valor_original = float( input("Valor original: R$ ") )

# Desconto que será concedido
desconto = float( input("Desconto (em %) para esse produto: ") )

# Transformando a porcentagem em número decimal
desconto = desconto / 100

# Exibindo tudo
print('Valor original:     R$', valor_original)
print('Desconto ganho:     R$', valor_original * desconto)
print('Valor com desconto: R$', valor_original * (1-desconto) )
