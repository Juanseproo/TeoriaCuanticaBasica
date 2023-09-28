import sys
import math
def Producto_int_2_vectores(A, B):
    """
    Producto interno de dos vectores
    """
    if len(A) != len(B):
        print("Deben tener ambos la misma longuitud")
        sys.exit()
    return sum(v1 * v2 for v1, v2 in zip(A, B))

def Cal_Prob_Posi(vector, posicion):
    vector_daga = [complex(x.real, -x.imag) for x in vector]
    denominador = math.sqrt(Producto_int_2_vectores(vector, vector_daga).real)
    prob = (posicion.real**2 + posicion.imag**2 / denominador**2) - 1
    return prob
