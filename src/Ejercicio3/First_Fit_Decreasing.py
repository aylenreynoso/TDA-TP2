"""
    https://en.wikipedia.org/wiki/First-fit-decreasing_bin_packing

    Aqui se encuentra la descripcion de este problema que nos ayudara a resolver
    a partir de una heuristica (Greedy), con una aproximacion <= 1.22 OPT.
    
    La cual es mas que suficiente la cual cumple la consigna(aproximacion <= 2 OPT)
"""

def FFD(objetos):

    if len(objetos) < 1:
        return 0

    objetos_ordenados = sorted(objetos, reverse=True)  #Ordenamos de mayor a menor - O(nlog(n))

    empaquetar = [[1.0,[]]]

    for objeto in objetos_ordenados: # O(n)
        empaqueto = False
        for i in range(len(empaquetar)): #O(m)
            tam, contenedor = empaquetar[i]
            if objeto <= tam:
                empaquetar[i][0] -= objeto
                contenedor.append(objeto)
                empaqueto = True 
                break
        if not empaqueto:
            empaquetar.append([1.0-objeto,[objeto]])

    return len(empaquetar)