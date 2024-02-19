class Restaurante:

    restaurantes = []

    #atributos da classe
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f' {self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_praca = Restaurante('Praça', 'Gourmet')

restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

#print(dir(restaurantes)) # verifica os métodos, atributos e propriedades
#print(vars(restaurantes)) # verifica o dicionário desses métodos, atributos e propriedades 

Restaurante.listar_restaurantes()