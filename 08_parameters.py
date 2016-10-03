'''
Existem dois tipos de parâmetros:
Parâmetros formais são aqueles passados na hora da criação do subprograma.
Parâmetros reais são aqueles passados na hora da invocação do subprograma.
'''

#nota-se que em python é possível passar valores padrão na hora de passar os parâmetros formais.
#os valores padrão servem para no caso a função seja invocada sem receber nenhum parâmetro real, ela utiliza os valores padrão.
def average(note1=6, note2=6, note3=6, note4=6): #criando uma função com 4 parâmetros.
    av = (note1 + note2 + note3 + note4) / 4; #atribuindo a média das 4 notas para a variável av
    if av >= 6: #iniciando uma estrutura condicional para definir em qual das 3 opções o aluno se encontra, de acordo com sua média.
        print("Aprovado \nNota:", av)
    elif av >= 4:
        print('Recuperação \nNota:', av)
    else:
        print('Reprovado \nNota:', av)

average() #invocando a função sem passar parâmetros, no caso ela irá executar com os valores padrão.
'''
Resultado:
Aprovado
Nota: 6.0
'''
print()
average(7,5,5,6) #invocando a função passando 4 parâmetros reais.
'''
Resultado
Recuperação
Nota: 5.75
'''
