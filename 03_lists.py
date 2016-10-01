#OBS: as listas podem receber qualquer tipo de dados, e é possível inserir lista dentro de lista;

numbers = [0,1,2,3,4,5,6,7,8,9]; #criando uma lista de numeros
print(numbers) #resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

mix = ['Hello', 1, 4.2, ['Junior', 'Pleno', 'Senior']] #criando uma lista mista
print(mix) #resultado: ['Hello', 1, 4.2, ['Junior', 'Pleno', 'Senior']]

#Digamos que eu quero pegar só um valor, o princípio é o mesmo utilizado nas strings
print(mix[2]) #passando o indíce 2, terei o resultado: 4.2

print(mix[3]) #passando o indíce 3, terei o resultado: ['Junior', 'Pleno', 'Senior']
#nota-se que meu retorno foi uma lista inteira.

#Mas e se eu quiser apenas um valor de uma lista que está dentro de outra lista? é simples.
print(mix[3][0]) #passando primeiro o indíce 3 para buscar na primeira lista e
#depois o indíce 0 para buscar na lista que referencia o indíce 3, terei o resultado: 'Junior'


#Manipulação de listas
#Apagando através do valor, utiliza-se 'remove'
numbers.remove(9) #apagando o número 9
print(numbers) #resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8]

numbers.append(9) #adicionando o número 9
print(numbers) #resultado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Apagando através do indíce, utiliza-se 'del'
del(numbers[0]) #apagando o indíce 0
print(numbers) #resultado: [1, 2, 3, 4, 5, 6, 7, 8, 9]
