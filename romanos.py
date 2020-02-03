valores = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
valores5 = {'V':5, 'L':50, 'D':500}
simbolosOrdenados = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

def romano_a_arabigo(numRomano):
    numArabigo = 0
    numRepes = 1
    ultimoCaracter = ''
    for letra in numRomano:  
        #recorrer de izquierda a derecha el número romano
        
        #incrementamos el valor del número arábigo con el valor númerico del símbolo romano
        if letra in valores:
            numArabigo += valores[letra]
            if ultimoCaracter == '':
                pass
            elif valores[ultimoCaracter] > valores[letra]:
                numRepes = 1
            elif valores[ultimoCaracter] == valores[letra]:
                numRepes += 1
                if letra in valores5:
                    return 0
                if numRepes > 3:
                    return 0
            elif valores[ultimoCaracter] < valores[letra]:
                if numRepes > 1:
                    return 0
                
                if ultimoCaracter in valores5:
                    return 0
                
                distancia = simbolosOrdenados.index(letra) - simbolosOrdenados.index(ultimoCaracter)
                if distancia > 2:
                    return 0

                numArabigo -= valores[ultimoCaracter]*2
                numRepes = 1
        
        else: 
            #si el símbolo romano no es permitido devolvemos error(0)
            return 0
        ultimoCaracter = letra

    return numArabigo