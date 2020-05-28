# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 19:38:47 2017

@author: Arnulfo
"""

def trans(matriz):
    '''
    Encuentra la transpuesta de un matriz
    assumiendo hileras de la misma longitud
    '''
    hileras = len (matriz)
    columnas = len(matriz[0])
    t = [[0 for x in range(hileras)] for y in range(columnas)] 
    
    for i in range(hileras):
        for j in range(columnas):
            t[j][i] = matriz[i][j]
    return t

aux =[[0,0,0,0],[1,1,1,1]]
uno = trans(aux)
print(aux)

import numpy as np
from itertools import zip_longest

dos = np.transpose(aux)
tres = [list(i) for i in zip(*aux)]
cuatro = [[fila[i] for fila in aux ] for i in range(len(aux[0]))]
cinco = [list(f) for f in zip_longest(*aux, fillvalue = 0)]
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)