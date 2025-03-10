from UtilMath import *
class Birge_Vieta:

    def __init__(self, coeffs):
        self.polnmCoeffsList: list[float] = coeffs
        self.raices = []

    def iniciarBirgeVieta(self):
        grado = len(self.polnmCoeffsList) - 1
        polnmList = self.polnmCoeffsList
        for i in range(grado - 2):
            r = self.iniciarIteracion(polnmList)
            self.raices = r
            polnmList = UtilMath.divisionSintetica(polnmList,r)

    @staticmethod
    def iniciarIteracion(polnmcoeffs:list[float]):

        interv = UtilMath.getIntervalo(polnmcoeffs)
        polnmDervcoeffs = UtilMath.getDerivada(polnmcoeffs)

        return Birge_Vieta.NewtonRaphsonMetd(interv,polnmcoeffs,polnmDervcoeffs, 0.0000001)

    @staticmethod
    def NewtonRaphsonMetd(interv:list[float],polnmcoeffs:list[float], polnmDervcoeffs:list[float], e:float):
        i:int = 0
        xi = interv[0]
        error: float = 1
        while error > e:

            xinext = xi - (UtilMath.evaluarFuncion(polnmcoeffs,xi)/UtilMath.evaluarFuncion(polnmDervcoeffs,xi))
            error = abs((xinext - xi)/xinext)
            print("---------------------------")
            print(" i | Xi | F(Xi) | Xi+1 | e |")
            print(str(i), " | ", str(xi), " | ", str(UtilMath.evaluarFuncion(polnmcoeffs,xi)), " | ", str(xinext), " | ", str(error), " |" )
            print("---------------------------")
            xi = xinext
            i += 1
        return xi




