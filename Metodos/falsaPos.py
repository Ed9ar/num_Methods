
import numpy as np
from numpy import pi
import math

'''
vv = input("Valor Verdadero: ")
def funcion(x):
    #definir aqui la funcion
    res = 0
    #print( "Valor en funcion " + str(float(x**2)))
    res = float((3.5967*x)/(math.sqrt(((x**2)+0.81)**3))-1)
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
        #xr = xu - ((funcion(xu)*(xl-xu)/float((funcion(xl)-funcion(xu)))))
        xr = ((xu*funcion(xl))/(funcion(xl)-funcion(xu))- (xl*funcion(xu))/(funcion(xl)-funcion(xu)))
        print("Evaluar esto en la funcion (FALSA POS) XR: " + str(xr))
        tempva = va
        va = xr
        vaa = tempva
        print("Comparativo "+ str(funcion(xr)))
        if (funcion(xr)*funcion(xl)) < 0:
            xl = xr
            xu = xu
        elif (funcion(xr)*funcion(xl)) > 0:
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
        #print("El error aproximado porcentual es: " + str(ea))
        print("El error aproximado porcentual es: " + str(ea)) 

    print(str(xr))
    print("El valor que haya en este nivel de error sera correcto hasta " + str(n) +" cifras")

falsaPos()
'''
import math
#se define la funcion f donde se esta utilizando un parametro que es x.
def f(x):
#en este apartado se estan declarando variables.
  g=9.8
  m=68.1
  t=10
  v=40
  #esta la formula que implementa el libro.
  res = float((3.5967*x)/(math.sqrt(((x**2)+0.81)**3))-1)
  return res
# 
def tol(n):
  resultado=0.5
  return resultado
  
def ErrorVerdadero(vaverd,aproxact):
  resultado=(vaverd-aproxact)/vaverd*100
  return abs(resultado)
  
def ErrorRelativo(xr,auxiliar):
  resultado=((xr-auxiliar)/xr*100)
  return abs(resultado)
  
print("ingrese el valor inferior del intervalo")
xl=float(input())

print("ingrese el valor superior del intervalo")
xu=float(input())

while(f(xl)* f(xu)>0):
  print("no hay una raiz en el intervalo")
  print("ingrese el valor inferior del intervalo")
  xl=float(input())
  print("ingrese el valor superior del intervalo")
  xu=float(input())
print("si hay una raiz en el intervalo")
xr= xu-(f(xu)*(xl-xu))/(f(xl)-f(xu))
vr=1.5097851
tolerancia=tol(3)
auxiliar=0
ErrorVerd=ErrorVerdadero(vr,xr)
ErrorRel=ErrorRelativo(xr,auxiliar)
contador=0
while(ErrorRel>tolerancia):
  contador+=1
  auxiliar=xr
  xr= xu-(f(xu)*(xl-xu))/(f(xl)-f(xu))
  if f(xl)*f(xr)<0:
    xu=xr
  else:
    if f(xu)*f(xr)<0:
        xl=xr 
    else:
      print("la raiz real es: " , xr)
  ErrorVerd=ErrorVerdadero(vr,xr)
  print("La iteracion actual es: ", contador)
  print("la raiz es: ", xr)
  print("el error verdadero es: ", ErrorVerd)
  if (contador>=2):
    ErrorRel=ErrorRelativo(xr,auxiliar)
    print("y su error Relativo es: " , ErrorRel)
    print("----------------------------------------")
  else:
    print("el primer error relativo no se puede calcular")
    print("----------------------------------------")
print("la raiz aproximada es: " , xr, "y se obtuvo en ", contador, "iteraciones")
