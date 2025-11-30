"""
    https://en.wikipedia.org/wiki/Next-fit-decreasing_bin_packing


    Aqui se encuentra la descripcion de este problema que nos ayudara a resolver
    a partir de una heuristica (Greedy), con una aproximacion <= 2 OPT.
    
    La cual es mas que suficiente la cual cumple la consigna(aproximacion <= 2 OPT)
"""

def NFD(objetos):
    
    if len(objetos) < 1:
        return 0

    objetos_ordenados = sorted(objetos, reverse=True)# Ordenar de mayor a menor - O(nlog(n))

    empaquetar = [[1.0, []]]

    for objeto in objetos_ordenados: # O(n)
        tam, contenedor = empaquetar[-1]  # siempre el ÚLTIMO contenedor

        if objeto <= tam:
            empaquetar[-1][0] -= objeto
            contenedor.append(objeto)
        else:
            empaquetar.append([1.0 - objeto, [objeto]])

    return len(empaquetar)