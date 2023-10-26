import math
import sys
import numpy as np
#Juan Sebastian Buitrago Piñeros CNYT
def adicion(matriz1, matriz2):
    """
    Adición de matrices complejas.
    (list(2d), list(2d)) -> list(2d)
    """
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices no tienen las mismas dimensiones y no se pueden sumar")
    return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]

def matriz_I(n, x):
    """
    Da una matriz identidad con filas y columnas n y valor de diagonal x
    (int, int) -> list(2d)
    """
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                fila.append(x)
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

def hermitiana(matriz):
    """
    Comprueba si la matriz es igual a su traspuesta conjugada
    list2d -> bool
    """
    return np.allclose(matriz, np.conj(matriz.T))

def accion(matriz, vector):
    """
    Función para calcular la "acción" de una matriz sobre un vector.
    (list(2d), list) -> list
    """
    if len(matriz[0]) != len(vector):
        print("El número de columnas de la matriz debe ser igual a la longitud del vector.")
        sys.exit()
    result = [sum(matriz[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]
    return result 

def normalizar(vector, suma = 0):
    """
    Normaliza un vector dado
    (list, int) -> int
    """
    for i in range(len(vector)):
        suma += vector[i].real**2 + vector[i].imag**2
    result = math.sqrt(suma)
    return result

def PInterno(A, B):
    """
    Producto interno de dos vectores
    (list, list) -> int
    """
    if len(A) != len(B):
        print("Deben tener ambos la misma longuitud")
        sys.exit()
    return sum(v1 * v2 for v1, v2 in zip(A, B))

def conjugar_vector(vector):
    """
    Conjunga un vector dado
    list -> list
    """
    conjugar = [complex(x.real, -x.imag) for x in vector]
    return conjugar

def Cal_Prob_Posi(Φ, posicion, denominador = 0):
    """
    El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
    Φ = Vector complejo
    (list, int, int) -> float 
    (cj)/||Φ⟩|²
    """
    for i in range(len(Φ)):
        denominador += math.sqrt(Φ[i].real**2 + Φ[i].imag**2)**2
    denominador, numerador = math.sqrt(denominador), Φ[posicion]
    result = (math.sqrt(numerador.real**2 + numerador.imag**2)**2/denominador**2)*100
    return result

def Cal_Prob_Posi_Doble(Φ, Ψ):
    """
    El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo. |Φ> --> |Ψ>
    Φ = Vector complejo (Inicial)
    Ψ = Vector complejo (Final)
    (list, list) --> float
    |⟨φ|ψ⟩|²
    """
    if not len(Φ) == len(Ψ):
        raise ValueError("Los vectores deben tener la misma longitud para calcular la probabilidad de transición.")
    bra_Ψ = conjugar_vector(Ψ)
    result = abs(PInterno(bra_Ψ, Φ))**2
    return result

def Cal_Prob_Posi_Doble_Normalizada(Φ, Ψ):
    """
    El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo, pero el resultado esta entre 0 y 1 |Φ> --> |Ψ> 
    Φ = Vector complejo (Inicial)
    Ψ = Vector complejo (Final)
    (list, list) --> float
    |⟨φ|ψ⟩|² / (||φ⟩|²*||ψ⟩|²)
    """
    numerador, denominador = Cal_Prob_Posi_Doble(Φ, Ψ), normalizar(Φ)**2 * normalizar(Ψ)**2
    return numerador/denominador

def amplitud_de_transicion(φ, ψ):
    """
    Amplitud de transición. El sisxtema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
    φ = Vector complejo (Inicial)
    ψ = Vector complejo (Final)
    (list, list) --> float
    ⟨φ|ψ⟩
    """
    bra_φ = conjugar_vector(φ)
    numerador = PInterno(bra_φ, ψ)
    return numerador

def amplitud_de_transicion_normalizada(φ, ψ):
    """
    Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación, pero el resultado esta entre 0 y 1
    φ = Vector complejo (Inicial)
    ψ = Vector complejo (Final)
    (list, list) --> float
    ⟨φ|ψ⟩ / ∣∣φ⟩∣⋅∣∣ψ⟩∣
    """
    numerador = amplitud_de_transicion(φ, ψ)
    denominador = normalizar(φ) * normalizar(ψ)
    return numerador/denominador

def varianza_y_media_del_observable(Ω, ψ):
    """
    Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula 
    la media y la varianza del observable en el estado dado.
    Ω = Matriz compleja
    ψ = Vector complejo
    (list(2d), list(2d)) -> (int, int)
    """
    if hermitiana(np.array(Ω)) == False:
        sys.exit()
    bra_ψ = conjugar_vector(ψ)
    media = PInterno(bra_ψ, accion(Ω, ψ))
    var = PInterno(bra_ψ, accion(adicion(Ω,  matriz_I(len(Ω), -round(media.real))), ψ))
    return round(media.real), var

def valores_vectores(Ω):
    """
    Calcula los valores propios y los vectores propios de una matriz compleja.
    Ω = Matriz compleja
    list(2d) -> valoresprops, vectores
    """
    valores, vectores = np.linalg.eig(Ω)
    lista_valores = [val for val in valores]
    lista_vectores = [[v for v in vector] for vector in vectores]
    return lista_valores, lista_vectores

def probabilidades_vectores(inicial, observable, posicion):
    """
    La probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.
    (list, list(2d), int) -> float
    """
    vectores = valores_vectores(observable)[1]
    return amplitud_de_transicion(inicial, vectores[posicion])


"""
----------------------------------------------------------------------------------------
# Ejercicio 4.3.1
----------------------------------------------------------------------------------------
# Vector inicial :

v = [[1, 0], [0, 0]]

observable = [[0, 0, 1, 0], [1, 0, 0, 0]]

vr = accion(observable, v)

valores, vectores = valores_vectores(observable)

print("El resultado de la observacion es: ", vr)

print("Los valores propios son: ", valores, "y sus vectores propios son: ", vectores, ")
----------------------------------------------------------------------------------------
# Ejercicio 4.3.2
----------------------------------------------------------------------------------------
# prob = probabilidades_vectores(vr, observable, 1)
----------------------------------------------------------------------------------------
# Excercise 4.4.1
----------------------------------------------------------------------------------------
v1 = [[0, 0, 1, 0], [1, 0, 0, 0]]
v2 = [[math.sqrt(2)/2, math.sqrt(2)/2], [math.sqrt(2)/2, -math.sqrt(2)/2, 0)]]

"""
