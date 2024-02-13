class Restaurante:
    #atributos da classe
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
restaurante_praca.ativo = True

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizzaria La Vint'
restaurante_pizza.categoria = 'Italiana'
restaurante_pizza.ativo = True

restaurantes = [restaurante_praca, restaurante_pizza]

print(dir(restaurantes)) # verifica os métodos, atributos e propriedades
print(vars(restaurantes)) # verifica o dicionário desses métodos, atributos e propriedades 