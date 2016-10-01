print("Hello World\nYou're Welcome"); # \n é usado para pular uma linha, printa a frase dividida pelo \n em duas linhas
#Resultado:
#Hello World
#You're Welcome
print(r"Hello World\nYou're Welcome"); # r significa row, ou seja, ira printar a frase inteira de forma literal, sem saltar linha;
#Resultado
#Hello World\nYou're Welcome

name = 'Fernando'; #atribuindo um valor a variável name
last_name = 'Gontijo'; #atribuindo um valor a variável last_name
full_name = name +" "+last_name; #concatenando name com last_name
print(name); #printa o name, resultado: 'Fernando'
print(last_name); #printa o last_name, resultado: 'Gontijo'
print(full_name); #printa o full_name, resultado: 'Fernando Gontijo'

print(name[0]); #printa o caractere a posição 0 do name, resultado: 'F'

print(name[0:3]); #printa os caracteres que estão no intervalo entre a posição 0 e 3, resultado: 'Fer'
#OBS: quando se trata de intervalo, sempre será incluído o primeiro valor e será excluido o último valor.
#No exemplo acima o indíce 0 referencia a letra 'F' e o indíce 3 referencia a letra 'n', então o retorno será 'Fer'

print(full_name[6:11]); #printa os caracteres que estão no intervalo entre a posição 6 e 11
#o indíce 6 referencia a letra 'd' e o indíce 11 referencia a letra 'n', então o retorno será 'do Go'
