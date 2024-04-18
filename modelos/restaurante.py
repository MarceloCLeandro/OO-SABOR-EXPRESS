class Restaurante:

    restaurantes = []

    #atributos da classe
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        
    def _str_(self): return f'{self._nome} {self._categoria}'

    
    #Métodos da Classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')


    #Atributos Especiais 
    @property
    def ativo(self):
        return '✔️' if self._ativo else '❌'


    
    #Métodos para os Objs
    def alternar_estado(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()

restaurante_pizza = Restaurante('pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

#print(dir(restaurantes)) # verifica os métodos, atributos e propriedades
#print(vars(restaurantes)) # verifica o dicionário desses métodos, atributos e propriedades 

Restaurante.listar_restaurantes()