'''
É uma maneira de construtir uma estrutura de repetição ou laço de repetição, onde o programa irá repetir
determinada instrução até que percorra todos os elementos e finalize.
--> Só é usado quando sabemos quantas vezes o bloco de código deve ser repetido. <--
Vamos entender um pouco sobre o for.

for(para) cada i(variável que eu criei para usar dentro do for, poderia ser qualquer nome) in(na) list.
ou seja percorre cada i na list, no caso o i é o indíce e list é a lista com um conjunto de indíces;
'''

list = [2, 4, 6, 8, 10] #atribuindo numeros a uma lista

#Criando um for para percorer todas os indíces de uma lista

for i in list: #for(para) cada i(variável que eu criei para usar dentro do for, poderia ser qualquer nome) in(na) list.
    print(i) #printa cada i, até chegar no fim da lista
'''
Resultado:
2
4
6
8
10
'''
#Basicamente o for vai percorer indíce por indíce da lista e o print dentro do bloco vai mostrar cada valor destes indíces.

print() #saltando uma linha
print("\n") #saltando duas linhas;

#Criando um for para percorer todos os indíces de uma lista, com um if que irá selecionar quais destes itens serão printados
for i in list: #for(para) cada i(variável que eu criei para usar dentro do for, poderia ser qualquer nome) in(na) list.
    if i > 5: #se o valor no indíce i for maior que 5, printa, senão não faz nada.
        print(i) #printa apenas os valores que são maiores que 5, até chegar no fim da lista
'''
Resultado:
6
8
10
'''
