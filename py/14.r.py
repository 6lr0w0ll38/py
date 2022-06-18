import numpy as np

def bao_dong_bac_cau ( M ) :
    M = np . array (M , dtype = bool )
    A = L = M
    n = len( M )
    for p in range (2 , n +1) :
        L = M . dot ( L )
        A = A + L
    return np . array (A , dtype =int)

M = [[0 , 0 , 0 , 0 , 1] ,
     [0 , 1 , 0 , 0 , 0] ,
     [0 , 0 , 0 , 1 , 0] ,
     [1 , 0 , 1 , 0 , 0] ,
     [0 , 1 , 0 , 0 , 1]]
print (bao_dong_bac_cau(M))
