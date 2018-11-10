#ecoding:utf-8

print 'Um novo tipo de carro foi lançado. Ele faz 20km com 1L de combustivel. Vamos saber o tanto que seu carro pode andar compativel com o seu tanto de dinheiro.\n'

din=float(input("Quanto dinheiro voce tem:R$"))
com=float(input("Informe o preço do combustivel:R$"))

litro=din/com  #tanto de litros de combustivel que ele consegue comprar com o dinheiro

distancia=litro*20

print 'Com R$',din,' voce consegue comprar %0.2f'%litro,' litros de combustivel. E seu carro conseguirá andar %0.2f'%distancia,' km.'


