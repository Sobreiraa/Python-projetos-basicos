''' Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares do prédio, excluindo o térreo, capacidade do elevador e quantas pessoas estão presentes nele. A classe também deve disponibilizar os seguintes métodos:
    * Inicializa: deve receber como parâmetro a capacidade do elevador e o  total de andares do prédio (os elevadores sempre começam no térreo e vazio);
    * Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
    * Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
    * Sobe: para subir um andar (não deve subir se já estiver no último andar);
    * Desce: para descer um andar (não deve descer se já estiver no térreo);
    * Encapsular todos os atributos da classe (criar os métodos set e get).
'''

class Elevador:

    def __init__(self) -> None:
        self.__andar_atual = 0 # Andar atual do elevador
        self.__total_andares = 0 # Total de andares do elevador
        self.__pessoas_elevador = 0 # Pessoas presentes no elevador
        self.__capacidade_pessoas = 0 # Capacidade total de pessoas no elevador
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GETTERS E SETTERS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ Getter e Setter do atributo andar_atual ~~~~~~~~~~~~~~~~~~~~~~~~~

    @property
    def get_andar_atual(self) -> int:
        return self.__andar_atual
    
    @get_andar_atual.setter
    def set_andar_atual(self, valor) -> str:
        if isinstance(valor, int): # Verificando se o valor é do tipo int.
            if valor < 0: # Verificando se o valor é negativo.
                self.__andar_atual = 0 # Atribuindo valor neutro.
            elif valor > self.__total_andares: # Verificando se o valor é maior do que o permitido.
                self.__andar_atual = self.__total_andares # Recebendo o mesmo valor que o permitido.
            else:
                self.__andar_atual = valor # Recebendo o valor que o usuário solicitou.
        else:
            print('Digite um valor do tipo int.')
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ Getter e Setter do atributo total_andares ~~~~~~~~~~~~~~~~~~~~~~~~~

    @property
    def get_total_andares(self) -> int:
        return self.__total_andares
    
    @get_total_andares.setter
    def set_total_andares(self, valor) -> str:
        if isinstance(valor, int): # Verificando se o valor é do tipo int.
            if valor <= 0:  # Verificando se o valor é negativo.
                self.__total_andares = 10 # Atribuindo valor positivo.
            else:
                self.__total_andares = valor # Recebendo o valor que o usuário solicitou.
        else:
            print('Digite um valor do tipo int.')

    # ~~~~~~~~~~~~~~~~~~~~~~~~ Getter e Setter do atributo pessoas_elevador ~~~~~~~~~~~~~~~~~~~~~~~~

    @property
    def get_pessoas_elevador(self) -> int:
        return self.__pessoas_elevador
    
    @get_pessoas_elevador.setter
    def set_pessoas_elevador(self, valor) -> str:
        if isinstance(valor, int): # Verificando se o valor é do tipo int.
            if valor < 0: # Verificando se o valor é negativo.
                self.__pessoas_elevador = 0 # Atribuindo valor neutro.
            elif valor > self.__capacidade_pessoas: # Verificando se o valor é maior do que o permitido.
                self.__pessoas_elevador = self.__capacidade_pessoas # Recebendo o mesmo valor que o permitido
            else:
                self.__pessoas_elevador = valor # Recebendo o valor que o usuário solicitou.
        else:
            print('Digite um valor do tipo int.')

    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ Getter e Setter do atributo total_andares ~~~~~~~~~~~~~~~~~~~~~~~~~

    @property
    def get_capacidade_pessoas(self) -> int:
        return self.__capacidade_pessoas
    
    @get_capacidade_pessoas.setter
    def set_capacidade_pessoas(self, valor):
        if isinstance(valor, int): # Verificando se o valor é do tipo int.
            if valor <= 0: # Verificando se o valor é negativo.
                self.__capacidade_pessoas = 10 # Atribuindo valor positivo.
            else:
                self.__capacidade_pessoas = valor # Recebendo o valor que o usuário solicitou.
        else:
            print('Digite um valor do tipo int.')
    
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ MÉTODOS DO OBJETO ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def inicializa(self, total_andares, capacidade_pessoas) -> None: # Método para iniciar o elevador com capacidade de pessoas e total de andares.
        if total_andares <= 0 or capacidade_pessoas <= 0: # Conferindo se a cap_pessoas e total_andares é maior que zero.
            self.__capacidade_pessoas = 10 # Atribuindo valores positivos.
            self.__total_andares = 10 # Atribuindo valores positivos.
        else:
            self.__capacidade_pessoas = capacidade_pessoas  # Recebendo o valor que o usuário solicitou.
            self.__total_andares = total_andares # Recebendo o valor que o usuário solicitou.
            

    def entra_pessoa(self) -> str: # Método para entrar uma pessoa no elevador.
        if self.__pessoas_elevador < self.__capacidade_pessoas: # Conferindo se o elevador está cheio.
            self.__pessoas_elevador += 1 # Adicionando uma pessoa no elevador.
            print('Uma pessoa está entrando no elevador.')
        else:
            print('Elevador lotado, espere o próximo.')


    def sai_pessoa(self) -> str: # Método para sair uma pessoa do elevador.
        if self.__pessoas_elevador > 0: # Conferindo se tem alguém no elevador.
            self.__pessoas_elevador -= 1 # Saindo uma pessoa do elevador.
            print('Uma pessoa está saindo do elevador.')
        else:
            print('Impossível sair alguém, o elevador está vazio.')
    

    def sobe_andar(self) -> str: # Método para subir um andar.
        if self.__pessoas_elevador > 0:
            if self.__andar_atual < self.__total_andares: # Conferindo se o andar atual está abaixo do total máximo de andares.
                self.__andar_atual += 1 # Subindo um andar.
                print('Subindo 1 andar.')
            else:
                print('Impossível subir mais, o elevador está na cobertura.')
        else:
            print('Para subir um andar é necessário que tenha ao menos 1 pessoa no elevador.')


    def desce_andar(self) -> str: # Método para descer um andar.
        if self.__pessoas_elevador > 0:
            if self.__andar_atual > 0: # Conferindo se o andar atual está acima do térreo.
                self.__andar_atual -= 1 # Descendo um andar.
                print('Descendo 1 andar.')
            else:
                print('Impossível descer mais, o elevador está no térreo.')
        else:
            print('Para descer um andar é necessário que tenha ao menos 1 pessoa no elevador.')
