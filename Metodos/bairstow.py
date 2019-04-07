import math
import numpy as np
import sys

#vv = input("Valor Verdadero: ")


def bairstow():
    counter = 0
    vaa = 2
    va = 1
    
    ear = 2
    eas = 2

    #Esto es para ES
    #print("El es tolerancia porcentual es: " + str(es) + " %")
    #definir aqui la funcion
    r = -1
    s = -1
    #print( "Valor en funcion " + str(float(x**2)))
    funciona = np.array([0.531441, 0, -10.96810827, 0, 2.34, 0, 1])
    #funciona = np.array([1.25, -3.875, 2.125, 2.75, -3.5, 1, 0])
    print(funciona)
    while(ear >= 0.5 and eas >= 0.5):
        counter = counter + 1
        #res = float((75*(math.e**(-1.5*x))+(20*(math.e**(-0.075*x)))-15))
        print("Iteracion  "+ str(counter))
        #Pasar arreglo
        b6 = funciona[6]
        b5 = funciona[5] + r* b6
        b4 = funciona[4] + r* b5 +s* b6
        b3 = funciona[3] + r* b4 + s * b5 
        b2 = funciona[2] + r* b3 + s *b4
        b1 = funciona[1] + r* b2 + s * b3
        b0 = funciona[0] + r* b1 + s * b2

        funcionb = np.array([b0,b1,b2,b3,b4,b5,b6])
        print(funcionb)

        c6 = funcionb[6]
        c5 = funcionb[5] + r* c6
        c4 = funcionb[4] + r* c5 + s * c6
        c3 = funcionb[3] + r* c4 + s * c5
        c2 = funcionb[2] + r* c3 + s * c4
        c1 = funcionb[1] + r* c2 + s * c3
        c0 = funcionb[0] + r* c1 + s * c2

        funcionc = np.array([c0,c1,c2,c3,c4,c5,c6])
        print(funcionc)

        a = np.array([[c2,c3], [c1,c2]])
        b = np.array([-b1,-b0])
        solucion = np.linalg.solve(a, b)
        print("Solucion")
        print(solucion)
        #Delta r
        rd= solucion[0]
        #Delta s
        sd= solucion[1]
        tempr = r 
        temps = s

        #Aqui se ajustan r y s
        r = rd + r 
        s = sd + s
        print("R:" + str(r))
        print("S:" + str(s))
        ear= abs((r-tempr)/r)*100
        print("Error aprox r" + str(ear))

        eas= abs((s-temps)/s)*100
        print("Error aprox s" + str(eas))
        #funciona = funcionc
        #print(funciona)
        try:
            x1 = (r+(math.sqrt((r**2)+(4*(s)))/2))
            x2 = (r-(math.sqrt((r**2)+(4*(s)))/2))
        except:
            print("Una raiz o mas son imaginarias")
            x1 = (r+(math.sqrt((r**2)+(4*(abs(s)))/2)))
            x2 = (r-(math.sqrt((r**2)+(4*(abs(s)))/2)))


        print("X1 " + str(x1))
        print("X2 " + str(x2))
        print(" ")
    
    #Se realiza la division
    counter = 0
    vaa = 2
    va = 1
    
    ear = 2
    eas = 2

    #definir aqui la funcion
    r = -1
    s = -1
    #print( "Valor en funcion " + str(float(x**2)))
    funciona = np.array([-10.8466, 0, 2.479, 0, 1, 0, 0])
    #funciona = np.array([1.25, -3.875, 2.125, 2.75, -3.5, 1, 0])
    print(funciona)
    while(ear >= 0.5 and eas >= 0.5):
        counter = counter + 1
        #res = float((75*(math.e**(-1.5*x))+(20*(math.e**(-0.075*x)))-15))
        print("Iteracion  "+ str(counter))
        #Pasar arreglo
        b6 = funciona[6]
        b5 = funciona[5] + r* b6
        b4 = funciona[4] + r* b5 +s* b6
        b3 = funciona[3] + r* b4 + s * b5 
        b2 = funciona[2] + r* b3 + s *b4
        b1 = funciona[1] + r* b2 + s * b3
        b0 = funciona[0] + r* b1 + s * b2

        funcionb = np.array([b0,b1,b2,b3,b4,b5,b6])
        print(funcionb)

        c6 = funcionb[6]
        c5 = funcionb[5] + r* c6
        c4 = funcionb[4] + r* c5 + s * c6
        c3 = funcionb[3] + r* c4 + s * c5
        c2 = funcionb[2] + r* c3 + s * c4
        c1 = funcionb[1] + r* c2 + s * c3
        c0 = funcionb[0] + r* c1 + s * c2

        funcionc = np.array([c0,c1,c2,c3,c4,c5,c6])
        print(funcionc)

        a = np.array([[c2,c3], [c1,c2]])
        b = np.array([-b1,-b0])
        solucion = np.linalg.solve(a, b)
        print("Solucion")
        print(solucion)
        #Delta r
        rd= solucion[0]
        #Delta s
        sd= solucion[1]
        tempr = r 
        temps = s

        #Aqui se ajustan r y s
        r = rd + r 
        s = sd + s
        print("R:" + str(r))
        print("S:" + str(s))
        ear= abs((r-tempr)/r)*100
        print("Error aprox r" + str(ear))

        eas= abs((s-temps)/s)*100
        print("Error aprox s" + str(eas))
        #funciona = funcionc
        #print(funciona)
        try:
            x1 = (r+(math.sqrt((r**2)+(4*(s)))/2))
            x2 = (r-(math.sqrt((r**2)+(4*(s)))/2))
        except:
            print("Una raiz o mas son imaginarias")
            x1 = (r+(math.sqrt((r**2)+(4*(abs(s)))/2)))
            x2 = (r-(math.sqrt((r**2)+(4*(abs(s)))/2)))


        print("X1 " + str(x1))
        print("X2 " + str(x2))
        print(" ")
bairstow()
