"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    rows = len(matrix[0])
    for i in range(rows):
        rowstr = ''
        for j in range(len(matrix)):
            rowstr += (str(matrix[j][i]) + ' ')
        print(rowstr)


#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    length = len(matrix)
    for i in range(length):
        for j in range(length):
            if (i == j):
                matrix[j][i] = 1
            else:
                matrix[j][i] = 0
    return matrix

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    m_result = m2
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            for k in range(len(m1)):
                m_result[i][j] = m1[k][j] * m2[i][k]
    for n in range(len(m2[0])):
        for p in range(len(m2)):
            m2[p][n] = m_result[p][n]
    return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
