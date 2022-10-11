# Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor e marcha. Crie também um método imprimir, que deve mostrar na tela os valores de todos os atributos. O atributo marcha indica em que marcha a moto se encontra no momento, sendo representado de forma inteira. Onde: 0 - neutro, 1 - primeira, 2 - segunda, etc.
# Adicione os métodos marcha_acima e marcha_abaixo, que deverão efetuar a troca de marchas, onde o método marcha_acima sobe uma marcha e o método marcha_abaixo deverá realizar o oposto.
# Crie os atributos maior_marcha, onde o atributo maior_marcha indica qual será a maior marcha possível para a moto. Desta forma os métodos marcha_acima e marcha_abaixo devem ser reescritos de forma a não permitirem a troca de marchas para valores abaixo do esperado. O método imprimir deve ser modificado de forma a mostrar na tela os valores de todos os atributos.
# Construa os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligada conforme o caso.

class Moto:

    def __init__(self, marca: str, modelo: str, cor: str, maior_marcha: int) -> None:
        self.__marca = marca.strip().title()
        self.__modelo = modelo.strip().title()
        self.__cor = cor.strip().title()
        self.__marcha = 0
        self.__maior_marcha = maior_marcha
        self.__ligada = False
    
    def __str__(self) -> str:
        return f'Marca: {self.__marca} // Modelo: {self.__modelo} // Cor: {self.__cor} // Marcha atual: {self.__marcha} '
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ GETTERS E SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @property # ~~~~~~~~~~~~~~~~ GETTER E SETTER DA MARCA ~~~~~~~~~~~~~~~~~~~~~~~
    def get_marca(self) -> str:
        return self.__marca.strip().title()
    
    @get_marca.setter
    def set_marca(self, valor) -> None:
        if isinstance(valor, str): # VERIFICANDO SE O VALOR É COMPÁTIVEL
            self.__marca = valor.strip().title()
        else:
            print('É necessário que passe um valor do tipo string.')
    

    @property # ~~~~~~~~~~~~~~~~ GETTER E SETTER DO MODELO ~~~~~~~~~~~~~~~~~~~~~~
    def get_modelo(self) -> str:
        return self.__modelo.strip().title()
    
    @get_modelo.setter
    def set_modelo(self, valor) -> None:
        if isinstance(valor, str): # VERIFICANDO SE O VALOR É COMPÁTIVEL
            self.__modelo = valor.strip().title()
        else:
            print('É necessário que passe um valor do tipo string.')

    @property # ~~~~~~~~~~~~~~ GETTER E SETTER DA COR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_cor(self) -> str:
        return self.__cor.strip().title()
    
    @get_cor.setter
    def set_cor(self, valor) -> None:
        if isinstance(valor, str): # VERIFICANDO SE O VALOR É COMPÁTIVEL
            self.__cor = valor.strip().title()
        else:
            print('É necessário que passe um valor do tipo string.')
    
    
    @property # ~~~~~~~~~~~~~~ GETTER E SETTER DA MARCHA ~~~~~~~~~~~~~~~~~~~~~~~~~~
    def get_marcha(self) -> int:
        return self.__marcha
        
    @get_marcha.setter
    def set_marcha(self, valor) -> None:
        if self.__ligada: # VERIFICANDO SE A MOTO ESTÁ LIGADA.
            if isinstance(valor, int): # VERIFICANDO SE O VALOR É COMPÁTIVEL
                if valor >= 0 and valor <= self.__maior_marcha:
                    self.__marcha = valor
                else:
                    print(f'O valor precisa ser maior/igual a zero e menor/igual a {self.__maior_marcha}.')
            else:
                print('Necessário um valor número do tipo int.')
        else:
            print('Ligue a moto.')
      
    
    @property # ~~~~~~~~~~~~~~ GETTER E SETTER DA MAIOR MARCHA ~~~~~~~~~~~~~~~~~~~~~~~~
    def get_maior_marcha(self) -> int:
        return self.__maior_marcha
    
    @get_maior_marcha.setter
    def set_maior_marcha(self, valor) -> None:
        if isinstance(valor, int): # VERIFICANDO SE O VALOR É COMPÁTIVEL
            if valor > 0:
                self.__maior_marcha = valor
            else:
                print('O valor deve ser maior que a menor marcha possível.')
        else:
            print('Necessário um valor número do tipo int.')
        
    
    @property # ~~~~~~~~~~~ GETTER PARA VERIFICAR SE ESTÁ LIGADA OU DESLIGADA ~~~~~~~~~~
    def get_ligada(self) -> bool:
        return self.__ligada


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MÉTODOS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def imprimir(self) -> str:
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')
        print(f'Cor: {self.__cor}')
        print(f'Maior marcha: {self.__maior_marcha}')
        print(f'Marcha atual: {self.__marcha}')
        print(f'A moto está ligada? {self.__ligada}')


    def marcha_acima(self) -> str:
        if self.__ligada: # VERIFICANDO SE A MOTO ESTÁ LIGADA.
            if self.__marcha >= 0:
                if self.__marcha < self.__maior_marcha:
                    self.__marcha += 1
                    print('Subindo marcha.')
                else:
                    print(f'A marcha não pode ser maior que {self.__maior_marcha}. ')
            else:
                print('A marcha não pode ser menor que 0.')
        else:
            print('Ligue a moto.')
    

    def marcha_abaixo(self) -> str:
        if self.__ligada: # VERIFICANDO SE A MOTO ESTÁ LIGADA.
            if self.__marcha <= self.__maior_marcha:
                if self.__marcha > 0:
                    self.__marcha -= 1
                    print('Descendo marcha.')
                else: 
                    print('Para voltar uma marcha é necessário que a marcha seja maior que 1.')
        else:
            print('Ligue a moto.')
    

    def ligar(self) -> None:
        if self.__ligada == False:
            self.__ligada = True
    

    def desligar(self) -> None:
        if self.__ligada == True:
            self.__ligada = False