import random
import time
import math

class Node:

    def __init__(self, board, player, parent, child, roundsPlayed, roundsWon,move):
       self.board=board
       self.player=player
       self.parent=parent
       self.child=child
       self.roundsPlayed=roundsPlayed
       self.roundsWon=roundsWon
       self.move=move


def innerScorePreference(node,UCB):
    a=1
    eq=math.pow(node.move[0]-3.5,2)+(node.move[1]-math.pow(3.5,2))
    if eq<=0: return 0
    return UCB*a/(math.sqrt(eq))

def greedPenalty(node,color):
    b=4
    t = 1 if color=='B' else -1
    greed=(math.pow(-1,t)*(node.board.num_pieces('B')-node.board.num_pieces('W')))/math.pow((node.board.num_pieces('B')+node.board.num_pieces('W')),b)
    return greed

def badMovePenalty(node,UCB):
    c=0.5
    d=0.5
    e=-1.5
    coefficient=0
    badMoveListC=[(1,1),(1,6),(6,1),(6,6)]
    badMoveListD=[(0,1),(1,0),(6,0),(7,1),(7,6),(6,7),(0,6),(1,7)]
    goodMoveList=[(0,0),(0,7),(7,0),(7,7)]
    if node.move in badMoveListC:
        coefficient=c
    elif node.move in badMoveListD:
        coefficient=d
    elif node.move in goodMoveList:
        coefficient=e
    
    return UCB*coefficient
    
        

def UCB(node,totalPlays,parent):
    C=1
    if parent.player==node.player:
        UCB = (node.roundsWon/node.roundsPlayed) + C*math.sqrt(2*math.log(totalPlays)/node.roundsPlayed)
    else:
        UCB = ((node.roundsPlayed - node.roundsWon)/node.roundsPlayed) + C*math.sqrt(2*math.log(totalPlays)/node.roundsPlayed)
    innerScore = innerScorePreference(node,UCB)
    greed=greedPenalty(node,node.player)
    badMove=badMovePenalty(node,UCB)
    if((node.board.num_pieces('W')+node.board.num_pieces('B'))>50):
        return UCB
    else:
        if parent.player==node.player:
            return UCB + innerScore - greed - badMove
        else:
            return UCB - innerScore + greed + badMove
       

def bestSucessor(node,totalPlays):
    best=0
    
    for i in range(0,len(node.child)):
            if UCB(node.child[i],totalPlays,node)>UCB(node.child[best],totalPlays,node):
                best = i
    return node.child[best]

def createChild(node):
    #nem sempre vai ser o oponente que joga no proximo board 
    legal_moves=node.board.legal_moves(node.player)
    selectedMove=None
    if len(legal_moves)==0:
        selectedMove=(-1, -1)
    else:
        for i in range(0,len(legal_moves)):
            found=False
            for j in range(0,len(node.child)):
                if node.child[j].move == legal_moves[i]:
                    found=True
                    break
            if not found:
                selectedMove=legal_moves[i]
     
                break  
    newPlayer=None          
    nodeBoardCopy = node.board.copy()
    nodeBoardCopy.process_move(selectedMove, node.player)
    if nodeBoardCopy.legal_moves(nodeBoardCopy.opponent(node.player)):  
        newPlayer=nodeBoardCopy.opponent(node.player)
    else: 
        newPlayer=node.player
    return Node(nodeBoardCopy, newPlayer, node, [], 0, 0, selectedMove)

def selectAndExpand(root):
    totalPlays = root.roundsPlayed
    node = root
    while (len(node.child) == len(list(dict.fromkeys(node.board.legal_moves(node.player))))) and node.child:
        node = bestSucessor(node,totalPlays)

    # node <- o cara que a gente vai ter que pegar uma jogada dele para virar um nodo na árvore (FAZER FUNCAO)
    if node.board.is_terminal_state():
        return node

    leaf = createChild(node)
    node.child.append(leaf)
    
    return leaf

def backpropagation (node, resultado): #resultado: retorno da simulação
    while node.parent:
        node.roundsPlayed += 1
        node.roundsWon += resultado
        if node.parent.player != node.player:
            resultado= 1-resultado
        node = node.parent
    node.roundsPlayed += 1
    node.roundsWon += resultado

def simulate(the_board,colorNode):
    #contabilizar empates
    badMoveListC=[(1,1),(1,6),(6,1),(6,6)]
    badMoveListD=[(0,1),(1,0),(6,0),(7,1),(7,6),(6,7),(0,6),(1,7)]
    result =0
    boardCopy=the_board.copy()
    while not boardCopy.is_terminal_state():
        legal_moves = boardCopy.legal_moves(colorNode)
        move=random.choice(legal_moves) if len(legal_moves) > 0 else (-1, -1)
        tries=0
        while (move in badMoveListC or move in badMoveListD) and tries<2:
            move=random.choice(legal_moves)
            tries+=1
        boardCopy.process_move(move, colorNode)
        colorNode=the_board.opponent(colorNode);
    if(boardCopy.winner()==colorNode):
        result=1
    return (result)




def selectedMove(root):
    bestMove=0
    if root.player==root.child[0].player:
        for i in range(0,len(root.child)):
            winRation=root.child[i].roundsWon/root.child[i].roundsPlayed
            if  winRation > root.child[bestMove].roundsWon/root.child[bestMove].roundsPlayed:
                bestMove=i
    else:    
        for i in range(0,len(root.child)):
            loseRatio=root.child[i].roundsWon/root.child[i].roundsPlayed
        #we want to choose the worst adversary unles the next node is also the same player
            if  loseRatio < root.child[bestMove].roundsWon/root.child[bestMove].roundsPlayed:
                bestMove=i
    return root.child[bestMove].move

def make_move(the_board, color):
 
    root = Node(the_board, color, None, [], 0, 0, (0,0))
    legal_moves = root.board.legal_moves(root.player)
    if len(legal_moves) > 0:

        timeLimit = 4.9
        startTime = time.time()
        currentTime = startTime
        iterations=0
        while currentTime-startTime < timeLimit and iterations<100000:
            leaf = selectAndExpand(root)
            sims=0
            while sims !=1:
                result = simulate(leaf.board,leaf.player)
                backpropagation(leaf, result)
                sims+=1
            currentTime = time.time()
            iterations+=1

        return selectedMove(root) # melhor filho da raiz

    return (-1,-1)
    

