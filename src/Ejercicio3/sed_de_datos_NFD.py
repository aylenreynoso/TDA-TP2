import random
import time
import math
import matplotlib.pyplot as plt

from First_Fit_Decreasing import FFD
from Next_Fit_Decreasing import NFD

def generar_set_datos(tamano, seed):
    random.seed(seed)
    return [round(random.uniform(0.01, 1), 2) for _ in range(tamano)]

def medir_tiempo(func, *args):
    inicio = time.perf_counter()
    resultado = func(*args)
    fin = time.perf_counter()
    return resultado, fin - inicio

def ejecutar_experimentos(algoritmo, nombre_alg):
    tamanios = [1000, 5000, 10000, 15000, 30000, 50000]
    seeds =   [10,     20,     30,     40,      50,      60]


    tiempos = []

    print(f"\n=== Resultados para {nombre_alg} ===")

    for tamano, seed in zip(tamanios, seeds):
        data = generar_set_datos(tamano, seed)
        resultado, tiempo = medir_tiempo(algoritmo, data)

        tiempos.append(tiempo)
        print(f"{tamano} elementos | {tiempo:.8f}s | contenedores = {resultado}")

    return tamanios, tiempos

if __name__ == "__main__":

     # Ejecutamos NFD y obtenemos tiempos medidos
    tamanos_nfd, tiempos_nfd = ejecutar_experimentos(NFD, "NFD")

    # Gráfico comparando tiempos medidos de NFD con su complejidad teórica O(n log n)
    plt.figure(figsize=(8,5))
    plt.plot(tamanos_nfd, tiempos_nfd, marker="o", label="NFD tiempo medido")

    # Curva teórica O(n log n)
    curva_nfd = [n * math.log(n) for n in tamanos_nfd]
    factor_nfd = tiempos_nfd[0] / curva_nfd[0]  # escalamos para comparación visual
    curva_nfd_scaled = [c * factor_nfd for c in curva_nfd]
    plt.plot(tamanos_nfd, curva_nfd_scaled, marker="x", linestyle="--", label="O(n log n) teórica")

    plt.title("Comparación de tiempos de NFD con su complejidad teórica")
    plt.xlabel("Tamaño del input (n)")
    plt.ylabel("Tiempo (s)")
    plt.legend()
    plt.grid(True)
    plt.show()