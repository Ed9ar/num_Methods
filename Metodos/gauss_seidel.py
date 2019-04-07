import numpy as np
from numpy import pi
import math

vv = input("Valor Verdadero: ")

mat = np.matrix([[3,-.1, -.2, 7.85],[.1,7,-.3, -19.3],[.3,-.2,10, 71.4]])
#El ultimo valor para cada renglon es el resultado de la ecuacion 


def gaussSeidel():
    counter = 0
    vaa1 = 2
    va1 = 1

    vaa2 = 2
    va2 = 1
    
    vaa3 = 2
    va3 = 1

    
    ea1 = ((va1-vaa1)/float(va1))*100
    ea2 = ((va2-vaa2)/float(va2))*100
    ea3 = ((va3-vaa3)/float(va3))*100

    x1 = input("Ingresa x1: ")  
    x2 = 0 
    x3 = 0
    #n = input("Cifras (n): ")
    #es = (0.5 * (10**(2-n)))
    es = 5
    #Esto es para ES
    print("El es tolerancia porcentual es: " + str(es) + " %")

    while abs(ea1) > es or abs(ea2) > es or abs(ea3) > es:
        counter += 1
        print(" ")
        print( "Iteracion " + str(counter))              
        
        x1 = (mat[0,3] - mat[0,1] * x2 - mat[0,2] *x3)/ mat[0,0]
        x2 = (mat[1,3] - mat[1,0] * x1 - mat[1,2] *x3)/ mat[1,1]
        x3 = (mat[2,3] - mat[2,0] * x1 - mat[2,1] *x2)/ mat[2,2]

        print(mat[2,3])
        print(mat[2,0])
       
        print(mat[2,1])
        print(mat[2,2])


        print( "X1 : " + str(x1))
        print( "X2 : " + str(x2))
        print( "X3 : " + str(x3))

        tempva1 = va1
        va1 = x1
        vaa1 = tempva1

        tempva2 = va2
        va2 = x2
        vaa2 = tempva2

        tempva3 = va3
        va3 = x3
        vaa3 = tempva3


        #Esto es para ET
        ea1 = ((va1-vaa1)/float(va1))*100
        ea2 = ((va2-vaa2)/float(va2))*100
        ea3 = ((va3-vaa3)/float(va3))*100


        #Esto es para EA
        print("El error aproximado porcentual ea1 es: " + str(ea1))
        print("El error aproximado porcentual ea2 es: " + str(ea2))
        print("El error aproximado porcentual ea3 es: " + str(ea3))



def gaussSeidelRelajado():
    counter = 0
    vaa1 = 2
    va1 = 1

    vaa2 = 2
    va2 = 1
    
    vaa3 = 2
    va3 = 1

    
    ea1 = ((va1-vaa1)/float(va1))*100
    ea2 = ((va2-vaa2)/float(va2))*100
    ea3 = ((va3-vaa3)/float(va3))*100

    cosarelax = input("Ingresa la cosa relax: ")
    x1 = input("Ingresa x1: ")  
    x2 = 0 
    x3 = 0
    #n = input("Cifras (n): ")
    #es = (0.5 * (10**(2-n)))
    es = 5
    #Esto es para ES
    print("El es tolerancia porcentual es: " + str(es) + " %")

    while abs(ea1) > es or abs(ea2) > es or abs(ea3) > es:
        counter += 1
        print(" ")
        print( "Iteracion " + str(counter))              
        
        x1 = (mat[0,3] - mat[0,1] * x2 - mat[0,2] *x3)/ mat[0,0]
        
        x2 = (mat[1,3] - mat[1,0] * x1 - mat[1,2] *x3)/ mat[1,1]
        x3 = (mat[2,3] - mat[2,0] * x1 - mat[2,1] *x2)/ mat[2,2]

        print(mat[2,3])
        print(mat[2,0])
       
        print(mat[2,1])
        print(mat[2,2])


        print( "X1 : " + str(x1))
        print( "X2 : " + str(x2))
        print( "X3 : " + str(x3))

        tempva1 = va1
        va1 = x1
        vaa1 = tempva1

        tempva2 = va2
        va2 = x2
        vaa2 = tempva2

        tempva3 = va3
        va3 = x3
        vaa3 = tempva3

        x1 = cosarelax * x1 + (1-cosarelax)*(vaa1)
        x2 = cosarelax * x2 + (1-cosarelax)*(vaa2)
        x3 = cosarelax * x3 + (1-cosarelax)*(vaa3)

        #Esto es para ET
        ea1 = ((va1-vaa1)/float(va1))*100
        ea2 = ((va2-vaa2)/float(va2))*100
        ea3 = ((va3-vaa3)/float(va3))*100


        #Esto es para EA
        print("El error aproximado porcentual ea1 es: " + str(ea1))
        print("El error aproximado porcentual ea2 es: " + str(ea2))
        print("El error aproximado porcentual ea3 es: " + str(ea3))




gaussSeidel()


gaussSeidelRelajado()