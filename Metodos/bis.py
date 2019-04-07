import numpy as np
import math
from numpy import pi

vv = input("Valor Verdadero: ")
def funcion(x):
    #definir aqui la funcion
    res = 0
    #print( "Valor en funcion " + str(float(x**2)))
    #res = float((75*(math.e**(-1.5*x))+(20*(math.e**(-0.075*x)))-15))
    #res = float((1/(4*math.pi*(8.85*(10**-12))))*((2*(10**-5)*(2*(10**-5))*x)/(((x**2)+(0.9**2))**(3/2.0))))
    res = float((3.5967*x)/(math.sqrt(((x**2)+0.81)**3))-1)
    return res

def bis():
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
        xr = (xl+xu)/2.0
        #Esto es para la propuesta de raiz de cada iteracion
        print("Evaluar esto en la funcion (BISECCION) XR: " + str(xr))
        tempva = va
        va = xr
        vaa = tempva
        print("Comparativo "+ str(funcion(xl)* funcion(xr)))
        if (funcion(xl)* funcion(xr)) < 0:
            xu = xr
            xl = xl
        elif (funcion(xl)* funcion(xr)) > 0:
            xl = xr
            xu = xu
        print(xl)
        print(xu)
        ev = vv - va
        er = (ev/float(vv)) * 100
        #Esto es para el ET 
        print("El error verdadero es: " + str(er))
        ea = ((va-vaa)/float(va))*100
        #Esto es para el EA
        print("El error aproximado porcentual es: " + str(ea))
 
    print(str(xr))
    print("El valor que haya en este nivel de error sera correcto hasta " + str(n) +" cifras")

bis()
