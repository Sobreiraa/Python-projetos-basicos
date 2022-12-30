from passlib.hash import pbkdf2_sha256

class Cadastro:
    def __init__(self) -> None:
        self.__usuarios_bd = []
        self.__mensagem_boas_vindas()
        self.__escolher_opcao()


    def __mensagem_boas_vindas(self) -> None:
        print()
        print('-' * 50)
        print('~~~~~~~~~~~~~~~~~~~~~Bem vindo~~~~~~~~~~~~~~~~~~~~')
        print('-' * 50)
        print()


    def __escolher_opcao(self) -> None:
        try:
            opcao = int(input('''Qual opção deseja? 
[1] - Entrar no sistema
[2] - Cadastrar usuário
[3] - Mudar senha
[4] - Sair do sistema 
 '''))

            while (opcao < 1) or (opcao > 4):
                print('Opção inválida. Tente novamente...')
                opcao = int(input('''Qual opção deseja? 
[1] - Entrar no sistema
[2] - Cadastrar usuário
[3] - Mudar senha
[4] - Sair do sistema 
 '''))

        except (ValueError, TypeError):
            print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números inteiro. Programa encerrado.')
            exit()
        except KeyboardInterrupt:
            print('Não foi informado nenhum valor. Programa encerrado.')
            exit()

        if opcao == 1:
            print()
            self.__entrar_no_sistema()
        elif opcao == 2:
            print()
            self.__cadastrar_usuario()
        elif opcao == 3:
            print()
            self.__mudar_senha()
        else:
            print()
            print('Saindo do sistema.')
            exit()
    
    
    def __entrar_no_sistema(self) -> None:
        if len(self.__usuarios_bd) == 0:
            print('Nenhum usuário cadastrado. Cadastre para poder entrar no sistema.')
            print()
            self.__cadastrar_usuario()
        else:
            print()
            print('-' * 50)
            print('Bem vindo ao nosso sistema VIP.')
            print('Digite as informações do usuário para fazer login.')
            print('-' * 50)
            print()

            login = str(input('Digite seu e-mail ou nickname para login: '))
            

            if login in self.__usuarios_bd:
                if '@' in login: # ENTRANDO COM EMAIL
                    usuario_numero = self.__usuarios_bd.index(login)
                    print('-' * 50)
                    print()
                    print('E-mail encontrado. Buscando informações...')
                    print(f'Bem vindo {self.__usuarios_bd[usuario_numero - 2]} {self.__usuarios_bd[usuario_numero - 1]}.')
                    print()
                    print('Precisamos da sua senha para confirmar que é você.')
                    print()
                    print('-' * 50)

                    senha_login = input('Senha para login: ')
                    if pbkdf2_sha256.verify(senha_login, self.__usuarios_bd[usuario_numero + 2]):
                        print('-' * 50)
                        print('Acesso permitido. Obrigado pela preferência.')
                        print('Voltando ao sistema...')
                        print('-' * 50)
                        print()
                        self.__escolher_opcao()
                    else:
                        print('-' * 50)
                        print()
                        print('Senha incorreta.')
                        print('Saindo do sistema...')
                        print('-' * 50)
                        exit()

                else:
                    usuario_numero = self.__usuarios_bd.index(login)
                    if login == self.__usuarios_bd[usuario_numero]:
                        print('-' * 50)
                        print()
                        print('Usuário encontrado pelo Nickname. Buscando informações...')
                        print(f'Bem vindo {self.__usuarios_bd[usuario_numero - 3]} {self.__usuarios_bd[usuario_numero - 2]}.')
                        print()
                        print('Agora precisaremos da sua senha para confirmar que é você.')
                        print()
                        print('-' * 50)

                        senha_login = input('Senha para login: ')
                        if pbkdf2_sha256.verify(senha_login, self.__usuarios_bd[usuario_numero + 1]):
                            print('-' * 50)
                            print('Acesso permitido. Obrigado pela preferência.')
                            print('Voltando ao sistema...')
                            print('-' * 50)
                            print()
                            self.__escolher_opcao()
                        else:
                            print('-' * 50)
                            print()
                            print('Senha incorreta.')
                            print('Saindo do sistema...')
                            print('-' * 50)
                            exit()
            else:
                print()
                print('Usuário não encontrado.')
                print('Voltando ao sistema...')
                print()
                self.__escolher_opcao()


    def __cadastrar_usuario(self) -> None:
        print('-' * 50)
        print('Cadastro de usuários...')
        print('Vou precisar de algumas informações para cadastro.')
        print('-' * 50)
        print()

        # VALIDAÇÃO DO NOME
        nome = str(input('Nome: ')).title().strip()
        while not nome.isalpha():
            print('Digite apenas letras.')
            nome = str(input('Nome: ')).title().strip()

        # VALIDAÇÃO DO SOBRENOME
        sobrenome = str(input('Sobrenome: ')).title().strip()
        while not sobrenome.isalpha():
            print('Digite apenas letras.')
            sobrenome = str(input('Sobrenome: ')).title().strip()

        # VALIDAÇÃO DO EMAIL
        email = str(input('E-mail: ')).strip().lower()
        while (not '@' in email) or (not 'gmail.com' in email) or (len(email) <= 10):
            print('ERROR... E-mail inválido. Tente novamente.')
            email = str(input('E-mail: ')).strip().lower()

        # VALIDAÇÃO DO NICKNAME
        nickname = str(input('Nickname: ')).lower().strip()
        while True:
            if (len(nickname) <= 4) or (len(nickname) >= 25) or ('@' in nickname):
                print('O nickname deve ter no mínimo 5 e no máximo 24 letras.')
                nickname = str(input('Nickname: ')).lower().strip()
            else:
                break
            
        # VALIDAÇÃO DA SENHA
        senha = input('Senha: ')
        while True:
            if (len(senha) <= 4) or (len(senha) >= 31):
                print('A senha deve ter no mínimo 5 e no máximo 30 caracteres e também não deve ter o caractere @.')
                senha = input('Senha: ')
            else:
                break

        hash = pbkdf2_sha256.hash(senha)

        # VALIDAÇÕES PARA CRIAR USUÁRIO

        if (nickname in self.__usuarios_bd) or (email in self.__usuarios_bd):
            print()
            print('Usuário já cadastrado.')
            print('Voltando ao sistema...')
            print()
        else:
            self.__usuarios_bd.append(nome)
            self.__usuarios_bd.append(sobrenome)
            self.__usuarios_bd.append(email)
            self.__usuarios_bd.append(nickname)
            self.__usuarios_bd.append(hash)
            
            print('Usuário cadastrado.')
            print('Voltando ao inicio do sistema...')
            print()

        self.__escolher_opcao()

    
    def __mudar_senha(self) -> None:
        if len(self.__usuarios_bd) == 0:
            print('Nenhum usuário cadastrado.')
            print()
            self.__escolher_opcao()
        else:
            print('-' * 50)
            try:
                opc = int(input('''Esqueceu sua senha ou deseja trocar de senha? 
[1] - Esqueci senha
[2] - Desejo mudar minha senha 
 '''))

                while (opc < 1) or (opc > 2):
                    opc = int(input('''Esqueceu sua senha ou deseja trocar de senha? 
[1] - Esqueci senha
[2] - Desejo mudar minha senha 
 '''))
            except (ValueError, TypeError):
                print('Tivemos um problema com o tipo de dado inserido, na próxima vez digite apenas números inteiro. Programa encerrado.')
                exit()
            except KeyboardInterrupt:
                print('Não foi informado nenhum valor. Programa encerrado.')
                exit()
            
            if opc == 1:
                print()
                print('Precisamos de algumas informações.')

                email = str(input('Digite seu e-mail: '))

                if email in self.__usuarios_bd:
                    usuario_numero = self.__usuarios_bd.index(email)
                    nickname = str(input('Digite seu nickname: '))
                    if nickname == self.__usuarios_bd[usuario_numero + 1]:
                        senha = input('Digite sua nova senha: ')
                        while True:
                            if (len(senha) <= 4) or (len(senha) >= 31):
                                print('A senha deve ter no mínimo 5 e no máximo 30 caracteres e também não deve ter o caractere @.')
                                senha = input('Nova senha: ')
                                print('Senha salva.')
                                print()
                            else:
                                break
                                

                        hash = pbkdf2_sha256.hash(senha)

                        self.__usuarios_bd[usuario_numero + 2] = hash
                    else:
                        print('Usuário não encontrado. Voltando ao sistema...')
                else:
                    print('Usuário não encontrado.')
            else:
                login = str(input('Digite seu e-mail ou nickname para login: '))
                if login in self.__usuarios_bd:
                    if '@' in login: # ENTRANDO COM EMAIL
                        usuario_numero = self.__usuarios_bd.index(login)
                        print('-' * 50)
                        print('Precisamos da sua senha para confirmar que é você.')

                        senha_login = input('Senha para login: ')
                        if pbkdf2_sha256.verify(senha_login, self.__usuarios_bd[usuario_numero + 2]):
                            nova_senha = input('Digite sua nova senha: ')
                            while True:
                                if (len(nova_senha) <= 4) or (len(nova_senha) >= 31):
                                    print('A senha deve ter no mínimo 5 e no máximo 30 caracteres e também não deve ter o caractere @.')
                                    nova_senha = input('Nova senha: ')
                                    print('Senha salva.')
                                    print()
                                else:
                                    break

                            hash = pbkdf2_sha256.hash(nova_senha)
                            self.__usuarios_bd[usuario_numero + 2] = hash
                        else:
                                print('-' * 50)
                                print()
                                print('Senha incorreta.')
                                print('Saindo do sistema...')
                                print('-' * 50)
                                exit()
                    else:
                        usuario_numero = self.__usuarios_bd.index(login)
                        if login == self.__usuarios_bd[usuario_numero]:
                            print('-' * 50)
                            print('Agora precisaremos da sua senha para confirmar que é você.')

                            senha_login = input('Senha para login: ')
                            if pbkdf2_sha256.verify(senha_login, self.__usuarios_bd[usuario_numero + 1]):
                                nova_senha = input('Digite sua nova senha: ')
                                while True:
                                    if (len(nova_senha) <= 4) or (len(nova_senha) >= 31):
                                        print('A senha deve ter no mínimo 5 e no máximo 30 caracteres e também não deve ter o caractere @.')
                                        nova_senha = input('Nova senha: ')
                                        print('Senha salva.')
                                        print()
                                    else:
                                        break

                                hash = pbkdf2_sha256.hash(nova_senha)
                                self.__usuarios_bd[usuario_numero + 1] = hash
                            else:
                                print('-' * 50)
                                print()
                                print('Senha incorreta.')
                                print('Saindo do sistema...')
                                print('-' * 50)
                                exit()
                else:
                    print('Usuário não encontrado. Voltando ao sistema...')

            print()
            self.__escolher_opcao()


cadastro = Cadastro()