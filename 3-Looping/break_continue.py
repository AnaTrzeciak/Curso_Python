#ecoding:utf-8

#================================================================
#While + Else

#while TESTE:
#    codigo
#    codigo
#    ...
#else:
#    codigo
#    ...

#Enquanto o TESTE for verdadeiro, ele roda o código dentro do WHILE.Quando a condição vira falso, e não se usa uma instrução BREAK, o código do ELSE será executado (com uma mensagem de saída, de desligamento de sistema, por exemplo).

#================================================================

#Instrução BREAK: A função do BREAK é simplesmente parar o looping. Se fizer um teste, ele der positivo e você usar a break, o laço é automaticamente findado.
#Sintaxe:

#while TESTE:
#    codigo
#    if TESTE2:
#       break;
#    ...
#=================================================================
#Instrução CONTINUE: Se ao invés de break usar continue, o laço não é terminado. Porém, ele pula do continue pro início do laço, tudo que tem ali em diante do continue não é mais executado.

#=================================================================

#Exercicio:Escreva um programa em Python que vai somar todos os números de 1 até 1 milhão, menos os que são múltiplos de 3.

soma_total= 0

for count in range(100000):
  count += 1
  if(count % 3 ==0):continue
  soma_total +=count

print(soma_total)
