import math
import sys
def normalizar_vector(vector, suma = 0):
    """
    Normaliza un vector dado
    """
    for i in range(len(vector)):
        suma += vector[i].real**2 + vector[i].imag**2
    result = math.sqrt(suma)
    return result

def Producto_int_2_vectores(A, B):
    """
    Producto interno de dos vectores
    """
    if len(A) != len(B):
        print("Deben tener ambos la misma longuitud")
        sys.exit()
    return sum(v1 * v2 for v1, v2 in zip(A, B))

def conjugar_vector(vector):
    """
    Conjunga un vector dado
    """
    conjugar = [complex(x.real, -x.imag) for x in vector]
    return conjugar

def Cal_Prob_Posi(vector, posicion, denominador = 0):
    """
    El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
    (list2d, int) -> float 
    """
    for i in range(len(vector)):
        denominador += math.sqrt(vector[i].real**2 + vector[i].imag**2)**2
    denominador, numerador = math.sqrt(denominador), vector[posicion]
    result = (math.sqrt(numerador.real**2 + numerador.imag**2)**2/denominador**2)*100
    return result

def Cal_Prob_Posi_Doble(vector1, vector2):
    """
    El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
    """
    if not len(vector1) == len(vector2):
        sys.exit()
    vector2 = conjugar_vector(vector2)
    N_vector1, N_vector2 = normalizar_vector(vector1), normalizar_vector(vector2)
    
    for i in range(len(vector1)):
        vector1[i], vector2[i] = vector1[i]/N_vector1, vector2[i]/N_vector2
    result = Producto_int_2_vectores(vector1, vector2)
    return result

def amplitud_de_transicion(vector1, vector2):
    """
    Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
    """
    numerador = Producto_int_2_vectores(conjugar_vector(vector1), vector2)
    denominador = normalizar_vector(vector1) * normalizar_vector(vector2)
    result = numerador/denominador
    return result
