# Escreva um código que apresente a classe Televisor, com atributos ligado, canal e volume. Adicione um método imprimir que deve mostrar na tela os valores de todos os atributos. O atributo ligado será boleano e deverá indicar o estado atual do televisor, se ligado ou desligado. O atributo canal deverá indicar o canal atual em que o televisor está sintonizado. O atributo volume deverá indicar o volume atual do televisor. Crie ou herde os métodos ligar e desligar do eletrodoméstico. Crie os atributos numero_canais e volume_maximo, onde numeros_canais indica o número máximo de canais que o televisor pode sintonizar e o volume_maximo indica qual o maior nível de volume possível. O método imprimir deve ser modificado de forma a mostrar na tela os valores de todos os atributos. Faça também os métodos canal_acima e o canal_abaixo, sendo que o método canal_acima deve sintonizar sempre o próximo canal em relação ao canal atual, onde ao chegar ao maior canal possível deverá voltar ao canal 1. O método canal_abaixo deve sintonizar sempre o canal anterior em relação ao canal atual, onde chegar ao canal 1 deverá voltar ao maior canal possível, simulando desta forma o funcionamento de um televisor. E por último adicione os métodos volume_acima e volume_abaixo, sendo que o método volume_acima deve modificar o volume para o próximo nível de volume possível, onde ao chegar ao volume_maximo não poderá possibilitar que o volume seja alterado. O método volume_abaixo deve modificar o volume para o nível imediatamente inferior de volume em relação ao volume atual, não podendo ser menor do que 0, simulando desta forma o funcionamento de um televisor.


from eletrodomestico import Eletrodomestico

