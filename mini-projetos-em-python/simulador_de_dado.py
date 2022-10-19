# Simulador de dados
# Simula o uso de um dado, retornando um valor entre 1 e 6.

from random import randint
import PySimpleGUI as sg

class SimuladorDeDado:

    def __init__(self) -> None:
        self.__dado = 0 # Dado.
        self.__valor_minimo = 1 # Valor mínimo para o dado.
        self.__valor_maximo = 6 # Valor máximo para o dado.
        self.__mensagem = 'Você gostaria de gerar um novo valor para o dado? [S/N] ' # Mensagem.

        
    def iniciar(self) -> str or int: # Método para iniciar.

        while True: # Enquanto o usuário quiser jogar.
            resposta = str(input(self.__mensagem)).upper().strip() # Resposta do usuário.
            while not resposta.isalpha(): # Validando resposta.
                print('Digite apenas [S/N]') 
                resposta = str(input(self.__mensagem)).upper().strip() # Pedindo outra resposta depois da invalidação.
    
            if resposta == 'S' or resposta == 'SIM': # Conferindo resposta.
                self.joga_dado() # Chamando método que joga o dado.
            elif resposta == 'NÃO' or resposta == 'NAO' or resposta == 'N':
                print('Agradecemos sua participação.')
                exit()
            else: 
                print('Resposta inválida.')
                print('Saindo...')
                exit() # Saindo pois o usuário não quer jogar ou por não receber uma resposta correta.
            
            continuar = str(input('Quer continuar? ')).upper().strip() # Resposta para continar a jogar o dado.

            if continuar == 'S' or continuar == 'SIM': # Validando resposta para continuar.
                self.joga_dado() # Jogando dado outra vez.
            elif continuar == 'NÃO' or continuar == 'NAO' or continuar == 'N':
                print('Agradecemos sua participação.')
                break
            else:
                print('Resposta inválida. Saindo...') 
                break # Parando.


    def joga_dado(self) -> int: # Método que joga o dado.
        self.__dado = randint(self.__valor_minimo, self.__valor_maximo) # Usando o randint para sortear os dados.
        print('Jogando dado...', self.__dado) # Mostrando o valor do dado.


# Testes

# Criando o dado.
dado = SimuladorDeDado()

# Chamando o método iniciar.
dado.iniciar()