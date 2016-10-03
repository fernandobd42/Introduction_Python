'''
Um dicionário é basicamente um dado composto por key(chave) e value(valor);
'''
cars = {} #definindo um dicionário
cars['Punto'] = 'black' #'Punto' é a chave e 'black' o valor
cars['Golf'] = 'grey' #'Golf' é a chave e 'grey' o valor
cars['Cruze'] = 'green' #'Cruze' é a chave e 'green' o valor

print(cars) #print(mostrar) todos atributos de todos os carros
'''
Resposta:
{'Golf': 'grey', 'Cruze': 'green', 'Punto': 'black'}
'''

#print(mostrar) o valor do 'Cruze'
print(cars['Cruze'])
'''
Resultado:
green
'''

#É possível buscar apenas as keys(chaves) de um dicionário
print(cars.keys())
'''
Resultado:
dict_keys(['Golf', 'Punto', 'Cruze'])
'''

#Também é possível buscar apenas os values(valores) de um dicionário
print(cars.values())
'''
Resultado:
dict_values(['grey', 'black', 'green'])
'''


#Iterando no dicionário para buscar as keys(chaves) no caso os carros no dicionário cars
for car in cars: #for(para) car(variável que eu criei para referênciar cada carro) in(em) cars
    print(car) #printa(mostra) car ou key(chave) de cada item do dicionário
'''
Resultado:
Golf
Punto
Cruze
'''

#Iterando no dicionário para buscar as keys(chaves) e os values(valores) no dicionário cars
for car in cars: #for(para) car(variável que eu criei para referênciar cada carro) in(em) cars
    print(car +" = "+cars[car]) #printa(mostra) o car ou a key(chave) = cars[car] ou o value(valor) de cada item do dicionário
'''
Resultado:
Cruze = green
Punto = black
Golf = grey
'''
#nota-se que funcionou, porém este metódo é caracterizado como uma gambiarra(forma errada).

#Agora iremos fazer uma iteração correta no dicionário cars para buscar as chaves e valores
for key, value in cars.items(): #for(para) key(chave) e value(valor) no dicionário in(em) cars.items()
    print(key +" = "+ value) #printa(mostra) key(chave) = value(valor) de cada item do dicionário
'''
Resultado:
Golf = grey
Cruze = green
Punto = black
'''
#nota-se que o resultado foi o mesmo da iteração anterior, porém desta forma o código fica mais claro e elegante.
