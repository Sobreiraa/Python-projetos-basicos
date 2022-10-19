''' Crie uma classe Agenda que possa armazenaar 10 pessoas e seja capaz de realizar as seguintes operções:
* Armazenar_pessoa (Nome, idade, altura);
* Remove_pessoa (nome);
* Busca_pessoa (nome) // informa em que posição da agenda está a pessoa;
* Imprime_agenda() // imprime os dados de todas as pessoas da agenda;
''' 

class Agenda:

    contatos = 0

    def __init__(self) -> None: # Método construtor.
        self.__agenda = [] # Agenda (LISTA).


    def armazena_pessoa(self) -> str: # Método para armazenar uma pessoa na agenda.
        if self.contatos <= 10: # Conferindo se tem espaço na agenda.

            nome = str(input('Nome: ')).title().strip() # Nome da pessoa.
            while not nome.isalpha(): # Validando se o usuário digitou apenas letras.
                print('Digite apenas letras.')
                nome = str(input('Nome: ')).title().strip()
            
            try: # Validação de dados.
                idade = int(input('Idade: ')) # Idade da pessoa.
                while idade <= 0: # Conferindo se a idade é um número negativo.
                    print('Precisamos de um valor positivo.') 
                    idade = int(input('Idade: '))
            except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.


            try: # Validação de dados.
                altura = float(input('Altura: ')) # Altura da pessoa.
                while altura <= 0: # Conferindo se a altura é um número negativo.
                    print('Precisamos de um valor positivo.')
                    altura = float(input('Altura: '))
            except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            except KeyboardInterrupt:
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.


            if nome in self.__agenda: # Conferindo se já tem essa pessoa na agenda.
                print('Essa pessoa já está na agenda.')
            else:
                self.__agenda.append(nome) # Adicionando o nome na agenda.
                self.__agenda.append(idade) # Adicionando a idade na agenda.
                self.__agenda.append(altura) # Adicionando a altura na agenda.
        else:
            print('Lista cheia.')
        
        print('-=' * 50)


    def remove_pessoa(self) -> str: # Método para remover alguma pessoa da agenda.
        pessoa_remover = str(input('Qual pessoa deseja remover? ')).title().strip() # Solicitando a pessoa para remoção.
        if pessoa_remover in self.__agenda: # Conferindo se a pessoa x está na agenda.
            numero_remover = self.__agenda.index(pessoa_remover) # Dando um número para remover a pessoa na posição correta.
            del self.__agenda[numero_remover] # Removendo nome.
            del self.__agenda[numero_remover] # Removendo idade.
            del self.__agenda[numero_remover] # Removendo altura.
            print(f'Removendo {pessoa_remover}.')
        else:
            print('Pessoa não encontrada.')


    def busca_pessoa(self) -> str: # Método para buscar pessoa.
        buscar_pessoa = str(input('Digite qual pessoa deseja buscar: ')).title().strip() # Buscando pessoa.
        if buscar_pessoa in self.__agenda: # Conferindo se a pessoa x está na agenda.
            numero_pessoa = self.__agenda.index(buscar_pessoa) # Pegando a pessoa na posição correta.
            print(f'Nome: {self.__agenda[numero_pessoa]}') # Imprimindo dados da pessoa.
            print(f'Idade: {self.__agenda[numero_pessoa + 1]}') # Imprimindo dados da pessoa.
            print(f'Altura: {self.__agenda[numero_pessoa + 2]}') # Imprimindo dados da pessoa.
        else:
            print('Busca não encontrada.')
    

    def imprime_agenda(self) -> str: # Método para imprimir a agenda.
        print(f'Assim ficou sua agenda de contatos: {self.__agenda}')