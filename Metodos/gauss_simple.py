import numpy as np
from numpy import pi
import math

#mat = np.matrix([[3,-.1, -.2, 7.85],[.1,7,-.3, -19.3],[.3,-.2,16, 71.4]])
#El ultimo valor para cada renglon es el resultado de la ecuacion 
#mat = np.matrix([[2,1, -1, 1],[5,2,2, -4],[3,1,1, 5]])
mat = np.matrix([[1,7, -4,-51],[4,-4,9,62],[12,-1,3,8]])
def gauss():
    print(mat)
    mat1 = mat

    for i in range(3):
        mul = (mat[i,0]/mat[0,0])
        print(i)
        if i == 1 :
            for j in range(4):
                mat1[i,j] = mat[i,j] - ((mat[i-1,j]) * (mul))
        elif i == 2:
            for j in range(4):
                print("")
                #mat1[i][j] = mat1[i][j] - (mat1[i-2][j]) * ((mat1[2][0]/mat1[0][0]))
                mat1[i,j] = mat[i,j] - ((mat[i-2,j]) * (mul))
    print(mat1)
    return mat1

def gauss2(mat1):
    mat2 = mat1
    mul = (mat[2,1]/mat[1,1])
    for i in range(3):
        print(i)
        if i == 2 :
            for j in range(4):
                mat2[i,j] = mat1[i,j] - ((mat1[i-1,j]) * (mul))
    print(mat2)


gauss2(gauss())
#Para el determinante se hace positivo negativo positivo para 