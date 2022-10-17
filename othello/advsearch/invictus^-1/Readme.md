# Trabalho 2 - MCTS em Othello

### Inteligencia Artificial 2022/1

### Instituto de Informática - Universidade Federal do Rio Grande do Sul

## Autores

- Gabriel Madeira (00322863) Turma B
- João Pedro Lopes Bazotti (00323915) Turma A
- Vitória Colonetti Benedet (00303081) Turma B

## Função de avaliação

Utilizamos como critério de seleção o UCB (Upper Coefficient Bound), com a constante C igual a um dividido pela raiz de 2 e as métricas InnerScore, GreedPenality e PositionPenalty.

## Estratégia de parada

Utilizamos a contagem do tempo em cada iteração do MCTS, caso o tempo desde o início da execução do algoritmo seja superior a 4.9 segundos, o algoritmo retorna a melhor jogada até então.

## Eventuais melhorias

Encontramos um artigo que possui algumas propostas de melhoria para o MCTS.
Na implementação original do UCB, o método majoritariamente favorece em direção aos nodos com maior vitórias. Entretanto, quando temos poucas simulações isso pode fazer com que o algoritmo falhe em selecionar bons movimentos. Por isso,ao invés de usar apenas o cálculo do UCB, é acrescentado a este as métricas InnerScore, GreedPenality e PositionPenalty. As duas primeiras derivam do princípio que no reversi não é uma boa ideia virar muitas peças no início do jogo, já que diminuem a mobilidade do jogador, dando ao oponente maior possibilidades de jogadas válidas. Além disso, as peças próximas ao centro do tabuleiro permitem maiores conexões. O InnerScore é um reforço positivo para manter os movimentos perto do centro do tabuleiro, tem um peso a. O GreedPenalty é uma penalidade em ser ambicioso, penalidade essa que diminui ao longo do jogo pela utilização de um coeficiente b. Por último, o PositionPenalty é uma penalidade em fazer algumas jogadas que são predeterminadas como jogadas ruins, c e d são parâmetros que determinam o peso da penalidade nas jogadas adjacentes aos cantos diagonais e adjacentes aos cantos das bordas respectivamente. Realizamos diversas jogadas a fim de determinar os melhores coeficientes a,b,c e d dentro do tempo disponível (cerca de 5 segundos).

Além disso, varremos o código procurando por possíveis trocas de estruturas de dados mais eficientes.

## Decisões de projeto

Devido ao interesse dos integrantes no algoritmo, escolhemos MCTS. Para ter uma vantagem sobre o algoritmo puro, procuramos por fontes onde foi encontrado algum tipo de otimização.

## Dificuldades encontradas

Tivemos dificuldade em testar o funcionamento do algoritmo. Dado que, em algumas situações, mesmo estando logicamente errada, nossa implementação conseguia ganhar do random. Quando jogávamos, tínhamos um controle melhor, porém o processo era demorado, devido ao tempo para pensar em jogadas. Inicialmente não implementamos a árvore e o backtracking corretamente para 2 jogadores. Isso fazia o algoritmo escolher a melhor jogada para o jogador adversário, levando o algoritmo à derrota.

## Bibliografia completa

- Slides do professor Anderson Rocha Tavares
- https://vgarciasc.github.io/mcts-viz/
- https://royhung.com/reversi
