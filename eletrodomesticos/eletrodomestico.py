# Escreva um código que apresente a classe Eletrodoméstico, com atributo ligado e o método imprimir. O método imprimir deve mostrar na tela os valores de todos os atributos. O atributo ligado será boleano e deverá indicar o estado atual do eletrodoméstico, se ligado ou desligado. Crie os métodos ligar e desligar, que deverão mudar o conteúdo do atributo ligado conforme o caso.

class Eletrodomestico:
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTRUTOR ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self) -> None:
        self.__ligado = False
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ GETTER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    @property
    def get_ligado(self) -> bool:
        return self.__ligado
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ MÉTODOS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def imprimir(self) -> str:
        print(f'O eletrodoméstico está ligado? {self.__ligado}')
    

    def ligar(self) -> None:
        if not self.__ligado:
            self.__ligado = True
    
    def desligar(self) -> None:
        if self.__ligado:
            self.__ligado = False
