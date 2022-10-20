# Decida por mim
# Faça uma pergunta para o programa e ele terá que te dar uma resposta.

import random

class DecidaPorMim: 

    def __init__(self) -> None:
        self.__pergunta = '' # Aqui será a instância para a pergunta.
        self.__respostas = ['Sim', # Aqui estão as respostas.
        'Não',
        'Talvez',
        'Não entendi',
        'Com certeza, você deveria fazer isso',
        'Não faça isso.',
        'Está na hora certa.',
        'Estou indeciso.']
    

    def iniciar(self) -> None: # Método para iniciar.
        self.pergunta_usuario() # Método que pede pro usuário fazer uma pergunta.
        self.resposta_computador() # Método que a máquina responde o usuário.
    

    def pergunta_usuario(self) -> str: # Método que pede pro usuário fazer uma pergunta.
        self.__pergunta = str(input('Faça uma pergunta: ')) # Pedindo p usuário fazer uma pergunta.
        while self.__pergunta.isnumeric(): # Conferindo se a pergunta não é númerica.
            print('Faça uma pergunta com apenas letras.')
            self.__pergunta = str(input('Pergunte: '))
        
    
    def resposta_computador(self) -> str: # Método em que a máquina responde o usuário
        print(self.__pergunta) # Repetindo pergunta para ficar mais interativo.
        print('Pensando....')
        print(f'Minha resposta é: {random.choice(self.__respostas)}.') # Respondendo.


# Testando

# Criando objeto.
decida = DecidaPorMim()

# Chamando o método que inicia.
decida.iniciar()