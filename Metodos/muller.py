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
    #res = float((1/(4*math.pi*8.85*10**-12)*(((2*10**-5)*(2*10**-5)*x)/(x**2+((0.9)**2))**(3/2))))			
    res = float((75*(math.e**(-1.5*x))+(20*(math.e**(-0.075*x)))-15))
    return res

def calcX3(x2,c,b,a):
    x3 = 0
    if((b + math.sqrt((b**2)-4*a*c)) > (b - math.sqrt((b**2)-4*a*c))):
        x3 = x2 + ((-2*c)/(b + math.sqrt((b**2)-4*a*c)))
    else:
        x3 = x3 = x2 + ((-2*c)/(b - math.sqrt((b**2)-4*a*c)))
    return x3

def muller():
    counter = 0
    vaa = 2
    va = 1
    
    ea = ((va-vaa)/float(va))*100
    n = input("Cifras (n): ")
    es = (0.5 * (10**(2-n)))
    #Esto es para ES
    print("El es tolerancia porcentual es: " + str(es) + " %")

    x0 = input("X0 : ")
    x1 = input("X1 : ")
    x2 = input("X2 : ")
    while abs(ea) > es:
        counter += 1
        print(" ")
        print( "Iteracion " + str(counter))              

        h0 = x1 - x0
        h1 = x2 - x1


        d0 = ((funcion(x1) - funcion(x0))/float(h0))

        d1 = ((funcion(x2) - funcion(x1))/float(h1))
        
        a = ((d1-d0)/float(h1+h0))
        b = a*h1 + d1
        c = funcion(x2)

        print("A " + str(a))
        print("B " + str(b))
        print("C " + str(c))
        d0 = (funcion(x1) - funcion(x0)/float(h0))
        d1 = (funcion(x2) - funcion(x1)/float(h1))
        #Aqui se obtiene la propuesta de raiz para cada iteracion

        x3 = calcX3(x2,c,b,a)

        print("Evaluar esto en la funcion X3: " + str(x3))
        x0 = x1
        x1 = x2
        x2 = x3

        tempva = va
        va = x3
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
 
    print(str(x3))
    print("El valor que haya en este nivel de error sera correcto hasta " + str(n) +" cifras")
muller()