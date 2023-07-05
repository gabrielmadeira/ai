import queue
import time

solution="12345678_"
backtrackDic={
"acima":"abaixo","abaixo":"acima","esquerda":"direita","direita":"esquerda",None:None
}
class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado, pai, acao, custo):

       self.estado=estado;
       self.pai=pai;
       self.acao=acao;
       self.custo=custo;
    def __lt__(self, other):
        return 0< 1

def sucessor(estado):
    succs=[]
    emptyPos=0
    for i in range (len(estado)):
        if estado[i]=="_":
            emptyPos=i
    
    if emptyPos >2:
        estadoList=list(estado)
        temp=estado[emptyPos-3]
        estadoList[emptyPos-3]='_'
        estadoList[emptyPos]=temp
        succs.append(("acima","".join(estadoList)))
    if emptyPos < 6:
        estadoList=list(estado)
        temp=estadoList[emptyPos+3]
        estadoList[emptyPos+3]='_'
        estadoList[emptyPos]=temp
        succs.append(("abaixo","".join(estadoList)))
    if emptyPos !=0 and emptyPos !=3 and emptyPos !=6:
        estadoList=list(estado)
        temp=estadoList[emptyPos-1]
        estadoList[emptyPos-1]='_'
        estadoList[emptyPos]=temp
        succs.append(("esquerda","".join(estadoList)))
    if emptyPos !=2 and emptyPos !=5 and emptyPos !=8:
        estadoList=list(estado)
        temp=estadoList[emptyPos+1]
        estadoList[emptyPos+1]='_'
        estadoList[emptyPos]=temp
        succs.append(("direita","".join(estadoList)))
    return succs

def expande(nodo):
    nodeList=[];
    succs=sucessor(nodo.estado)
    for succ in succs:
        nodeList.append(Nodo(succ[1],nodo,succ[0],nodo.custo+1))
    return nodeList

def bfs(estado):
    if inversions(estado)%2==1:
        return None
    start = time.time()
    X=dict();
    F=queue.Queue()
    F.put(Nodo(estado,None,None,0))
    while not F.empty():
        end = time.time()
        if end-start>59:
            return None
        V=F.get()
        if V.estado == solution:
           end = time.time()
           print(end-start)
           print(len(X))
           print(V.custo)
           return print_path(V)
        if V.estado not in X:
            X[V.estado]=True
        nodeList=expande(V)
        for node in nodeList:
            if backtrackDic[V.acao] != node.acao and node.estado not in X:
                F.put(node)
    return None
    
def inversions(str):
    inversionCount = 0
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if str[i] != "_" and str[j] != "_" and str[i] > str[j]:
                inversionCount += 1
    return inversionCount    


def dfs(estado):
    if inversions(estado)%2==1:
        return None
    start = time.time()
    X=dict();
    F=queue.LifoQueue()
    F.put(Nodo(estado,None,None,0))
    while not F.empty():
        end = time.time()
        if end-start>59:
            return None
        V=F.get()
        if V.estado == solution:
           end = time.time()
           print(end-start) 
           print(len(X))
           print(V.custo)
           return print_path(V)
        if V.estado not in X:
            X[V.estado]=True
        nodeList=expande(V)
        for node in nodeList:
            if backtrackDic[V.acao] != node.acao and node.estado not in X:
                F.put(node)
    return None

def h_hamming(estado):

    diff = 0
    for x in range (len(solution)):
        if solution[x] !='_':
            if solution[x] != estado[x]:
                diff += 1
    return diff

def astar_hamming(estado):
    if inversions(estado)%2==1:
        return None
    start = time.time()
    X=dict();
    F=queue.PriorityQueue()
    F.put((h_hamming(estado),Nodo(estado,None,None,0)))
    while not F.empty():
        end = time.time()
        if end-start>59:
            return None
        Tupla=F.get()
        V=Tupla[1]
        if V.estado == solution:
           end = time.time()
           print(end-start)
           print(len(X))
           print(V.custo)
           return print_path(V)
        if not V in X:
            X[V] = True
        nodeList=expande(V)
        for node in nodeList:
            if backtrackDic[V.acao] != node.acao:
                F.put((node.custo + h_hamming(node.estado), node))
    return None
    
def h_manhattan(estado):
    mat_sol = [[0,1,2,1,2,3,2,3,4],[1,0,1,2,1,2,3,2,3],[2,1,0,3,2,1,4,3,2],[1,2,3,0,1,2,1,2,3],[2,1,2,1,0,1,2,1,2],[3,2,1,2,1,0,3,2,1],[2,3,4,1,2,3,0,1,2],[3,2,3,2,1,2,1,0,1]]
    sum_dist = 0
    for x in range(len(estado)):
        if estado[x] == '1':
            sum_dist += mat_sol[0][x]
        if estado[x] == '2':
            sum_dist += mat_sol[1][x]
        if estado[x] == '3':
            sum_dist += mat_sol[2][x]
        if estado[x] == '4':
            sum_dist += mat_sol[3][x]
        if estado[x] == '5':
            sum_dist += mat_sol[4][x]
        if estado[x] == '6':
            sum_dist += mat_sol[5][x]
        if estado[x] == '7':
            sum_dist += mat_sol[6][x]
        if estado[x] == '8':
            sum_dist += mat_sol[7][x]
    return sum_dist 

    
def print_path(estado_final):   
    curr = estado_final
    path = [curr.acao]
    while curr.pai:
        if curr.pai.acao is not None:
            path.append(curr.pai.acao)
        curr = curr.pai
    path.reverse()
    return path

def astar_manhattan(estado):
    if inversions(estado)%2==1:
        return None
    start = time.time()
    X=dict();
    F=queue.PriorityQueue()
    F.put((h_manhattan(estado),Nodo(estado,None,None,0)))
    while not F.empty():
        end = time.time()
        if end-start>59:
            return None
        Tupla=F.get()
        V=Tupla[1]
        if V.estado == solution:
           end = time.time()
           print(end-start)
           print(len(X))
           print(V.custo)
           return print_path(V)
        if not V in X:
            X[V] = True
        nodeList=expande(V)
        for node in nodeList:
            if backtrackDic[V.acao] != node.acao:
                F.put((node.custo + h_manhattan(node.estado), node))
    return None

def main():
    str="2_3541687"
    print(bfs(str))
    print(dfs(str))
    print(astar_hamming(str))
    print(astar_manhattan(str))

if __name__ == '__main__':
    main()