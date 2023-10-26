# Libreria de Teoría Cuántica Básica, Observables Y Medidas

Este repositorio contiene pruebas unitarias para un módulo llamado `OperacionesVectorescplx`, el cual proporciona operaciones relacionadas con números complejos. Las pruebas están escritas utilizando el marco de trabajo `unittest` de Python.

### Autor
Juan Sebastian Buitrago Piñeros

## Instalación

1. Clona el repositorio en tu máquina local:
git clone https://github.com/Juanseproo/pruebas-numeros-complejos.git

2. Cambia al directorio del proyecto:

3. Asegúrate de tener Python instalado. El código está escrito en Python 3.

## Ejecución de las Pruebas

Para ejecutar las pruebas unitarias, sigue estos pasos:

1. Abre una terminal o línea de comandos.

2. Navega al directorio del proyecto si aún no estás allí.

3. Ejecuta el siguiente comando:

Esto ejecutará el conjunto de pruebas y mostrará los resultados.

## Casos de Prueba 1ra Parte

El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. El simulador debe permitir especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

### `adicion()`

    Adición de matrices complejas.
    (list(2d), list(2d)) -> list(2d)

### `matriz_I()`

    Da una matriz identidad con filas y columnas n y valor de diagonal x
    (int, int) -> list(2d)

### `hermitiana()`

    Comprueba si la matriz es igual a su traspuesta conjugada
    list2d -> bool

### `accion()`

    Función para calcular la "acción" de una matriz sobre un vector.
    (list(2d), list) -> list

### `normalizar()`

    Normaliza un vector dado
    (list, int) -> int

### `PInterno()`

    Producto interno de dos vectores
    (list, list) -> int

### `conjugar_vector()`

    Conjunga un vector dado
    list -> list

### `Cal_Prob_Posi()`

    El sistema debe calcular la probabilidad de encontrarlo en una posición en particular.
    Φ = Vector complejo
    (list, int, int) -> float 
    (cj)/||Φ⟩|²

### `Cal_Prob_Posi_Doble()`

    El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo. |Φ> --> |Ψ>
    Φ = Vector complejo (Inicial)
    Ψ = Vector complejo (Final)
    (list, list) --> float
    |⟨φ|ψ⟩|²

### `Cal_Prob_Posi_Doble_Normalizada()`

    El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo, pero el resultado esta entre 0 y 1 |Φ> --> |Ψ> 
    Φ = Vector complejo (Inicial)
    Ψ = Vector complejo (Final)
    (list, list) --> float
    |⟨φ|ψ⟩|² / (||φ⟩|²*||ψ⟩|²)

### `amplitud_de_transicion()`

    Amplitud de transición. El sisxtema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación
    φ = Vector complejo (Inicial)
    ψ = Vector complejo (Final)
    (list, list) --> float
    ⟨φ|ψ⟩

### `amplitud_de_transicion_normalizada()`

    Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación, pero el resultado esta entre 0 y 1
    φ = Vector complejo (Inicial)
    ψ = Vector complejo (Final)
    (list, list) --> float
    ⟨φ|ψ⟩ / ∣∣φ⟩∣⋅∣∣ψ⟩∣

### `varianza_y_media_del_observable()`

    Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula 
    la media y la varianza del observable en el estado dado.
    Ω = Matriz compleja
    ψ = Vector complejo
    (list(2d), list(2d)) -> (int, int)

### `valores_vectores()`

    Calcula los valores propios y los vectores propios de una matriz compleja.
    Ω = Matriz compleja
    list(2d) -> valoresprops, vectores

### `probabilidades_vectores()`

    La probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.
    (list, list(2d), int) -> float

### Licencia

Este proyecto está autorizado bajo la licencia MIT; consulte el archivo LICENSE.md para obtener más información.
