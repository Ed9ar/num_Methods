import numpy as np
from numpy import pi
import math

#mat = np.matrix([[1,1/2.0,1/3.0 ],[1, 2/3.0,2/4.0],[1,3/4.0,3/5.0]])
mat_i = np.identity(3)
sol = np.matrix([[1,0, 0],[0,1,0],[0,0,1]])

mat = np.matrix([[1,7, -4],[4,-4,9],[12,-1,3]])
mat_inv = np.linalg.inv(mat)

print(mat)

print("MATRIZ INVERSA")
print(mat_inv)


#El ultimo valor para cada renglon es el resultado de la ecuacion 

def gauss():
    #print(mat)
    mat1 = mat
    mat_i[1,0] = float(mat[1,0]/mat[0,0])
    mat_i[2,0] = float(mat[2,0]/mat[0,0])
    for i in range(3):
        mul = (mat[i,0]/mat[0,0])
        #print(i)
        if i == 1 :
            for j in range(3):
                mat1[i,j] = mat[i,j] - ((mat[i-1,j]) * (mul))
        elif i == 2:
            mat_i[i,1] = float(mat[i,1]/mat[1,1])
            for j in range(3):
                print("")
                #mat1[i][j] = mat1[i][j] - (mat1[i-2][j]) * ((mat1[2][0]/mat1[0][0]))
                mat1[i,j] = mat[i,j] - ((mat[i-2,j]) * (mul))

    #print(mat1)
    print("LOW")
    print(mat_i)
    return mat1

def gauss2(mat1):
    mat2 = mat1
    mul = (mat[2,1]/mat[1,1])
    for i in range(3):
        #print(i)
        if i == 2 :
            for j in range(3):
                mat2[i,j] = mat1[i,j] - ((mat1[i-1,j]) * (mul))
    print("UP")
    print(mat2)
    return mat2

def solux(mat_i, sol, mat2):
    #(1,0,0)
    d1 = sol[0,0]
    for i in range(3):
        if i == 1:
            d2 = sol[0,1] - (mat_i[1,0] * d1)
        elif i == 2:
            print(mat_i[2,0] * d1)
            print(mat_i[2,1] * d2)
            d3 = sol[0,2] - (mat_i[2,0] * d1 - mat_i[2,1] * d2)
    
    print("")
    print("Solucion d1, d2, d3 (1,0,0)")
    sold = np.matrix([d1,d2,d3])
    print(sold)

    x3 = (sold[0,2]/mat2[2,2])
    i = 2
    while i >= 0:
        if i == 1:
            x2 = (sold[0,i]-(x3*mat2[1,2]))/(mat2[1,1])
        elif i == 0:
            x1 = (sold[0,i]-((mat2[0,1]*x2)+(mat2[0,2])))/(mat2[0,0])
        i-=1
    print("")
    print("Columna inversa 1")
    solx1 = np.matrix([x1,x2,x3])
    ia0 = x1
    ia1 = x2
    ia2 = x3
    print(solx1)

    #repetir proceso pero con (0,1,0)
    d1 = 0
    d2 = sol[1,1]
    d3 = sol[1,2] - (mat_i[2,0] * d1 - mat_i[2,1] * d2)
    
    print("")
    print("Solucion d1, d2, d3 (0,1,0)")
    sold = np.matrix([d1,d2,d3])
    print(sold)

    x3 = (sold[0,2]/mat2[2,2])
    i = 2
    while i >= 0:
        if i == 1:
            x2 = (sold[0,i]-(x3*mat2[1,2]))/(mat2[1,1])
        elif i == 0:
            x1 = (sold[0,i]-((mat2[0,1]*x2)+(mat2[0,2])))/(mat2[0,0])
        i-=1
    print("")
    print("Columna inversa 2")
    solx2 = np.matrix([x1,x2,x3])
    ib0 = x1
    ib1 = x2
    ib2 = x3
    print(solx2)

    #Asignar valores para d en el paso (0,0,1) los dos primeros son 0 y el ultimo es 1
    d1 = 0
    d2 = 0
    d3 = 1

    print("")
    print("Solucion d1, d2, d3 (0,0,1)")
    sold = np.matrix([d1,d2,d3])
    print(sold)

    x3 = (sold[0,2]/mat2[2,2])
    i = 2
    while i >= 0:
        if i == 1:
            x2 = (sold[0,i]-(x3*mat2[1,2]))/(mat2[1,1])
        elif i == 0:
            x1 = (sold[0,i]-((mat2[0,1]*x2)+(mat2[0,2])))/(mat2[0,0])
        i-=1
    print("")
    print("Columna inversa 3")
    solx3 = np.matrix([x1,x2,x3])
    ic0 = x1
    ic1 = x2
    ic2 = x3
    print(solx3)
    '''inversa = np.matrix([ia0,ia1,ia2],[ib0,ia1,ia2],[ic0,ic1,ic2])
    print("Inversa")
    print(inversa)'''
    return 
    
solux(mat_i, sol, gauss2(gauss()))
#Para el determinante se hace positivo negativo positivo para 