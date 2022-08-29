"""
Descrição: código que possui as principais operações de cálculo.
"""


import sys
sys.path.append( '/Users/Tarso/Desktop/Projeto GitHub/NumMath/Basics/python' )

import linalg as la


def gradient(scalarf, dimDomain, point, h):

    """
    Descrição: calcula o gradiente de qualquer função escalar f diferenciável em point. Para tal, itera-se sobre
                as coordenadas para efetuar a diferenciação por meio de diferenças finitas (central de ordem 4).
                A variável infinitesimal é uma lista alocando o incremento h apenas na variável de diferenciação.
                Ao final de cada diferenciação, adiciona-se ao vetor gradiente. Por fim, obtém-se o resultado.

    Entrada(s):
                i) f (list): função escalar;
                ii) dimDomain (int): domínio da função escalar f;
                iii) point (tuple): ponto a avaliar o gradiente da função escalar f;
                iv) h (float): passo de discretização do processo;

    Saída(s):
                i) grad (list): gradiente da função f avaliado em point.
    """

    grad = list()
    for i in range(dimDomain):
        infinitesimal = [0]*(i) + [h] + [0]*(dimDomain-1-i)
        # g.append((f(somaVetorial(point, escalar(1, infinitesimal))) - f(somaVetorial(point, escalar(-1, infinitesimal))))/(2*h)) central ordem 2
        grad.append((scalarf(la.vectorSum(point, la.vectorScalar(-2, infinitesimal))) - 8*scalarf(la.vectorSum(point, la.vectorScalar(-1, infinitesimal))) + 8*scalarf(la.vectorSum(point, la.vectorScalar(1, infinitesimal))) - scalarf(la.vectorSum(point, la.vectorScalar(2, infinitesimal))))/(12*h))
    return grad


def jacobian(vectorF, dimDomain, dimRange, point, h):

    """
    Descrição: calcula o jacobiano de qualquer função vetorial F diferenciável em point. Para tal, itera-se
                sobre as funções escalares de F. Para cada uma, calcula-se o gradiente por meio da função gradient
                acima. Ao final de cada iteração, adiciona-se o gradiente ao jacobiano.

    Entrada(s):
                i) vectorF (list): função vetorial F;
                ii) dimDomain (int): domínio da função vetorial F;
                iii) dimRange (int): codomínio da função vetorial F;
                iv) point (tuple): ponto a avaliar o gradiente da função vetorial F;
                v) h (float): passo de discretização do processo;

    Saída(s):
                i) jac (list): jacobiano da função vetorial F avaliada em point.
    """

    jac = list()
    for i in range(dimRange):
        f = vectorF[i]
        jac.append(gradient(f, dimDomain, point, h))
    return jac