class Televisor(Eletrodomestico):
    
    def __init__(self, numero_canais: int, volume_maximo: int, canal: int, volume: int) -> None:
        super().__init__()
        self.__numeros_canais = numero_canais
        self.__volume_maximo = volume_maximo
        self.__canal = canal
        self.__volume = volume
        self._verifica_valores_canal() # Usando um método dentro do construtor.
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GETTERS E SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# GETTERS E SETTERS DO NÚMERO DE CANAIS
    @property
    def get_numero_canais(self) -> int:
        return self.__numeros_canais
    
    @get_numero_canais.setter
    def set_numero_canais(self, valor) -> None:
        if self._Eletrodomestico__ligado: # Conferindo se o eletrodoméstico está ligado.
            if isinstance(valor, int): # Conferindo se o valor é uma instância do tipo inteiro
                if valor <= 0: # Verificando se o valor é maior que 0.
                    self.__numeros_canais = 10
                else:
                    self.__numeros_canais = valor
            else:
                print('É necessário um valor númerico do tipo inteiro.')
        else:
            print('Ligue a televisão.')


    # GETTERS E SETTERS DO VOLUME MÁXIMO
    @property
    def get_volume_maximo(self) -> int:
        return self.__volume_maximo
    
    @get_volume_maximo.setter
    def set_volume_maximo(self, valor):
        if self._Eletrodomestico__ligado: # Conferindo se o eletrodoméstico está ligado.
            if isinstance(valor, int): # Conferindo se o valor é uma instância do tipo inteiro
                if valor <= 0: # Verificando se o valor é maior que 0.
                    self.__volume_maximo = 10
                else:
                    self.__volume_maximo = valor
            else:
                print('É necessário um valor númerico do tipo inteiro.')
        else:
            print('Ligue a televisão.')


    # GETTERS E SETTERS DO CANAL
    @property
    def get_canal(self) -> int:
        return self.__canal
    
    @get_canal.setter
    def set_canal(self, valor) -> None:
        if self._Eletrodomestico__ligado: # Conferindo se o eletrodoméstico está ligado.
            if isinstance(valor, int): # Conferindo se o valor é uma instância do tipo inteiro.
                if valor <= 0: # Verificando se o valor é maior que 0.
                     self.__canal = 1
                else:
                    if valor > self.__numeros_canais: # Conferindo se o canal atual é maior que o número de canais.
                        self.__canal = self.__numeros_canais
                    else:
                        self.__canal = valor
            else:
                print('É necessário um valor númerico do tipo inteiro.')
        else:
            print('Ligue a televisão.')

    
    # GETTERS E SETTERS DO VOLUME
    @property
    def get_volume(self) -> int:
        return self.__volume
    
    @get_volume.setter
    def set_volume(self, valor) -> None:
        if self._Eletrodomestico__ligado: # Conferindo se o eletrodoméstico está ligado.
            if isinstance(valor, int): # Conferindo se o valor é uma instância do tipo inteiro.
                if valor <= 0: # Verificando se o valor é maior que 0.
                    self.__volume = int(self.__volume_maximo / 2) # Se o valor for menor que zero, o volume recebe a metade do volume máximo permitido.
                else:
                    if valor > self.__volume_maximo: # Conferindo se o volume atual é maior que o volume máximo.
                        self.__volume = self.__volume_maximo
                    else:
                        self.__volume = valor
            else:
                print('É necessário um valor númerico do tipo inteiro.')
        else:
            print('Ligue a televisão.')


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MÉTODOS DO OBJETO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def imprimir(self) -> str: # Método para imprimir todos os atributos.
        print(F'Número de canais: {self.__numeros_canais}')
        print(F'Canal atual: {self.__canal}')
        print(F'Número máximo do volume: {self.__volume_maximo}')
        print(F'Volume atual: {self.__volume}')
        print(F'Televisão está ligada? {self._Eletrodomestico__ligado}')


    def _verifica_valores_canal(self) -> str: # Método para verificar se tem algum dado inválido.
        if self.__canal or self.__numeros_canais <= 0: # Verificando se o canal ou o número de canais é menor que 0.
            self.__canal = 1
            self.__numeros_canais = 10
            print('Alterando valores de dados inválidos.')
        if self.__canal > self.__numeros_canais: # Conferindo se o canal atual é maior que o número de canais.
            self.__canal = self.__numeros_canais
            print('Alterando valores de dados inválidos.')

    
    def _verifica_valores_volume(self) -> str: # Método para verificar se tem algum dado inválido.
        if self.__volume or self.__volume_maximo <= 0: # Verificando se o volume ou o volume máximo é menor que 0.
            self.__volume = int(self.__volume_maximo / 2)
            self.__volume_maximo = 10
            print('Alterando valores de dados inválidos.')
        if self.__volume >= self.__volume_maximo: # Conferindo se o volume atual é maior que o volume permitido.
            self.__volume = self.__volume_maximo
            print('Alterando valores de dados inválidos.')
    
    def canal_acima(self) -> None:
        if self._Eletrodomestico__ligado: # Conferindo se o eletrodoméstico está ligado.
            if self.__canal == self.__numeros_canais:
                self.__canal = (self.__canal - self.__numeros_canais) +1 # Voltando ao canal 1, pois não dá para subir de canal se estiver no máximo.
            else:
                self.__canal += 1
        else:
            print('Ligue a televisão.')
    
    
    def canal_abaixo(self) -> None:
        if self._Eletrodomestico__ligado: # Conferindo se o eletrodoméstico está ligado.
            if self.__canal == 1:
                self.__canal = self.__numeros_canais + 1
            self.__canal -= 1
        else:
            print('Ligue a televisão.')
    

    def volume_acima(self) -> str:
        if self._Eletrodomestico__ligado: # Conferindo se o eletrodoméstico está ligado.
            if self.__volume == self.__volume_maximo: # Conferindo se o volume já está no máximo.
                print('Volume está no máximo. Impossível aumentar mais.')
            else:
                self.__volume += 1
        else:
            print('Ligue a televisão.')
    

    def volume_abaixo(self) -> str:
        if self._Eletrodomestico__ligado: # Conferindo se o eletrodoméstico está ligado.
            if self.__volume == 0:
                print('Volume está no mudo. Impossível diminuir mais.')
            else:
                self.__volume -= 1
        else:
            print('Ligue a televisão.')