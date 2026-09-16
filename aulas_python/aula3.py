"""
O python é uma linguagem dinamica e que interpreta as variaveis dinamicamente, ou seja, não precisamos declarar o tipo da variavel 
antes de usá-la, o interpretador do python irá inferir o tipo da variavel com base no valor que ela recebe.
"""

nome = "joao"
idade = 23

#para ler uma string, basta colocá-la entre aspas simples ou duplas, e para ler um número inteiro, basta digitá-lo sem aspas.

print("Rodrigo Faro")

print('Rodrigo Faro')

"""caso seja necessário utilizar algum tipo de aspas dentro de uma string, é necessário utilizar um operador de escape (barra invertida)
que pula o próximo caractere fazendo assim que o interpretador não leia ele como um tipo de aspas e evitando que a string seja encerrada"""

print("o \"Rodrigo Faro\" é um grande apresentador")

"""Um truque para utilizar as aspas duplas/aspas simples dentro de uma string sem que a mesma seja fechada é utilizar elas de forma alternada,
ou seja, caso eu queira utilizar aspas duplas dentro do meu texto, eu inicio o meu texto com aspas simples e vice versa"""

print('O "Rodrigo Faro" é um grande apresentador')

print('explicito', 'é', 'melhor " do que implicito')

print("Meu nome é", nome, "e minha idade é :", idade + 2)