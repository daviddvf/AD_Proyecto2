import math


class UtilMath:
    @staticmethod
    def getIntervalo(polnmcoeffs:list[float]):

        coeffsList = []
        for i in range(len(polnmcoeffs)):
            if i != 0:
                coeffsList.append(abs(polnmcoeffs[i])/abs(polnmcoeffs[0]))
        x = 1 + max(coeffsList)
        inter = [x * -1, x]
        return inter

    @staticmethod
    def getDerivada(polnmcoeffs:list[float]):
        grado = len(polnmcoeffs) - 1
        coeffsList = []

        for i in range(grado):
            a = polnmcoeffs[i] * (grado-i)
            coeffsList.append(a)
        return coeffsList

    @staticmethod
    def evaluarFuncion(polnmcoeffs:list[float], x):
        terminos = len(polnmcoeffs)
        grado = len(polnmcoeffs) - 1
        y = 0

        for i in range(len(polnmcoeffs)):
            if i != terminos - 1:
                y += polnmcoeffs[i] * (x ** (grado - i))
            else:
                y += polnmcoeffs[i]
        return y

    @staticmethod
    def divisionSintetica(polnmcoeffs:list[float], x):
        divPolnm = []
        m = 0
        for i in range(len(polnmcoeffs)):
            if i == 0:
                divPolnm.append(polnmcoeffs[i])
                m = x * polnmcoeffs[i]
            else:
                divPolnm.append(polnmcoeffs[i] + m)
                m = x * (polnmcoeffs[i] + m)
        divPolnm.pop()
        return divPolnm

    @staticmethod
    def formulaGen(polnmcoeffs:list[float]):
        a = polnmcoeffs[0]
        b = polnmcoeffs[1]
        c = polnmcoeffs[2]
        if len(polnmcoeffs) != 3:
            raise ValueError("Error: Ecuacion es diferente de 2do grado.")
        d = (b**2) - (4 * a * c)

        if d >= 0:
            x1 = (-b-math.sqrt(d))/(2*a)
            x2 = (-b+math.sqrt(d))/(2*a)
            r = [x1, x2]
            return r
        else:
            coeff = ""
            raiz = math.sqrt(-1 * d)
            if - b % (2 * a) == 0:
                coeff = str(- b / (2 * a))
            else:
                coeff = str(-1 * b) + "/" + str(2 * a)
            coeffi = ""

            if raiz % (2 * a) == 0:                          #Sin residuo

                if raiz.is_integer():                     #es entero
                    coeffi = str(raiz / (2 * a)) + "i"
                else:                                        #no es entero
                    coeffi = "√" + str(-d) + "/" + str(2 * a) + "i"
            else:                                            #con residuo
                if raiz.is_integer():
                    coeffi = str(raiz) + "i/" + str(2 * a)
                else:
                    coeffi = "√" + str(-d) + "i/" + str(2 * a)
            if coeff != "0.0":
                r = [coeff + "-" + coeffi, coeff + "+" + coeffi]
            else:
                r = ["-" + coeffi,"+" + coeffi]
            return r

    @staticmethod
    def factPolinmRaizNula(polnmcoeffs:list[float]):
        n = len(polnmcoeffs)
        polin = []
        for i in range(n):
            if i !=0 and i != n -1 :
                polin.append(polnmcoeffs[i])
        return polin




