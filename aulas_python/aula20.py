"""
Exercicio de lógica:

Solicitar que o usuario insira dois valores, e realizar a lógica para imprimir ao final do programa qual valor digitado é maior
"""

primeiro_valor = input('Digite o valor de um número: ')
segundo_valor = input('Digite o valor de um número: ')

if primeiro_valor > segundo_valor:
    print (f"O primeiro valor ({primeiro_valor}) é maior do que o segundo valor ({segundo_valor})")
elif primeiro_valor == segundo_valor:
    print (f"O primeiro valor ({primeiro_valor}) é igual ao segundo valor ({segundo_valor})")
else:
    print (f"O segundo valor ({segundo_valor}) é maior do que o primeiro valor ({primeiro_valor})")