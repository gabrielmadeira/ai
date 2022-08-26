from unittest import result
import numpy as np
def error(dataX,dataY,theta_0,theta_1):
    return(theta_0+theta_1*dataX)-dataY

def compute_mse(theta_0, theta_1, data):
    """
    Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    erroSum=0
    for i in range(len(data)):
        erroSum+=error(data[i][0],data[i][1],theta_0,theta_1)**2
    return erroSum/len(data)


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    Ftheta0=0
    Ftheta1=0
    for i in range(len(data)):
        Ftheta0+=error(data[i][0],data[i][1],theta_0,theta_1)
        Ftheta1+=error(data[i][0],data[i][1],theta_0,theta_1)*data[i,0]
    Ftheta0*=2/len(data)
    Ftheta1*=2/len(data)
    return[theta_0-(alpha*Ftheta0),theta_1-(alpha*Ftheta1)]


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    lTheta_0=theta_0
    lTheta_1=theta_1
    thetaList_0=[]
    thetaList_1=[]
    while(num_iterations):
        lTheta_0,lTheta_1=step_gradient(lTheta_0,lTheta_1,data,alpha)
        thetaList_0.append(lTheta_0)
        thetaList_1.append(lTheta_1)
        num_iterations-=1
    return thetaList_0,thetaList_1  
