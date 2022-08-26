import random

def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 9.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    attacks = 0
    for i in range(0, len(individual)):
        for j in range(i+1, len(individual)):
            if ((individual[i] == individual[j]) or 
                (individual[i]+abs(j-i) == individual[j]) or 
                (individual[i]-abs(j-i) == individual[j])):
                attacks += 1
    return attacks        
    # raise NotImplementedError  # substituir pelo seu codigo


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    melhor = participants[0]

    for i in range (0, len(participants)):
        if evaluate(participants[i]) < evaluate(melhor): ##se o atual tem menor conflitos - atualiza o melhor
            melhor = participants[i]
    
    return melhor
    #raise NotImplementedError  # substituir pelo seu codigo

def elitism(pop,e):
    """
    Recebe uma lista com vários indivíduos e retorna os e melhores deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list,list melhores e individuos da lista recebida
    """
    pop.sort(key=lambda x: evaluate(x))
    pop = pop[0:e]
    
    return pop

def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    
    o1 = parent1[0:index] + parent2[index:8]
    o2 = parent2[0:index] + parent1[index:8]

    children = [o1,o2] 

    return children

    #raise NotImplementedError  # substituir pelo seu codigo


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    
    rand = random.uniform(0, 1)
    if rand < m:
        pos = random.randint(0,7)
        num = random.randint(1,8)
        individual[pos] = num
    return individual
    # raise NotImplementedError  # substituir pelo seu codigo


def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    pop = list()
    for i in range(0,n):
        ind = list()
        for j in range(0,8):
            rand = random.randint(1,8)
            ind.append(rand )
        pop.append(ind)

    for gen in range(0, g):
        newPop = elitism(pop, e)
        
        while(len(newPop) < n):
            participants = list()
            for j in range(0, k):
                participants.append(pop[random.randint(0,n-1)])
            
            p1 = tournament(participants)
            participants = list()
            for j in range(0, k):
                participants.append(pop[random.randint(0,n-1)])
            p2 = tournament(participants)
            
            index = random.randint(1,6)

            cv = crossover(p1,p2,index)
            o1 = cv[0]
            o2 = cv[1]
            o1 = mutate(o1,m)
            o2 = mutate(o2,m)
            newPop.append(o1)
            newPop.append(o2)
        pop = newPop
    return tournament(pop)

        
    
    #raise NotImplementedError  # substituir pelo seu codigo
