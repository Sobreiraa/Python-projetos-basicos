from televisor import Televisor

televisao = Televisor(10, 15, 5, 6)

# Testes getters
print(televisao.get_numero_canais)
print(televisao.get_volume_maximo)
print(televisao.get_canal)
print(televisao.get_volume)

print('-' * 75)

# Teste de herança
televisao.ligar()

# Testes setters
televisao.set_numero_canais = -10
televisao.set_volume_maximo = -12
televisao.set_canal = -10
televisao.set_volume = -1

# Testes canal
televisao.canal_acima()
televisao.canal_acima()
televisao.canal_acima()
televisao.canal_acima()
televisao.canal_abaixo()
televisao.canal_abaixo()
televisao.canal_acima()

# Testes volume
televisao.volume_acima()
televisao.volume_acima()
televisao.volume_acima()
televisao.volume_acima()
televisao.volume_acima()
televisao.volume_acima()
televisao.volume_acima()
televisao.volume_acima()
televisao.volume_abaixo()
televisao.volume_abaixo()
televisao.volume_abaixo()
televisao.volume_abaixo()
televisao.volume_abaixo()
televisao.volume_abaixo()
televisao.volume_abaixo()
televisao.volume_abaixo()
televisao.volume_acima()
televisao.volume_acima()
televisao.volume_acima()


televisao.imprimir()