
Resolução de questões sobre algoritmos ambiciosos

**Número da Lista**: 1<br>
**Conteúdo da Disciplina**: Algoritimos Ambiciosos<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0103792 |  Júlia Farias Sousa|
| 18/0078640	 |  Yuri Alves Bacarias|


## Sobre 
Questões sobre Algorítimos Ambiciosos retiradas do Beecrowd e CodeForces .

## Screenshots das resoluções
<img width="934" alt="Captura de Tela 2023-05-30 às 10 06 41" src="https://github.com/projeto-de-algoritmos/Greed_Resolucoes/assets/60350851/c9c44a15-0798-45cc-9cf3-1cfe5e2b47a5">

![Screenshot from 2023-05-30 14-02-06](https://github.com/projeto-de-algoritmos/Greed_Resolucoes/assets/48924092/2d562802-7921-47f4-9868-9d72ea5cf9d7)

## Linguagens utilizadas
C++ e Python

## Questão 1 (Beecrowd)
Motoboy
Por Thobias, Fernando e Luiz, URI  Brazil

Timelimit: 1
José é um motoboy e trabalha fazendo entregas para uma pizzaria. Seu salário é baseado no número de pizzas entregues. Só que esta pizzaria está com muito movimento e ele pediu auxílio a seu amigo Roberto para que o ajudasse nas entregas. Como Roberto é camarada e está sem trabalho no momento, ele concordou em pegar aqueles pedidos cujas entregas serão mais demoradas.

Assim, sempre que chegam à pizzaria, antes de partirem para novas entregas José determina a quantidade de pizzas que Roberto deverá entregar e seleciona para ele os pedidos mais demorados. Por exemplo, se há 22 pizzas para serem entregues e José determinar que Roberto entregue no máximo 10 destas pizzas (pode ser menos), estas devem estar obrigatoriamente entre os pedidos que levarão mais tempo para serem entregues. Isso é ilustrado no primeiro caso de teste, onde Roberto deverá fazer a entrega do segundo, terceiro e sexto pedido, somando 8 pizzas e 62 minutos (23 + 21 + 18). Se Roberto fosse realmente entregar 10 pizzas, ele teria que atender o segundo, terceiro e quarto pedido e isto levaria 59 minutos (23 + 21 + 16), o que não é o objetivo de José, pois levaria menos tempo do que a primeira opção, ou seja, a relação pizzas/tempo não importa muito para José (isso pode ser observado no segundo caso de teste do exemplo abaixo).

Para poder fazer a divisão do trabalho, José pediu a um amigo acadêmico em Ciência da Computação que desenvolvesse um programa que determinasse quanto tempo seu amigo Roberto irá levar para entregar estes pedidos mais demorados.

### Entrada
A entrada contém vários casos de teste. Cada caso de teste contém na primeira linha um valor inteiro N (1 ≤ N ≤ 20) que indica o número de pedidos. A linha seguinte contém um valor inteiro P (1 ≤ P ≤ 30) indicando o número máximo de pizzas que podem ser entregues por Roberto. Cada uma das próximas N linhas contém um pedido com o tempo total para ser entregue e a quantidade de pizzas do pedido, respectivamente. A final da entrada é determinado por N = 0, e não deverá ser processado.

### Saída
Para cada caso de teste de entrada deve ser impresso um valor inteiro que determina o tempo que Roberto irá levar para entregar as suas pizzas seguido de um espaço em branco e do texto “min.” 

<img width="716" alt="Captura de Tela 2023-05-30 às 10 01 08" src="https://github.com/projeto-de-algoritmos/Greed_Resolucoes/assets/60350851/d7543754-642a-40c8-86db-ab1ea7bd6c8a">

#

## Questão 2 (Beecrowd)

Festival de Estátuas de Gelo
Por Wanderley Guimarães, USP  Brasil

Timelimit: 3
Todos os anos, artistas de todo o mundo se reúnem na cidade, onde fazem esculturas de gelo gigantescas. A cidade vira uma galeria de arte ao céu aberto, uma vez que as esculturas ficam expostas na rua por semanas, sem derreter. Afinal, a temperatura média no inverno de Harbin (época em que ocorrerá a final mundial do ICPC) é de -20 graus.

O primeiro passo para fazer a escultura é montar um grande bloco de gelo da dimensão pedida pelo artista. Os blocos são recortados das geleiras de Harbin em blocos de altura e profundidade padrão e vários comprimentos diferentes. O artista pode determinar qual o comprimento que ele deseja que tenha o seu bloco de gelo para que a escultura possa começar a ser esculpida.

Os comprimentos disponíveis dos blocos são {a1; a2; ...;  aN} e o comprimento que o artista deseja é M. O bloco de comprimento 1 é muito usado, por este motivo ele sempre aparece na lista de blocos disponíveis. Sua tarefa é determinar o número mínimo de blocos tal que a soma de seus comprimentos seja M.

### Entrada
A entrada é composta por diversas instâncias. A primeira linha da entrada contém um inteiro T indicando o número de instâncias. A primeira linha de cada instância contém dois inteiros N (1 ≤ N ≤ 25) e M (1 ≤ M ≤ 1000000) representando o número de tipos de blocos e o comprimento desejado pelo artista, respectivamente. A próxima linha contém os inteiros a1; a2; ...; aN , onde (1 ≤ ai ≤ 100) para todo i (1,2,...N) separados por espaço.

### Saída
Para cada instância, imprima o número mínimo de blocos necessários para obter um bloco de comprimento M.
<img width="725" alt="Captura de Tela 2023-05-30 às 10 03 47" src="https://github.com/projeto-de-algoritmos/Greed_Resolucoes/assets/60350851/f7febcc2-a4fc-4ee4-8dcf-5e12d151b328">

#


## Questão 3 (Beecrowd)

O jogo canhão de destruição é um jogo muito simples de ser entendido. Você recebeu como missão destruir um determinado castelo, sendo que o mesmo possui como característica um número inteiro R que é a sua resistência. Para tentar completar sua missão, você recebeu um canhão que é carregado com projéteis de chumbo, sendo que este canhão pode ser carregado com quantos projéteis forem possíveis desde que a soma do peso deles em quilos não exceda a capacidade de carga do canhão. Podem existir projéteis com pesos iguais e poder de destruição diferentes devido ao seu formato, embora isso não seja tão importante. Ao atingir o castelo, um projétil faz com que o seu valor de destruição seja diminuído da resistência do castelo.

Levando em consideração que o canhão pode ser carregado uma única vez, respeitando o seu limite de quilos, a sua tarefa é carregar o canhão com projéteis que não ultrapassem o seu limite de carga mas que façam o maior estrago possível, para saber se a missão foi completada ou não.

### Entrada

A primeira linha de entrada contém o número de casos de teste. Cada caso de teste inicia com uma linha contendo um número inteiro N (1 ≤ N ≤ 50), que representa o número de projéteis de chumbo disponíveis. Seguem N linhas contendo dois inteiros X e Y, representando respectivamente o poder de destruição do projétil e o peso do projétil. A próxima linha contém um inteiro K (1 ≤ K ≤ 100) que representa a capacidade de carga do canhão e a última linha do caso de teste contém um inteiro R que indica a resistência total do castelo.  


### Saída
Se o dano total das cargas carregadas for maior ou igual à resistência do castelo então deverá ser impressa a mensagem “Missao completada com sucesso”, caso contrário, deverá ser impressa a mensagem “Falha na missao”.

![Screenshot from 2023-05-30 13-57-51](https://github.com/projeto-de-algoritmos/Greed_Resolucoes/assets/48924092/41ec03db-af01-422a-aef7-6d695345a81a)

#

## Questão 4 (codeforces)

![Screenshot from 2023-05-30 13-56-32](https://github.com/projeto-de-algoritmos/Greed_Resolucoes/assets/48924092/43afbc6f-dea3-402a-a5c0-00eb62b160fa)
![Screenshot from 2023-05-30 13-57-01](https://github.com/projeto-de-algoritmos/Greed_Resolucoes/assets/48924092/ca4b0b74-d71f-4d21-9207-ada9774a6f3d)
