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
    #res = float((75*(math.e**(-1.5*x))+(20*(math.e**(-0.075*x)))-15))
    res = float((1/(4*math.pi*8.85*10**-12)*(((2*10**-5)*(2*10**-5)*x)/(x**2+((0.9)**2))**(3/2))))	
    print(res)
    return res


def funcionDerivada(x):
    #definir aqui la funcion
    res = 0
    #print( "Valor en funcion " + str(float(x**2)))
    res = float(-112.5*(np.e**(-1.5*x))-(1.5*(np.e**(-0.075*x))))
    print(res)
    return res


def newR():
    counter = 0
    vaa = 2
    va = 1
    
    ea = ((va-vaa)/float(va))*100
    n = input("Cifras (n): ")
    es = (0.5 * (10**(2-n)))
    #Esto es para ES
    print("El es tolerancia porcentual es: " + str(es) + " %")
    
    xi = input("Xi: ")
    while abs(ea) > es:
        counter += 1
        print(" ")
        print( "Iteracion " + str(counter))              
        if xi == None:
                xi = input("Xi: ")
        #Aqui se obtiene la propuesta de raiz para cada iteracion
        xi = xi - ((funcion(xi))/float(funcionDerivada(xi)))
        print("Evaluar esto en la funcion Xr: " + str(xi))
        
        tempva = va
        va = xi
        vaa = tempva
       
        ev = vv - va
        er = (ev/float(vv)) * 100
        #Esto es para el ET 
        print("El error verdadero es: " + str(ev))
        print("El error relativo porcentual es: " + str(er))
        
        ea = ((va-vaa)/float(va))*100

        print(va)
        print(vaa)
        print(ea)
        #Esto es para el EA
        print("El error aproximado porcentual es: " + str(ea))
 
    print(str(xi))
    print("El valor que haya en este nivel de error sera correcto hasta " + str(n) +" cifras")

newR()
