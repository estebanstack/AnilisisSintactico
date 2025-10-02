Esteban Castro Rojas - Juan Sebastian Gonzalez Alvarez

# Descripción del proyecto

Este proyecto implementa el ejercicio realizado anteriormente de analizador sintáctico predictivo, diseñado para calcular automáticamente los conjuntos PRIMEROS, SIGUIENTES y las PREDICCIONES de cada producción.

El programa está escrito en Python y permite trabajar con distintas gramáticas, facilitando el análisis sintáctico en el desarrollo de compiladores o intérpretes.

El objetivo de este analizador es automatizar el proceso de análisis sintáctico para gramáticas tipo LL(1), proporcionando al usuario las herramientas necesarias para verificar si una gramática puede ser analizada mediante un parser predictivo.

# Gramatica

S → A uno B C

S → S dos

A → A tres

A → ε

B → D cuatro C tres

B → ε

C → cinco D B

C → ε

D → seis

D → ε

- No Terminales: S, A, B, C, D
- Terminales: uno, dos, tres, cuatro, cinco, seis
- ε representa la cadena vacía.

# Estructura del programa

El código contiene varias funciones principales:

- es_terminal(): Determina si un símbolo es terminal, es decir, si pertenece al lenguaje final reconocido por la gramática.
- inicializar_conjuntos(): Crea un diccionario vacío para inicializar los conjuntos de PRIMEROS o SIGUIENTES para cada no terminal.
- calcular_primeros(): Calcula el conjunto PRIMEROS de cada no terminal. Incluye los terminales que pueden aparecer al inicio de una derivación. Propaga ε cuando una producción puede derivar en cadena vacía.
- calcular_siguientes(): Calcula el conjunto SIGUIENTES para cada no terminal. Usa la relación entre producciones para determinar qué terminales pueden seguir a cada símbolo. Agrega $ (fin de entrada) al conjunto de SIGUIENTES del símbolo inicial.
- calcular_predicciones(): Calcula el conjunto de PREDICCIÓN para cada producción. Combina la información de PRIMEROS y SIGUIENTES para definir el conjunto de entrada válido para cada regla.

# Ejecución del programa

El archivo principal incluye dos gramáticas de prueba (G1 y G2) y una función probar() que ejecuta el análisis completo:

probar(G1, "Gramatica Ejercicio 1")
probar(G2, "Gramatica Ejercicio 2")

En la terminal, escribir al tener el archivo localizado.
python analizador.py
