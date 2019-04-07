import numpy as np

vv = input("Valor Verdadero: ")

def errorRelativo(val):
    va = val
    ev = vv - va
    er = (ev/float(vv)) * 100
    print("El error verdadero es: " + str(ev))
    print("El error relativo porcentual es: " + str(er))

def errorAprox():
    va = input("Valor Aproximado Actual: ")
    errorRelativo(va)
    vaa = input("Valor Aproximado Anterior: ")
    ea = ((va-vaa)/float(va))*100
    n = input("Cifras (n), si conoces es oprime 0: ")

    if n== 0:
        es = input("es : ")
    else:
        es = (0.5 * (10**(2-n)))
    
    print("El es tolerancia porcentual es: " + str(es) + " %")
    print("El error aproximado porcentual es: " + str(ea))
    
    while abs(ea) > es:
        vaa = va
        va = input("Valor Aproximado Actual: ")
        errorRelativo(va)
        ea = ((va-vaa)/float(va))*100
        print("El error aproximado porcentual es: " + str(ea))
    print("El valor que haya en este nivel de error sera correcto hasta " + str(n) +" cifras")

errorAprox()