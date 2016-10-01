'''
Funções, basicamente são subprogramas, dentro de um programa maior, utilizados para realizar uma tarefa específica.
'''

def say_hello():  #def define uma função, say_hello foi o nome que eu dei
  return "Hello World" #return define o retorno desta função
#OBS:a identação(espaçamento) define o bloco que faz parte função

print(say_hello()) #print(mostra) a função definida acima
'''
Resultado:
Hello World
'''
#Acima mostramos uma função bastante simples, que retorna uma string.

#Agora vamos criar uma função um pouco mais complexa;
def numbers_with_limit(limit): #definindo a função numbers_with_limit que receberá o parâmetro limit
    list = range(0,5) # definindo uma lista com intervalo entre 0 e 5
    for number in list[0:limit]: #percorrendo a lista numero por numero do intervalor 0 até o limit
#o limit será passado na hora da invocação da função.
        print(number) #printando(mostrando) os numeros que estão entre o intervalor de 0 até limit.

numbers_with_limit(3) #invocando a função atribuindo o numero 3 ao limit
'''
Resultado:
0
1
2
'''

print()
#outra maneira de criar uma mesma função seria,
def numbers_with_limit2(limit): #definindo a função numbers_with_limit2 que receberá o parâmetro limit
    for number in range(limit): #percorrendo a lista numero por numero, até alcançar o limit
#o qual será passado na hora da invocação da função.'''
        print(number) #printando(mostrando) os numeros que estão entre o intervalor de 0 até limit.

numbers_with_limit2(12) #invocando a função atribuindo o numero 12 ao limit
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
11
'''
