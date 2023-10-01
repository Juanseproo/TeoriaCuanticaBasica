import math
def Cal_Prob_Posi(vector, posicion):
    """
    El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
    (list2d, int) -> float 
    """
    denominador = 0
    for i in range(len(vector)):
        denominador += math.sqrt(vector[i].real**2 + vector[i].imag**2)**2
    denominador = math.sqrt(denominador)
    numerador = vector[posicion]
    result = (math.sqrt(numerador.real**2 + numerador.imag**2)**2/denominador**2)*100
    return result
