import numpy as np
from numpy import pi
import math

mat = np.matrix([[1.0,-1.0, 2.0],[-1.0,2.0,-1.0],[2.0,-1.0,5.0]])
x1 = np.matrix([[1.0,-1.0, 2.0],[2.0,2.0,-1.0],[5.0,-1.0,5.0]])
#Los valores de la columna 1 son los de resultados de la 
x2 = np.matrix([[1,1, 2],[-1,2,-1],[2,5,5]])
#Los valores de la columna 2 son los de resultados de la 
x3 = np.matrix([[1,-1, 1],[-1,2,2],[2,-1,5]])
#Los valores de la columna 3 son los de resultados de la 

mat_i = np.identity(3)

def determinante(mat):
    det = np.linalg.det(mat)
    print("DET ID:")
    print(np.linalg.det(x1))
    #print(det)
    return det

def soluciones():
    X1 = determinante(x1)/ determinante(mat)
    X2 = determinante(x2)/ determinante(mat)
    X3 = determinante(x3)/ determinante(mat)
    print("X1 : " + str(X1))
    print("X2 : " + str(X2))
    print("X3 : " + str(X3))

print("El determinante de la matriz es :" + str(determinante(mat)))
print("El determinante de x1 es :" + str(determinante(x1)))
print("El determinante de x2 es :" + str(determinante(x2)))
print("El determinante de x3 es :" + str(determinante(x3)))

soluciones()
#Para el determinante se hace positivo negativo positivo para 