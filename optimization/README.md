Integrantes do grupo

- João Pedro Lopes Bazotti - 00323915 - Turma A
- Gabriel Madeira - 00322863 - Turma B
- Vitoria Colonetti Benedet - 00303081 - Turma B

## Valores dos parâmetros do algoritmo genético (g, n, k, m, e) que resultem na execução que encontra uma configuração o menor número de ataques que foi possível obter

- (80, 400, 3, 0.7, 30)

## Resultados Alegrete

- De acordo com nossos testes a melhor regressão linear acontenceu com theta_0 e theta_1 como 0, alpha valendo 0.001 e com num_iterations valendo 30000, obtendo um erro quadrático médio quadrático de 8.527708192028557, números maiores de iterações melhoram esse valor porém o aumento com 100000 iterações é de menos de 0.000000001.

- Com features normalizadas o erro quadrático fica 0.014884927677517031.

## Instruções de como executar o algoritmo genético e obter o gráfico

- Abrir o notebook eight_queens.ipynb, ou, para verificar os extras, eight_queens_extra.ipynb, e rodar as células. É possível, adicionalmente, alterar a variável "runs" de acordo com a quantidade de execuções que desejar, no final, exibe a média dos conflitos resultantes das execuções. Além disso, também é possível alterar os parâmetros (g, n, k, m, e).
- Nós criamos uma variante da função "run_ga", chamada "run_ga_with_metrics" para retornar, alem do melhor individo resultante da execução, as métricas daquela execução, que é usada para a geração do gráfico.

## Documentação dos extras implementados

- Cross over: Crossover de 3 pontos -> Recebe dois indivíduos e uma lista ordenada de pontos de cruzamentos (indices) a partir do qual os genes serão trocados.
  Retorna os dois indivíduos com o material genético trocado. A ordem dos dois indivíduos retornados não é importante.

- Mutação: Mutação flip -> Recebe um indivíduo e a probabilidade de mutação (m). Caso random() < m, inverte o conteúdo do indivíduo usando a função reverse(). Exemplo: [3,2,7,5,2,4,1,1] -> [1,1,4,2,5,7,2,3]

- Normalização de features: No notebook alegrete as features são normalizadas entre 0 e 1 na segunda celula.
