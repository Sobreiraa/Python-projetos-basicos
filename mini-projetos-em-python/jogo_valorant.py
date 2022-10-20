# Jogo de aventura / Tema: Valorant
# Um jogo de decisões onde eu terei que criar vários finais diferentes baseados nas respostas que forem dadas.
# Desejo chegar a finais diferentes na minha história, de acordo com as respostas que eu passe para o programa.

class JogoValorant:

    def __init__(self) -> None:
        self.__jogo = '''Qual jogo deseja jogar? 
[0] - Valorant / [1] - Valorant  ''' # PERGUNTA SOBRE O JOGO.
        self.__classe = '''Qual classe de agentes deseja jogar?
[0] - Duelista
[1] - Sentinela
[2] - Iniciador
[3] - Controlador  ''' # PERGUNTA SOBRE A CLASSE DE AGENTES.
        self.__arma = '''Qual arma deseja comprar?
[0] - Vandal
[1] - Phantom
[2] - Spectre
[3] - Operator  ''' # PERGUNTA SOBRE A ARMA DO JOGO.
        self.__skin = '''Qual skin deseja?
[0] - Íon
[1] - Ancifogo
[2] - Sublime
[3] - Glitchpop  ''' # PERGUNTA SOBRE A SKIN DO JOGO.
        self.__mapa = '''Em qual mapa deseja jogar?
[0] - Split
[1] - Ascent
[2] - Haven
[3] - Fracture  ''' # PERGUNTA SOBRE O MAPA DO JOGO.
        self.__estrategia = '''Deseja atacar ou defender?
[0] - Defender
[1] - Atacar  ''' # PERGUNTA SOBRE A ESTRATEGIA DO JOGO.
        self.__historia_final = [] # HISTÓRIA FINAL DO JOGO.


    def iniciar(self) -> None: # Método que inicia toda a classe.
        self.pergunta1() # Método que chama uma pergunta.
        self.pergunta2() # Método que chama uma pergunta.
        self.pergunta3() # Método que chama uma pergunta.
        self.pergunta4() # Método que chama uma pergunta.
        self.pergunta5() # Método que chama uma pergunta.
        self.pergunta6() # Método que chama uma pergunta.
        self.imprime_historia_final() # Método que chama a história final.
    

    def pergunta1(self) -> str: # Método da pergunta 1.

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PERGUNTA 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
        try:
            resposta1 = int(input(self.__jogo)) # Perguntando ao usuário.

            if resposta1 == 0 or resposta1 == 1: # Validando resposta
                print('Ótima escolha')
                print('BRINCADEIRA.... Só temos o jogo VALORANT dísponivel.')
                self.__historia_final.append('O jogo escolhido foi Valorant') # Guardando a resposta na história final
            else: # Conferindo resposta.
                print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                exit() # Saindo após a inserção incorreta do dado.
        except (ValueError, TypeError): # Exceções para tipo de dado incorreto.
            print('Tivemos um problema com o tipo de dado inserido.')
            exit() # Saindo após a inserção incorreta do dado.
        except KeyboardInterrupt: # Erro caso o usuário não digite nada.
            print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
            exit() # Saindo após a inserção incorreta do dado.
    

    def pergunta2(self) -> str: # Método da pergunta 2.

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PERGUNTA 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ dueslita/sentinela/iniciador/controlador
        try:
            resposta2 = int(input(self.__classe)) # Perguntando ao usuário.

            if resposta2 == 0: # Conferindo resposta.
                print('Gosto muito desse classe de agentes.')
                self.__historia_final.append('Classe escolhida: Duelista') # Guardando a resposta na história final

                agente = int(input('''Qual agente deseja jogar?
                [0] - Raze
                [1] - Yoru  ''')) # Perguntando ao usuário.

                try:
                    if agente == 0: # Conferindo resposta.
                        print('O meu agente preferido.')
                        self.__historia_final.append('O agente escolhido foi a Raze') # Guardando a resposta na história final
                    elif agente == 1: # Conferindo resposta.
                        print('...')
                        self.__historia_final.append('O agente escolhida foi o Yoru') # Guardando a resposta na história final
                    else: # Conferindo resposta.
                        print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                        exit() # Saindo após a inserção incorreta do dado.

                except (ValueError, TypeError): # Erro caso o usuário não digite nada.
                    print('Tivemos um problema com o tipo de dado inserido.')
                    exit() # Saindo após a inserção incorreta do dado.
                except KeyboardInterrupt: # Erro caso o usuário não digite nada.
                    print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                    exit() # Saindo após a inserção incorreta do dado.

            elif resposta2 == 1: # Conferindo resposta.
                print('Não gosto dessa classe.')
                self.__historia_final.append('Classe escolhida: Sentinela') # Guardando a resposta na história final

                agente = int(input('''Qual agente deseja jogar?
                [0] - Killjoy
                [1] - Chamber  ''')) # Perguntando ao usuário.

                try:
                    if agente == 0: # Conferindo resposta.
                        print('Não conheço nenhuma main Killjoy boa.')
                        self.__historia_final.append('O agente escolhido foi a Killjoy') # Guardando a resposta na história final
                    elif agente == 1: # Conferindo resposta.
                        print('Ótima escolha')
                        self.__historia_final.append('O agente escolhida foi o Chamber') # Guardando a resposta na história final
                    else: # Conferindo resposta.
                        print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                        exit() # Saindo após a inserção incorreta do dado.

                except (ValueError, TypeError): # Exceções para tipo de dado incorreto.
                    print('Tivemos um problema com o tipo de dado inserido.')
                    exit() # Saindo após a inserção incorreta do dado.
                except KeyboardInterrupt: # Erro caso o usuário não digite nada.
                    print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                    exit() # Saindo após a inserção incorreta do dado.
            
            elif resposta2 == 2: # Conferindo resposta.
                print('Já joguei um pouco com essa classe.')
                self.__historia_final.append('Classe escolhida: Iniciador') # Guardando a resposta na história final

                agente = int(input('''Qual agente deseja jogar?
                [0] - Skye
                [1] - Fade  ''')) # Perguntando ao usuário.

                try:
                    if agente == 0: # Conferindo resposta.
                        print('Gosto da skye.')
                        self.__historia_final.append('O agente escolhido foi a Skye')
                    elif agente == 1: # Conferindo resposta.
                        print('Uma grande escolha.')
                        self.__historia_final.append('O agente escolhido foi a Fade')
                    else: # Conferindo resposta.
                        print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                        exit() # Saindo após a inserção incorreta do dado.

                except (ValueError, TypeError): # Exceções para tipo de dado incorreto.
                    print('Tivemos um problema com o tipo de dado inserido.')
                    exit() # Saindo após a inserção incorreta do dado.
                except KeyboardInterrupt: # Erro caso o usuário não digite nada.
                    print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                    exit() # Saindo após a inserção incorreta do dado.

            elif resposta2 == 3: # Conferindo resposta.
                print('Uma classe de agentes boa.')
                self.__historia_final.append('Classe escolhida: Controlador') # Guardando a resposta na história final

                agente = int(input('''Qual agente deseja jogar?
                [0] - Brimstone
                [1] - Harbor  ''')) # Perguntando ao usuário.

                try:
                    if agente == 0: # Conferindo resposta.
                        print('Tem uma boa ultimate.')
                        self.__historia_final.append('O agente escolhido foi o Brimstone') # Guardando a resposta na história final
                    elif agente == 1: # Conferindo resposta.
                        print('O grande novo agente.')
                        self.__historia_final.append('O agente escolhido foi o Harbor') # Guardando a resposta na história final
                    else: # Conferindo resposta.
                        print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                        exit() # Saindo após a inserção incorreta do dado.

                except (ValueError, TypeError): # Exceções para tipo de dado incorreto.
                    print('Tivemos um problema com o tipo de dado inserido.')
                    exit() # Saindo após a inserção incorreta do dado.
                except KeyboardInterrupt: # Erro caso o usuário não digite nada.
                    print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                    exit() # Saindo após a inserção incorreta do dado.

            else: # Conferindo resposta.
                print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                exit() # Saindo após a inserção incorreta do dado.

        except (ValueError, TypeError): # Exceções para tipo de dado incorreto.
            print('Tivemos um problema com o tipo de dado inserido.')
            exit() # Saindo após a inserção incorreta do dado.
        except KeyboardInterrupt: # Erro caso o usuário não digite nada.
            print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
            exit() # Saindo após a inserção incorreta do dado.

    
    def pergunta3(self) -> str:

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PERGUNTA 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Vandal/Phantom/Spectre/Operator
        try:
            resposta3 = int(input(self.__arma)) # Perguntando ao usuário.

            if resposta3 == 0: # Conferindo resposta.
                print('A melhor arma do jogo.')
                self.__historia_final.append('A arma para a partida é a Vandal') # Guardando a resposta na história final
            elif resposta3 == 1: # Conferindo resposta.
                print('A segunda melhor arma.')
                self.__historia_final.append('A arma para a partida é a Phantom') # Guardando a resposta na história final
            elif resposta3 == 2: # Conferindo resposta.
                print('Uma arma boa para patinetar.')
                self.__historia_final.append('A arma para a partida é a Spectre') # Guardando a resposta na história final
            elif resposta3 == 3: # Conferindo resposta.
                print('Não consigo jogar com essa arma.')
                self.__historia_final.append('A arma para a partida é a Operator') # Guardando a resposta na história final
            else: # Conferindo resposta.
                print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                exit() # Saindo após a inserção incorreta do dado.

        except (ValueError, TypeError): # Exceções para tipo de dado incorreto.
            print('Tivemos um problema com o tipo de dado inserido.')
            exit() # Saindo após a inserção incorreta do dado.
        except KeyboardInterrupt: # Erro caso o usuário não digite nada.
            print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
            exit() # Saindo após a inserção incorreta do dado.
    

    def pergunta4(self) -> str:

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PERGUNTA 4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Íon/Ancifogo/Sublime/Glitchpop
        try:
            resposta4 = int(input(self.__skin)) # Perguntando ao usuário.

            if resposta4 == 0: # Conferindo resposta.
                print('A melhor sking do jogo.')
                self.__historia_final.append('A skin escolhida foi Íon') # Guardando a resposta na história final
            elif resposta4 == 1: # Conferindo resposta.
                print('Pega muito.')
                self.__historia_final.append('A skin escolhida foi Ancifogo') # Guardando a resposta na história final
            elif resposta4 == 2: # Conferindo resposta.
                print('Essa é uma barbaridade.') 
                self.__historia_final.append('A skin escolhida foi Sublime') # Guardando a resposta na história final
            elif resposta4 == 3: # Conferindo resposta.
                print('A melhor bulldog é com essa skin.')
                self.__historia_final.append('A skin escolhida foi Glitchpop') # Guardando a resposta na história final
            else: # Conferindo resposta.
                print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                exit() # Saindo após a inserção incorreta do dado.

        except (ValueError, TypeError): # Exceções para tipo de dado incorreto.
            print('Tivemos um problema com o tipo de dado inserido.')
            exit() # Saindo após a inserção incorreta do dado.
        except KeyboardInterrupt: # Erro caso o usuário não digite nada.
            print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
            exit() # Saindo após a inserção incorreta do dado.

    
    def pergunta5(self) -> str:

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PERGUNTA 5 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Split/Ascent/Haven/Fracture
        try:
            resposta5 = int(input(self.__mapa)) # Perguntando ao usuário.

            if resposta5 == 0: # Conferindo resposta.
                print('Saudades desse mapa')
                self.__historia_final.append('O mapa escolhido foi Split') # Guardando a resposta na história final
            elif resposta5 == 1: # Conferindo resposta.
                print('Melhor mapa;')
                self.__historia_final.append('O mapa escolhido foi Ascent') # Guardando a resposta na história final
            elif resposta5 == 2: # Conferindo resposta.
                print('Esse mapa tem 3 bomb.')
                self.__historia_final.append('O mapa escolhido foi Haven') # Guardando a resposta na história final
            elif resposta5 == 3: # Conferindo resposta.
                print('Está um pouco melhor depois da atualização.')
                self.__historia_final.append('O mapa escolhido foi Fracture') # Guardando a resposta na história final
            else: # Conferindo resposta.
                print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                exit() # Saindo após a inserção incorreta do dado.

        except (ValueError, TypeError): # Exceções para tipo de dado incorreto.
            print('Tivemos um problema com o tipo de dado inserido.')
            exit() # Saindo após a inserção incorreta do dado.
        except KeyboardInterrupt: # Erro caso o usuário não digite nada.
            print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
            exit() # Saindo após a inserção incorreta do dado.


    def pergunta6(self) -> str:

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PERGUNTA 5 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Defender/Atacar
        try:
            resposta6 = int(input(self.__estrategia)) # Perguntando ao usuário.

            if resposta6 == 0: # Conferindo resposta.
                print('Começa Defendendo.')
                self.__historia_final.append('Você começa defendendo') # Guardando a resposta na história final
            elif resposta6 == 1: # Conferindo resposta.
                print('Melhor mapa;')
                self.__historia_final.append('Você começa atacando') # Guardando a resposta na história final
            else: # Conferindo resposta.
                print('Foi tentar ser esperto(a) ou digitou errado e saiu do jogo.')
                exit() # Saindo após a inserção incorreta do dado.
           
        except (ValueError, TypeError): # Exceções para tipo de dado incorreto.
            print('Tivemos um problema com o tipo de dado inserido.')
            exit() # Saindo após a inserção incorreta do dado.
        except KeyboardInterrupt: # Erro caso o usuário não digite nada.
            print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
            exit() # Saindo após a inserção incorreta do dado.
    

    def imprime_historia_final(self) -> str:

        for historia in self.__historia_final: # Laço para mostrar a lista da história completa em que o usuário escolheu,
            print(historia) # Imprimindo a história final.
            print() # Quebra de linha.
        
        print('Boa sorte.')

valorant = JogoValorant()
valorant.iniciar()