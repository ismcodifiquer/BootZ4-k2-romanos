class RomanNumber():
    __valores = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    __valores5 = {'V':5, 'L':50, 'D':500}
    __simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']


    __rangos = {
        0: {1: 'I', 5: 'V', 'next': 'X'},
        1: {1: 'X', 5: 'L', 'next': 'C'},
        2: {1: 'C', 5: 'D', 'next': 'M'},
        3: {1: 'M', 'next': ''}
    }

    def __init__(self, value):
        self.value = value
        self.__romanValue = self.__arabigo_a_romano()

    def __invertir(self, cad):
        return cad[::-1]

    def __gruposDeMil(self):
        cad = str(self.value)
        dac = self.__invertir(cad)
        grupos = []
        
        rango = 0

        for i in range(0, len(dac), 3):
            grupos.append([rango, int(self.__invertir(dac[i:i+3]))])
            rango += 1

        for i in range(len(grupos)-1):
            grupoMenor = grupos[i]
            grupoMayor = grupos[i+1]
            unidadesMayor = grupoMayor[1] % 10
            
            if unidadesMayor < 4:
                grupoMenor[1] += unidadesMayor * 1000
                grupoMayor[1] -= unidadesMayor


        grupos.reverse()
        return grupos

    def __arabigo_individual(self, valor):
        cad = self.__invertir(str(valor))
        res = ''

        for i in range(len(cad)-1, -1, -1):
            digit = int(cad[i])
            if digit <= 3:
                res += digit*self.__rangos[i][1]
            elif digit == 4:
                res += (self.__rangos[i][1] + self.__rangos[i][5])
            elif digit == 5:
                res += self.__rangos[i][5]
            elif digit < 9:
                res += (self.__rangos[i][5] + self.__rangos[i][1] * (digit-5))
            else:
                res += self.__rangos[i][1] + self.__rangos[i]['next']

        return res
  

    def __arabigo_a_romano(self):

        g1000 = self.__gruposDeMil()
        romanoGlobal = ''

        for grupo in g1000:
            rango = grupo[0]
            numero = grupo[1]
            
            if numero > 0:
                miRomano = '(' * rango + self.__arabigo_individual(numero) + ')' * rango
            else:
                miRomano = ''

            romanoGlobal += miRomano

        return romanoGlobal

    def __str__(self):
        return "'{}'".format(self.__romanValue)

    def __repr__(self):
        return self.__romanValue

    def __add__(self, value):
        return RomanNumber(value) + self.value
