import numpy as np
def Warshall ( W ) :
    W = np . array (W , dtype = bool )
    n = len( W )
    for k in range ( n ) :
        for i in range ( n ) :
            for j in range ( n ) :
                W [ i ][ j ] = W [ i ][ j ] + W [i ][ k ] * W [ k ][ j ]
        print (f'W{k +1}\n', np . array (W , dtype =int) )
    return np . array (W , dtype =int)

M = [[1 , 0 , 0 , 0 , 1] ,
     [0 , 1 , 0 , 0 , 0] ,
     [0 , 0 , 0 , 1 , 0] ,
     [1 , 0 , 1 , 0 , 0] ,
     [0 , 1 , 0 , 0 , 1]]

Warshall (W = M)
