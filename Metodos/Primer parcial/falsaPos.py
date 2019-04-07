import numpy as np
from numpy import pi
import math

vv = input("Valor Verdadero: ")
def funcion(x):
    #definir aqui la funcion
    res = 0
    #print( "Valor en funcion " + str(float(x**2)))
    res = float((75*(math.e**(-1.5*x))+(20*(math.e**(-0.075*x)))-15))
    return res

def falsaPos():
    counter = 0
    vaa = 2
    va = 1
    
    ea = ((va-vaa)/float(va))*100
    n = input("Cifras (n): ")
    #es = (0.5 * (10**(2-n)))
    es = .5
    #Esto es para ES
    print("El es tolerancia porcentual es: " + str(es) + " %")

    xl = input("Low (xl): ")
    xu = input("Upper (xu): ")
    while abs(ea) > es:
        counter += 1
        print(" ")
        print( "Iteracion " + str(counter))              
        if xl == None and xu == None:
                xl = input("Low (xl): ")
                xu = input("Upper (xu): ")
        #Aqui se obtiene la propuesta de raiz para cada iteracion
        xr = xu - ((funcion(xu)*(xl-xu)/float((funcion(xl)-funcion(xu)))))
        print("Evaluar esto en la funcion (FALSA POS) XR: " + str(xr))
        tempva = va
        va = xr
        vaa = tempva
        print("Comparativo "+ str(funcion(xr)))
        if (funcion(xr)) < 0:
            xl = xr
            xu = xu
        elif (funcion(xr)) > 0:
            xu = xr
            xl = xl
        else:
            return
        print(xl)
        print(xu)
        ev = vv - va
        er = (ev/float(vv)) * 100
        #Esto es para ET
        print("El error verdadero es: " + str(er))
        ea = ((va-vaa)/float(va))*100
        print(va)
        print(vaa)
        print(ea)
        #Esto es para EA
        print("El error aproximado porcentual es: " + str(ea))
        print("El error aproximado porcentual es: " + str(ea)) 

    print(str(xr))
    print("El valor que haya en este nivel de error sera correcto hasta " + str(n) +" cifras")

falsaPos()
