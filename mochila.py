def es_solucion(solucion, capacidad):
    """Determina si el conjunto solución es una solución válida"""
    total = 0
    for elemento in solucion:
            total = round(total + elemento[1], 2)
    if total == capacidad:
        return True
    else:
        return False


def mochila(conjunto_candidatos, capacidad):
     """Algoritmo voraz para resolver el problema de la mochila."""
     solucion = []
     restante = capacidad
     while conjunto_candidatos and not es_solucion(solucion, capacidad):
        dato = conjunto_candidatos.pop()
        if dato[1] <= restante:
            solucion.append(dato)
            restante = round(restante - dato[1], 2)
    
        return solucion