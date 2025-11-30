import pulp as pl

def construir_modelo(nodes, edges_cap, supply):
    """
    nodes: lista de nodos (por ej. [1,2,...,10])
    edges_cap: dict { (i,j): cap_ij } con aristas no dirigidas
    supply: dict { i: b_i } con oferta/demanda (MB)
             b_i < 0: nodo emisor
             b_i > 0: nodo receptor
             sum(b_i) debe ser 0
    """
    # Conjunto de arcos dirigidos
    arcs = []
    for (i, j) in edges_cap.keys():
        arcs.append((i, j))
        arcs.append((j, i))

    # Modelo
    prob = pl.LpProblem("TP2_Red_Facultad", pl.LpMinimize)

    # Variables de flujo x_ij >= 0 (MB)
    x = pl.LpVariable.dicts(
        "x",
        arcs,
        lowBound=0,
        cat="Continuous"
    )

    # Variables binarias y_ij: 1 si se usa la arista {i,j}
    y = pl.LpVariable.dicts(
        "y",
        edges_cap.keys(),
        lowBound=0,
        upBound=1,
        cat="Binary"
    )

    # ---------- Función objetivo ----------
    prob += pl.lpSum(y[(i, j)] for (i, j) in edges_cap.keys()), "Min_cantidad_enlaces"

    # ---------- Restricciones ----------

    # Capacidad de cada arista no dirigida
    for (i, j), cap in edges_cap.items():
        prob += (
            x[(i, j)] + x[(j, i)] <= cap * y[(i, j)],
            f"capacidad_{i}_{j}"
        )

    # Conservación de flujo en cada nodo
    for k in nodes:
        inflow  = pl.lpSum(x[(i, j)] for (i, j) in arcs if j == k)
        outflow = pl.lpSum(x[(i, j)] for (i, j) in arcs if i == k)
        prob += (
            inflow - outflow == supply[k],
            f"balance_nodo_{k}"
        )

    return prob, x, y, arcs


def resolver_y_mostrar(prob, x, y, nodes, arcs, edges_cap, archivo_salida=None):
    prob.solve(pl.PULP_CBC_CMD(msg=True))
    status = pl.LpStatus[prob.status]
    obj_val = pl.value(prob.objective)
    texto = []
    texto.append(f"Estado de la solución: {status}")
    texto.append(f"Valor función objetivo (cantidad de enlaces usados): {obj_val:.0f}\n")

    texto.append("Enlaces utilizados y flujos:")
    for (i, j) in edges_cap.keys():
        if pl.value(y[(i, j)]) > 0.5:
            flujo_ij = pl.value(x[(i, j)])
            flujo_ji = pl.value(x[(j, i)])
            flujo_total = flujo_ij + flujo_ji
            if flujo_total > 1e-6:
                texto.append(
                    f" - Arista ({i},{j}) usada: flujo total = {flujo_total:.2f} MB "
                    f"({flujo_ij:.2f} de {i}->{j}, {flujo_ji:.2f} de {j}->{i})"
                )

    texto.append("\nBalance de cada nodo:")
    for k in nodes:
        inflow = sum(pl.value(x[(i, j)]) for (i, j) in arcs if j == k)
        outflow = sum(pl.value(x[(i, j)]) for (i, j) in arcs if i == k)
        texto.append(
            f" Nodo {k}: entra = {inflow:.2f} MB, sale = {outflow:.2f} MB, "
            f"entra-sale = {inflow - outflow:.2f}"
        )

    print("\n".join(texto))

    if archivo_salida is not None:
        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write("\n".join(texto))


if __name__ == "__main__":
    nodes = list(range(1, 11))

    edges_cap = {
        (1, 2): 5,
        (1, 3): 5,
        (2, 6): 4,
        (2, 9): 2,
        (2, 5): 2,
        (3, 5): 3,
        (3, 4): 3,
        (3, 7): 2,
        (4, 7): 1,
        (4, 8): 4,
        (5, 7): 2,
        (6, 9): 3,
        (7, 10): 4,
        (8, 10): 3,
        (9, 10): 3,
    }

    supply = {i: 0 for i in nodes}
    supply[1] = -10
    supply[10] = 10

    assert abs(sum(supply.values())) < 1e-6, "La suma de b_i debe ser 0"

    prob, x, y, arcs = construir_modelo(nodes, edges_cap, supply)
    resolver_y_mostrar(prob, x, y, nodes, arcs, edges_cap, archivo_salida="resultado_red.txt")
