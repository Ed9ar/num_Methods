import numpy as np
from numpy import pi
import math

#meterlas pivoteadas
mat = np.matrix([[3,-.1, -.2, 7.85],[.1,7,-.3, -19.3],[.3,-.2,16, 71.4]])
#El ultimo valor para cada renglon es el resultado de la ecuacion 
def pivote(mat):
    if(mat[2,1] > mat[1,1]):
        temp = mat[2,0]
        mat[2,0] = mat[1,0]
        mat[1,0] = temp
        temp1 = mat[2,1]
        mat[2,1] = mat[1,1]
        mat[1,1] = temp1
        temp2 = mat[2,2]
        mat[2,2] = mat[1,2]
        mat[1,2] = temp2

    return mat

def gauss():
    print(mat)
    mat1 = mat
    
    for i in range(3):
        mul = (1/mat[0,0])
        print(i)
        if i == 0 :
            for j in range(4):
                mat1[i,j] = mat[i,j]  * (mul)
        else:
            temp = mat[i,0]
            for j in range(4):
                print("")
                mat1[i,j] = mat[i,j] - ((temp) * (mat[0,j]))
        
    print(mat1)
    print (" ")
    #mat1 = pivote(mat1)
    #print(mat1)
    return mat1

def gauss2(mat1):
    #Segunda Iteracion
    mat2 = mat1
    mul = (1/mat1[1,1])
    for i in range(3):
        print(i)
        if i == 1 :
            for j in range(4):
                mat2[i,j] = mat1[i,j]  * (mul)
            print("")

        elif i == 2:
            temp1 = mat1[i,1]
            temp2 = mat1[i-2,1] #Este el valor del renglon si es 1,1 es el 1 para cad i
            for j in range(4):
                mat2[i,j] = mat1[i,j] - ((temp1) * (mat1[1,j]))
                mat2[i-2,j] = mat1[i-2,j] - ((temp2) * (mat1[1,j]))
            print("")
   
    print(mat2)
    return mat2

def gauss3(mat2):
    #Tercera Iteracion
    mat3 = mat2
    mul = (1/mat2[2,2])
    i = 2
    while(i >= 0):
        print(i)
        if i == 2 :
            for j in range(4):
                mat3[i,j] = mat2[i,j]  * (mul)
            print("")

        else:
            temp = mat2[i,2]
            for j in range(4):
                mat3[i,j] = mat2[i,j] - ((temp) * (mat2[2,j]))    
            print("")
        i-=1
   
    print(mat2)
    return mat3


gauss3(gauss2(gauss()))
 