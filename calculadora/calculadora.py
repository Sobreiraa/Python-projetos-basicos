class Calculadora:
    def __init__(self) -> None:
        self.__escolhe_operacao()

    
    def __escolhe_operacao(self) -> None:
        try: # Tente escolher a operação
            operacao = int(input('''Qual operação deseja realizar?

        [1] - Soma
        [2] - Subtração
        [3] - Múltiplicação
        [4] - Divisão 

        '''))
            while (operacao < 1) or (operacao > 4): # Enquanto a operação for diferente das opções
                print('Tente novamente...')
                operacao = int(input('''Qual operação deseja realizar?

        [1] - Soma
        [2] - Subtração
        [3] - Múltiplicação
        [4] - Divisão 

        '''))
        except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
        except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.

        #---------------------------------- Validando opções escolhidas ----------------------------------

        if operacao == 1:
            self.__somar() # Operação de soma
        elif operacao == 2:
            self.__subtrair() # Operação de subtração
        elif operacao == 3:
            self.__multiplicar() # Operação de multiplicação
        else:
            self.__dividir() # Operação de divisão
        
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    
    def __somar(self) -> None: # -------------------- MÉTODO PARA SOMAR ----------------------
        print()
        print('-' * 75)
        try:
            qtd_numeros_para_somar = int(input('Deseja somar quantos números? '))
        except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
        except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            
        #---------------------------------------- Soma ----------------------------------------

        print('-' * 75)
        print()

        lista_de_numeros_para_calc = []
        for numero in range(1, qtd_numeros_para_somar+1):
            try:
                numero = int(input(f'Digite o {numero}° número para a soma: '))
                lista_de_numeros_para_calc.append(numero)
                print()
            except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.
        
        #---------------------------------------- Resultado ----------------------------------------

        soma_dos_numeros = 0
        for numero in range(0, qtd_numeros_para_somar): 
            soma_dos_numeros += lista_de_numeros_para_calc[numero] 

        print('-' * 75)
        print(f'A soma dos números {lista_de_numeros_para_calc} é {soma_dos_numeros}.') # Resultado
        print('-' * 75)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __subtrair(self) -> None: # --------------------- MÉTODO PARA SUBTRAIR --------------------------
        print()
        print('-' * 75)
        try:
            qtd_numeros_para_subtrair = int(input('Deseja subtrair quantos números? '))
        except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
        except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            
        #------------------------------------------ SUBTRAI  --------------------------------------------

        print('-' * 75)
        print()

        lista_de_numeros_para_calc = []
        for numero in range(1, qtd_numeros_para_subtrair+1):
            try:
                numero = int(input(f'Digite o {numero}° número para a subtração: '))
                lista_de_numeros_para_calc.append(numero)
                print()
            except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.
        
        #---------------------------------------- Resultado ----------------------------------------

        subtracao_dos_numeros = lista_de_numeros_para_calc[0]
        for numero in lista_de_numeros_para_calc[1:]:
            subtracao_dos_numeros -= numero 

        print('-' * 75)
        print(f'A subtração dos números {lista_de_numeros_para_calc} é {subtracao_dos_numeros}.') # Resultado
        print('-' * 75)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __multiplicar(self) -> None: # --------------------- MÉTODO PARA MULTIPLICAR --------------------------
        print()
        print('-' * 75)
        try:
            qtd_numeros_para_multiplicar = int(input('Deseja multiplicar quantos números? '))
        except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
        except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            
        #------------------------------------------ MULTIPLICAR  ---------------------------------------------

        print('-' * 75)
        print()

        lista_de_numeros_para_calc = []
        for numero in range(1, qtd_numeros_para_multiplicar+1):
            try:
                numero = int(input(f'Digite o {numero}° número para a multiplicação: '))
                lista_de_numeros_para_calc.append(numero)
                print()
            except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.
        
        #---------------------------------------- Resultado ----------------------------------------

        multiplicacao_dos_numeros = 1
        for numero in range(0, qtd_numeros_para_multiplicar):
            multiplicacao_dos_numeros *= lista_de_numeros_para_calc[numero]

        print('-' * 75)
        print(f'A multiplicação dos números {lista_de_numeros_para_calc} é {multiplicacao_dos_numeros}.') # Resultado
        print('-' * 75)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    def __dividir(self) -> None: # --------------------- MÉTODO PARA DIVIDIR --------------------------
        print()
        print('-' * 75)
        try:
            qtd_numeros_para_dividir = int(input('Deseja dividir quantos números? '))
        except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
        except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            
        #------------------------------------------ MULTIPLICAR  ---------------------------------------------

        print('-' * 75)
        print()

        lista_de_numeros_para_calc = []
        for numero in range(1, qtd_numeros_para_dividir+1):
            try:
                numero = int(input(f'Digite o {numero}° número para a divisão: '))
                lista_de_numeros_para_calc.append(numero)
                print()
            except (ValueError, TypeError): # Erros do tipo de dado inserido.
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números. Programa encerrado.')
                exit() # Saindo do programa após o erro.
            except KeyboardInterrupt: # Erro pois não foi inserido nada quando solicitado.
                print('O usuário preferiu não informar nenhum dado. Programa encerrado.')
                exit() # Saindo do programa após o erro.
        
        #---------------------------------------- Resultado ----------------------------------------

        divisao_dos_numeros = lista_de_numeros_para_calc[0]
        for numero in lista_de_numeros_para_calc[1:]:
            divisao_dos_numeros /= numero

        print('-' * 75)
        print(f'A divisão dos números {lista_de_numeros_para_calc} é {divisao_dos_numeros}.') # Resultado
        print('-' * 75)



calc = Calculadora()