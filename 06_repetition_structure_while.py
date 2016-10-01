'''
É outra maneira de construtir uma estrutura de repetição ou laço de repetição, onde o programa irá repetir
determinada instrução enquanto a condição for verdadeira.
--> É usado quando não sabemos de antemão quantas vezes o bloco de código deve ser repetido. <--
Vamos entender um pouco sobre while e do while.

while(enquanto) verifica a condição e só se ela for verdadeira que ele executa o bloco de instrução.
do(fazer) while(enquanto) ele executa o bloco de instrução uma vez e depois verifica.
'''

number = 0

while number < 10: #enquanto o número for menor que 10;
    print(number) #printa cada numero até que a condição se torne falsa;
    number = number+1 #cada vez que o programar chegar até aqui ele irá incrementar 1 no número;
'''
Resultado:
0
1
2
3
4
5
6
7
8
9

Vamos entender o while. a variável number começou com o valor 0; o metodo while diz que enquanto number for menor que 10,
execute o bloco, ou seja print(number)/mostre(number) e posterioemente execute parte mais importante do código no caso
a linha 15, que é onde ele incrementar o valor da variável number. básicamente na primeira vez que o programa chegar
até lá a variável number terá valor 0, apartir dai ela receberá seu valor atual mais 1, e o programar irá começar
novamente, enquanto a variável number que no caso agora tem 1 for menor que 10, execute o bloco... de 0 a 10, o bloco será
executado 10 vezes até que a variável number seja maior ou igual a 10, uma vez que o while faz a condição se referindo aos
números que são menores que 10, não incluindo o número 10;
'''

print()
n = 0

while n <= 10: #enquanto o número for menor ou igual a 10;
    print(n) #printa cada numero até que a condição se torne falsa;
    n+= 1 #cada vez que o programar chegar até aqui ele irá incrementar 1 no número;
'''
Resultado:
0
1
2
3
4
5
6
7
8
9
10

Nota-se que desta vez o bloco será executado 11 vezes, uma vez que o while faz a condição se referindo aos números menores
ou igual a 10, incluindo o número 10.
Nota-se também na linha 43, que é possível refatorar o código e ao invés de usar n = n + 1; podemos usar n += 1; para
incrementar 1.

'''
