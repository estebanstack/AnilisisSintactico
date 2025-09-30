

EPSILON = "ε"


def es_terminal(simbolo):
    return simbolo.islower() or simbolo.isdigit() or simbolo in {"uno", "dos", "tres", "cuatro", "cinco", "seis"}

def inicializar_conjuntos(G):
    conjuntos = {}
    for nt in G:
        conjuntos[nt] = set()
    return conjuntos


def calcular_primeros(G):
    primeros = inicializar_conjuntos(G)
    cambio = True

    while cambio:
        cambio = False
        for A in G:
            for prod in G[A]:
                for simbolo in prod:
                    if es_terminal(simbolo):
                        if simbolo not in primeros[A]:
                            primeros[A].add(simbolo)
                            cambio = True
                        break
                    else:
                        antes = len(primeros[A])
                        primeros[A] |= (primeros[simbolo] - {EPSILON})
                        if EPSILON not in primeros[simbolo]:
                            break
                        if len(primeros[A]) != antes:
                            cambio = True
                else:
                    if EPSILON not in primeros[A]:
                        primeros[A].add(EPSILON)
                        cambio = True
    return primeros


def calcular_siguientes(G, primeros, simbolo_inicial):
    siguientes = inicializar_conjuntos(G)
    siguientes[simbolo_inicial].add("$")

    cambio = True
    while cambio:
        cambio = False
        for A in G:
            for prod in G[A]:
                for i in range(len(prod)):
                    B = prod[i]
                    if not B.isupper():
                        continue
                    if i + 1 < len(prod):
                        beta = prod[i + 1:]
                        for s in beta:
                            if es_terminal(s):
                                if s not in siguientes[B]:
                                    siguientes[B].add(s)
                                    cambio = True
                                break
                            else:
                                antes = len(siguientes[B])
                                siguientes[B] |= (primeros[s] - {EPSILON})
                                if len(siguientes[B]) != antes:
                                    cambio = True
                                if EPSILON not in primeros[s]:
                                    break
                        else:
                            
                            antes = len(siguientes[B])
                            siguientes[B] |= siguientes[A]
                            if len(siguientes[B]) != antes:
                                cambio = True
                    else:
                        
                        antes = len(siguientes[B])
                        siguientes[B] |= siguientes[A]
                        if len(siguientes[B]) != antes:
                            cambio = True
    return siguientes


def calcular_predicciones(G, primeros, siguientes):
    predicciones = {}
    for A in G:
        for prod in G[A]:
            conjunto = set()
            for simbolo in prod:
                if es_terminal(simbolo):
                    conjunto.add(simbolo)
                    break
                else:
                    conjunto |= (primeros[simbolo] - {EPSILON})
                    if EPSILON not in primeros[simbolo]:
                        break
            else:
                conjunto |= siguientes[A]
            predicciones[(A, tuple(prod))] = sorted(conjunto)
    return predicciones


G1 = {
    "S": [["A", "uno", "B", "C"], ["S", "dos"]],
    "A": [["B", "C", "D"], ["A", "tres"], [EPSILON]],
    "B": [["D", "cuatro", "C", "tres"], [EPSILON]],
    "C": [["cinco", "D", "B"], [EPSILON]],
    "D": [["seis"], [EPSILON]]
}

G2 = {
    "S": [["A", "B", "uno"]],
    "A": [["dos", "B"], [EPSILON]],
    "B": [["C", "D"], ["tres"], [EPSILON]],
    "C": [["cuatro", "A", "B"], ["cinco"]],
    "D": [["seis"], [EPSILON]]
}


def probar(G, nombre):
    print(f"\n--- {nombre} ---")
    primeros = calcular_primeros(G)
    print("PRIMEROS:")
    for nt in G:
        print(f"  {nt} = {primeros[nt]}")

    siguientes = calcular_siguientes(G, primeros, "S")
    print("\nSIGUIENTES:")
    for nt in G:
        print(f"  {nt} = {siguientes[nt]}")

    pred = calcular_predicciones(G, primeros, siguientes)
    print("\nPREDICCION:")
    for regla, conj in pred.items():
        A, prod = regla
        print(f"  {A} → {' '.join(prod)}  =>  {conj}")


probar(G1, "Gramatica Ejercicio 1")
probar(G2, "Gramatica Ejercicio 2")
