'''
É uma maneira de construtir uma estrutura condicional, onde o programa terá mais de um caminho,
porém só poderá seguir um, de acordo com instruções recebidas previamente.
Vamos entender um pouco sobre o if(se), elif(se senão), else(senão)
'''
note1 = 8; #nota1 recebe o valor 8;
note2 = 6; #nota2 recebe o valor 6;
average = (note1 + note2) / 2;  #average recebe a média entre a nota1 + nota2

if average >= 6: #se a média for maior ou igual a 6
    print('Aprovado\nNota:',average) #printa Aprovado e na próxima linha Nota:, passando o valor da média
elif average >= 4: #se a média for maior ou igual a 4
    print('Recuperação\nNota:',average) #printa Recuperação e na próxima linha Nota:, passando o valor da média
else: #senão (se a média não for nenhuma das opções acima)
    print('Reprovado\nNota:',average) #printa Reprovado e na próxima linha Nota:, passando o valor da média

#OBS: nota-se que o bloco para cada condição é definido através da identação
