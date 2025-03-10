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
        if len(polnmcoeffs) != 3:
            raise ValueError("Error: Ecuacion es diferente de 2do grado.")
