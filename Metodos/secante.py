import numpy as np
import math
from numpy import pi, cos, sin
import math
import sys

vv = input("Valor Verdadero: ")

def funcion(x):
    #definir aqui la funcion
    res = 0
    #print( "Valor en funcion " + str(float(x**2)))
    res = float((3.5967*x)/(math.sqrt(((x**2)+0.81)**3))-1)
    return res


def secante():
    counter = 0
    vaa = 2
    va = 1
    
    ea = ((va-vaa)/float(va))*100
    n = input("Cifras (n): ")
    es = (0.5 * (10**(2-n)))
    #Esto es para ES
    print("El es tolerancia porcentual es: " + str(es) + " %")
    
    xi = input("Xi: ")
    xim = input("Xi - 1: ")
    while abs(ea) > es:
        counter += 1
        print(" ")
        print( "Iteracion " + str(counter))              
        if xi == None or xim == None:
                xi = input("Xi: ")
                xim = input("Xi - 1: ")
        #Aqui se obtiene la propuesta de raiz para cada iteracion
        tempxi = xi
        xi = xi - ((funcion(xi)*(xim-xi))/float((funcion(xim)-(funcion(xi)))))
        print("Evaluar esto en la funcion Xr: " + str(xi))
        xim = tempxi
        tempva = va
        va = xi
        vaa = tempva
       
        ev = vv - va
        er = (ev/float(vv)) * 100
        #Esto es para el ET 
        
        print("El error verdadero es: " + str(er))
        
        ea = ((va-vaa)/float(va))*100

        print(va)
        print(vaa)
        print(ea)
        #Esto es para el EA
        print("El error aproximado porcentual es: " + str(ea))
 
    print(str(xi))
    print("El valor que haya en este nivel de error sera correcto hasta " + str(n) +" cifras")
secante()