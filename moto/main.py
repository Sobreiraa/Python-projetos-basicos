from moto import Moto

# TESTES:

moto1 = Moto('Suzuki', 'GSX', 'azul', 6)

moto1.set_modelo = 'titan'
moto1.set_marca = 'honda'
moto1.set_cor = 'vermelho'
moto1.set_maior_marcha = 8
moto1.ligar()
moto1.set_marcha = 8

moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()

moto1.marcha_acima()
moto1.marcha_acima()
moto1.marcha_acima()
moto1.marcha_acima()
moto1.marcha_acima()

moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()
moto1.marcha_abaixo()




print('-' * 85)


moto1.imprimir()