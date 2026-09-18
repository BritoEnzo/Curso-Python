"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

name = input('Digite o seu nome: ')
age = input('Digite a sua idade ')

# lenght =  len(name) -1 

# print(lenght)


print (f'seu nome invertido é : {name[::-1]}')


if " " in name:
    print ("Seu nome contem espaços")
else:
    print ('Seu Nome não contém espaços')

print(f'Seu nome contém: {len(name)} letras')

print(f'a primeira letra do seu nome é "{name [0]}"')

print(f'A última letra do seu nome é "{name[len(name) -1]}"')

if name == "" or age == "":
    print('Desculpe, você deixou campos vazios.')