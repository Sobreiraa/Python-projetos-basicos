from elevador import Elevador

# Testando

# Criando objeto
elevador1 = Elevador()

# Setters
elevador1.set_andar_atual = 15
elevador1.set_total_andares = 10
elevador1.set_pessoas_elevador = 13
elevador1.set_capacidade_pessoas = 15

# Método inicializa
elevador1.inicializa(5, 3)

# Método entra pessoa
elevador1.entra_pessoa()
elevador1.entra_pessoa()
elevador1.entra_pessoa()

# Método sai pessoa
elevador1.sai_pessoa()
elevador1.sai_pessoa()

# Método sobe andar
elevador1.sobe_andar()
elevador1.sobe_andar()
elevador1.sobe_andar()
elevador1.sobe_andar()
elevador1.sobe_andar()
elevador1.sobe_andar()

# Método desce andar
elevador1.desce_andar()
elevador1.desce_andar()
elevador1.desce_andar()
elevador1.desce_andar()
elevador1.desce_andar()
elevador1.desce_andar()


# Getters
print(elevador1.get_andar_atual)
print(elevador1.get_total_andares)
print(elevador1.get_pessoas_elevador)
print(elevador1.get_capacidade_pessoas)