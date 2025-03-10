from Birge_Vieta import *


#n = int(input("Grado = "))
polinm = [1,-7,13,23,-78]
#for i in range(n+1):
    #if i + 1 != n+1:
        #polinm.append(float(input("X^"+str(n-i)+":")))
    #else:
        #polinm.append(float(input("C:")))
#Birge_Vieta.iniciarIteracion(polinm)
print(UtilMath.divisionSintetica(polinm,3))
