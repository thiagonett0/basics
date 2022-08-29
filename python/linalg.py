"""
Descrição: código que possui as principais operações algébricas lineares.
"""


def floatSum(a, b):

    """
    Descrição: opera a soma entre dois números reais;

    Entrada(s):
            i) a (float): operando primário;
            ii) b (float): operando secundário;
    
    Saída(s):
            i) _ (float): soma.
    """

    return a+b


def floatProduct(a, b):

    """
    Descrição: opera o produto entre dois números reais;

    Entrada(s):
            i) a (float): operando primário;
            ii) b (float): operando secundário;
    
    Saída(s):
            i) _ (float): produto.
    """

    return a*b


def dotProduct(u, v):

    """
    Descrição: opera o produto ponto (produto interno, produto escalar) entre dois vetores reais;

    Entrada(s):
            i) u (float): operando primário;
            ii) v (float): operando secundário;
    
    Saída(s):
            i) _ (float): produto ponto.
    """

    return sum(list(map(floatProduct, u, v)))


def vectorSum(u, v):

    """
    Descrição: opera a soma entre dois vetores reais;

    Entrada(s):
            i) u (float): operando primário;
            ii) v (float): operando secundário;
    
    Saída(s):
            i) _ (float): soma vetorial.
    """

    return list(map(floatSum, u, v))


def vectorScalar(a, v):

    """
    Descrição: opera o produto escalar entre um escalar e vetor reais. Perceba que
            os iteráveis de v tornam-se as entradas x de lambda;

    Entrada(s):
            i) a (float): escalar real;
            ii) v (float): vetor real;
    
    Saída(s):
            i) _ (float): produto escalar.
    """

    return list(map(lambda x: a*x, v))


def vectorOnes(size):

    """
    Descrição: cria vetor de 1s de tamanho size;

    Entrada(s):
            i) size (list): escalar real;
    
    Saída(s):
            i) _ (float): vetor 1s.
    """

    return list([1 for i in range(size)])


def vectorZeroes(size):

    """
    Descrição: cria vetor de 0s de tamanho size;

    Entrada(s):
            i) size (list): escalar real;
    
    Saída(s):
            i) _ (float): vetor 0s.
    """

    return list([0 for i in range(size)])


def euclidianNorm(v):

    """
    Descrição: calcula a norma euclidiana para vetores reais;

    Entrada(s):
            i) v (float): vetor real;
    
    Saída(s):
            i) _ (float): norma euclidiana.
    """

    return dotProduct(v, v)**0.5


def absoluteinfiniteNorm(v):
    
    """
    Descrição: calcula a norma infinita do vetor com entradas absolutas;

    Entrada(s):
            i) v (float): vetor real;
    
    Saída(s):
            i) _ (float): norma infinita do vetor transformado.
    """

    return max(list(map(abs, v)))


def distance(u, v):
 
    """
    Descrição: calcula a distância entre vetores;

    Entrada(s):
            i) u (float): vetor real;
            ii) v (float): vetor real;
    
    Saída(s):
            i) _ (float): distância entre u e v.
    """

    return euclidianNorm(vectorSum(u, vectorScalar(-1, v)))



def matrixVector(A, v):

    """
    Descrição: transforma um vetor por meio de matriz. Opera-se por meio produtos escalares das colunas e soma vetorial;

    Entrada(s):
            i) A (list): matriz de transformação;
            ii) v (list): vetor;

    Saída(s):
            i) _ (list): vetor transformado.
    """

    return list(map(lambda x: dotProduct(x, v), A))


def matrixSum(A, B):

    """
    Descrição: opera a soma entre duas matrizes reais;

    Entrada(s):
            i) A (list): matriz real;
            ii) B (list): matriz real;
    
    Saída(s):
            i) _ (list): soma matricial.
    """ 

    return list(map(lambda u,v: vectorSum(u, v) , A, B))


def matrixProduct(A, B):

    """
    Descrição: opera o produto entre duas matrizes reais;

    Entrada(s):
            i) A (list): matriz real;
            ii) B (list): matriz real;
    
    Saída(s):
            i) _ (list): produto matricial.
    """ 
    
    return list(map(lambda u: list(map(lambda v: dotProduct(u, v), matrixTranspose(B))), A))


def matrixTranspose(A):

    """
    Descrição: calcula a matriz transposta;

    Entrada(s):
            i) A (list): matriz;

    Saída(s):
            i) At (list): matriz transposta.
    """

    At = list()
    for j in range(len(A[0])):
        Atrow = list()
        for i in range(len(A)):
            Atrow.append(A[i][j])
        At.append(Atrow)
    return At


def matrixInverse():
    return


def matrixScalar(a, A):

    """
    Descrição: opera o produto escalar entre um escalar e matriz reais. Perceba que
            os iteráveis de A tornam-se as entradas v de lambda;

    Entrada(s):
            i) a (float): escalar real;
            ii) A (list): matriz real;
    
    Saída(s):
            i) _ (list): produto escalar.
    """

    return list(map(lambda v: vectorScalar(a, v), A))


def identityMatrix(size):
    
    """
    
    """

    I = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        I[i][i] = 1
    return I