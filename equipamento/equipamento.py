# Crie uma classe equipamento com dois atributos privados, e uma classe computador com dois atributos privados a sua escolha. A classe computador deverá herdar tudo da classe equipamento. Crie os métodos de acesso e de modificação para todos os atributos definidos em ambas as classes. Faça uma classe TestaEquipamento, que deverá conter o método main(), crie nela um objeto da classe Equipamento e instancie os dois atributos que você declarou na classe equipamento. Adicione também um objeto da classe computador, utilizando os dois atributos delcarados na própria classe e os dois herdados da classe equipamento. O método main() deverá exibir as informações dos dois objetos criados. Crie o método exibe() na classe equipamento para mostrar os dados dessa classe. Reescreva o método exibe() na classe computador, aproveitando o que já está escrito na superclasse Equipamento

class Equipamento:

    def __init__(self, marca: str, modelo: str) -> None:
        self.__marca = marca
        self.__modelo = modelo
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GETTERS E SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @property 
    def get_marca(self) -> str:
        return self.__marca

    @get_marca.setter
    def set_marca(self, valor) -> str:
        if isinstance(valor, str): # Conferindo se o valor é válido.
            self.__marca = valor
        else:
            print('Precisamos de um valor do tipo stirng.')
    

    @property
    def get_modelo(self) -> str:
        return self.__modelo
    
    @get_modelo.setter
    def set_modelo(self, valor) -> str:
        if isinstance(valor, str): # Conferindo se o valor é válido.
            self.__modelo = valor
        else:
            print('Precisamos de um valor do tipo stirng.')
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MÉTODOS DO OBJETO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def exibe(self) -> str:
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')

  

class Computador(Equipamento):

    def __init__(self, marca, modelo, processador: str, hd: int) -> None:
        super().__init__(marca, modelo)
        self.__processador = processador
        self.__hd = hd

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GETTERS E SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @property
    def get_processador(self) -> str:
        return self.__processador

    @get_processador.setter
    def set_processador(self, valor) -> str:
        if isinstance(valor, str): # Conferindo se o valor é válido.
            self.__processador = valor
        else:
            print('Precisamos de um valor do tipo string.')

    
    @property
    def get_hd(self) -> int:
        return self.__hd
    
    @get_hd.setter
    def set_hd(self, valor) -> str:
        if isinstance(valor, int): # Conferindo se o valor é válido.
            if valor > 0: # Conferindo se o valor é maior que 1.
                self.__hd = valor
            else:
                self.__hd = 500
        else:
            print('Precisamos de um valor númerico do tipo int.')
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MÉTODOS DO OBJETO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def exibe(self) -> str:
        print(f'Processador: {self.__processador}')
        print(f'HD: {self.__hd}')
        return super().exibe()
    
        
class TestaEquipamento:

    def __init__(self) -> None:
        pass

    
    def main(self) -> None:
        equipamento1 = Equipamento('Lg', 'LG35') # Criando um objeto da classe equipamento.
        computador1 = Computador('Samsung', 'Samsung G5', 'I5900', 1000) # Criando um objeto da classe computador.
        print('Equipamento')
        equipamento1.exibe()
        print('-' * 50)
        print('Computador')
        computador1.exibe()
    
    
teste = TestaEquipamento()
teste.main()