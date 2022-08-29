"""
Descrição: código que possui as principais operações de cálculo.
"""


import sys
sys.path.append( 'path' )


def mean(v):

    """
    Descrição: calcula a média de um vetor;

    Entrada(s):
            i) v (list): vetor;
    
    Saída(s):
            i) _ (float): média de v.
    """

    return sum(v)/len(v)



def std(v, mu):

    """
    Descrição: calcula o desvio padrão de um vetor;

    Entrada(s):
            i) v (list): vetor;
    
    Saída(s):
            i) _ (float): desvio padrão de v.
    """

    return (sum(list(map(lambda i: (i-mu)**2, v)))/len(v))**0.5