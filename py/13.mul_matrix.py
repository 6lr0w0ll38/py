from sympy import *

A = Matrix ([[2 , 0 , -1] ,
             [1 , 3 , -2]])

B = Matrix ([[ 0 , -1 , 1 , 0] ,
             [ 2 , 3 , -1 , 4] ,
             [ -3 , 0 , -2 , 1]])

print (A * B)

import numpy as np
A = np.array ([[2 , 0 , -1] ,
                 [1 , 3 , -2]])
B = [[ 0 , -1 , 1 , 0] ,
     [ 2 , 3 , -1 , 4] ,
     [ -3 , 0 , -2 , 1]]
print (list(A.dot(B)))
print (list(np.dot(A, B)))

def matrix_mul (A , B ) :
    m , n = len ( A ) , len( B )
    p = len( B [0])
    C = [[0 for j in range ( p ) ] for i in range ( m ) ]
    for i in range ( m ) :
        for j in range ( p ) :
            for k in range ( n ) :
                C [ i ][ j ] += A [ i ][ k ] * B [ k ][ j ]
    return C

A = [[ 2 , 0 , -1] ,
     [ 1 , 3 , -2]]
B = [[ 0 , -1 , 1 , 0] ,
     [ 2 , 3 , -1 , 4] ,
     [ -3 , 0 , -2 , 1]]

print (matrix_mul (A , B ))

matrix_mul = lambda A , B : [ [ sum( a * b for a , b in zip( row , col ) ) for col in zip (* B) ] for row in A ]
print (matrix_mul(A, B))
