# Python-projetos-basicos
 Projetos básicos que criei para testar meus conhecimentos em **Programação Orientada a Objetos**.

### 1. Eletrodoméstico/Televisor. 

Utilizando Herança.

Escreva um código que apresente a classe Televisor, com atributos ligado, canal e volume. Adicione um método imprimir que deve mostrar na tela os valores de todos os atributos. O atributo ligado será boleano e deverá indicar o estado atual do televisor, se ligado ou desligado. O atributo canal deverá indicar o canal atual em que o televisor está sintonizado. O atributo volume deverá indicar o volume atual do televisor. Crie ou herde os métodos ligar e desligar do eletrodoméstico. Crie os atributos numero_canais e volume_maximo, onde numeros_canais indica o número máximo de canais que o televisor pode sintonizar e o volume_maximo indica qual o maior nível de volume possível. O método imprimir deve ser modificado de forma a mostrar na tela os valores de todos os atributos. Faça também os métodos canal_acima e o canal_abaixo, sendo que o método canal_acima deve sintonizar sempre o próximo canal em relação ao canal atual, onde ao chegar ao maior canal possível deverá voltar ao canal 1. O método canal_abaixo deve sintonizar sempre o canal anterior em relação ao canal atual, onde chegar ao canal 1 deverá voltar ao maior canal possível, simulando desta forma o funcionamento de um televisor. E por último adicione os métodos volume_acima e volume_abaixo, sendo que o método volume_acima deve modificar o volume para o próximo nível de volume possível, onde ao chegar ao volume_maximo não poderá possibilitar que o volume seja alterado. O método volume_abaixo deve modificar o volume para o nível imediatamente inferior de volume em relação ao volume atual, não podendo ser menor do que 0, simulando desta forma o funcionamento de um televisor.
***

### 2. Moto

Escreva um código que apresente a classe Moto, com atributos marca, modelo, cor e marcha. Crie também um método imprimir, que deve mostrar na tela os valores de todos os atributos. O atributo marcha indica em que marcha a moto se encontra no momento, sendo representado de forma inteira. Onde: 0 - neutro, 1 - primeira, 2 - segunda, etc.
Adicione os métodos marcha_acima e marcha_abaixo, que deverão efetuar a troca de marchas, onde o método marcha_acima sobe uma marcha e o método marcha_abaixo deverá realizar o oposto.
Crie os atributos maior_marcha, onde o atributo maior_marcha indica qual será a maior marcha possível para a moto. Desta forma os métodos marcha_acima e marcha_abaixo devem ser reescritos de forma a não permitirem a troca de marchas para valores abaixo do esperado. O método imprimir deve ser modificado de forma a mostrar na tela os valores de todos os atributos.
Construa os métodos ligar e desligar que deverão mudar o conteúdo do atributo ligada conforme o caso.
***
