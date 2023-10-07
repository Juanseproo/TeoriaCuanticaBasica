import math
import sys
import numpy as np

def accion_de_una_matriz(matriz, vector):
    """
    Función para calcular la "acción" de una matriz sobre un vector.
    """
    if len(matriz[0]) != len(vector):
        print("El número de columnas de la matriz debe ser igual a la longitud del vector.")
        sys.exit()
    result = [sum(matriz[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]
    return result    

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

def amplitud_de_transicion(φ, ψ):
    """
    Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
    φ = Vector complejo
    ψ = Vector complejo
    """
    numerador = Producto_int_2_vectores(conjugar_vector(φ), ψ)
    denominador = normalizar_vector(φ) * normalizar_vector(ψ)
    result = numerador/denominador
    return result

def varianza_del_observable(φ, ψ):
    """
    Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.
    φ = Matriz compleja
    ψ = Vector complejo
    """
    hermitiana = np.allclose(φ, φ.conj().T)
    if hermitiana == False:
        sys.exit()
    media = np.dot(ψ.conj().T, np.dot(φ, ψ)).real
    varianza = np.dot(ψ.conj().T, np.dot(φ**2, ψ)).real - media**2
    return varianza
