# Chute o número
# Criar um algoritmo que gera um valor aleatório e peça um número ao usuário até que ele acerte esse valor aleatório.

from random import randint

class ChuteNumero:

    def __init__(self) -> None:
        self.__numero_aleatorio = 0 # Atributo que será o valor aleatório.
        self.__valor_minimo = 1 # Atributo para o valor mínimo.
        self.__valor_maximo = 100 # Atributo para o valor máximo.
    

    def iniciar(self) -> None: # Método para iniciar o programa.
        self.gera_numero_aleatorio() # Chamando método que gera o número aleatório.
        self.chute_usuario() # Chamando o método que pede o chute do usuário.
    

    def gera_numero_aleatorio(self) -> None: # Método para gerar o número aleatório.
        self.__numero_aleatorio = randint(self.__valor_minimo, self.__valor_maximo) # Usando a biblioteca random para gerar o número aleatório
    

    def chute_usuario(self) -> str: # Método que pede e valida o chute do usuário.
        try: 
            while True: # Enquanto não acertar o chute.
                chute = int(input('Chute um número: ')) # Pedindo o chute.

                if chute == self.__numero_aleatorio: # Se o chute estiver correto.
                    print('Parabéns, você acertou.')
                    break # Termine o programa.

                elif chute < self.__numero_aleatorio: # Se o chute for menor.
                    print('Continue tentando...')
                    print('DICA: Chute um número maior!') # DICA.
                    
                else: # Se o chute for maior;
                    print('Continue tentando.')
                    print('DICA: Chute um número menor!') # DICA

        except (ValueError, TypeError): # Exceção do tipo de dado inserido pelo usuário.
            print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
            exit() # Saindo do programa após o erro.

        except KeyboardInterrupt: # Exceção de quando não insere nenhum valor.
            print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
            exit() # Saindo do programa após o erro.
        
        except: # Outras exceções.
            print('Tivemos algum problema ao chutar o número.')


# Testes

# Criando o objeto.
numero = ChuteNumero()

# Chamando o método para iniciar o programa.
numero.iniciar()