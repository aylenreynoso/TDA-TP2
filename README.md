# TP2 — Redes de flujo, Heurísticas Greedy y Randomización

Este repositorio contiene los scripts usados para resolver y experimentar con:
- **Redes de flujo / Programación Lineal Entera (ILP)**: minimizar la cantidad de enlaces utilizados cumpliendo demanda y capacidades.
- **Bin Packing (heurísticas greedy)**: *Next-Fit Decreasing (NFD)* y *First-Fit Decreasing (FFD)*.
- **Algoritmos randomizados**: gráfico de “certeza vs repeticiones” (tipo prueba interactiva / ZKP simplificada).

---

## Requisitos

- **Python 3.9+** 
- Dependencias:
  - `pulp`
  - `numpy`
  - `matplotlib`


---

## Configuración del entorno

### 1) Crear y activar entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2) Instalar dependencias

```bash
pip install pulp numpy matplotlib

```

### 3) Desactivar entorno virtual

```bash
deactivate
```

---

## Cómo correr cada script

> Ejecutar estos comandos desde la carpeta donde están los `.py`.

---

### Ejercicio 1 — Red de flujo (ILP con PuLP)

**Archivo:** `ejercicio_1.py`

Este script modela una red con:
- variables de flujo por dirección,
- capacidades por arista,
- conservación de flujo en nodos,
- y **minimización de enlaces usados** (decisión binaria).

Además, produce una salida con:
- estado del solver,
- valor de función objetivo,
- enlaces utilizados y flujos (por sentido),
- y el balance por nodo.

**Ejecutar:**
```bash
python3 ejercicio_1.py
```

**Salida:**
- genera un archivo con las salidas de resultado y ademas se mostraran en terminal.

---

### Heurísticas Greedy — Bin Packing (NFD / FFD)

**Archivos:**
- `Next_Fit_Decreasing.py` → implementación de **NFD**
- `First_Fit_Decreasing.py` → implementación de **FFD**


---

### Experimentos — Tiempos (NFD vs curva teórica `O(n log n)`)

**Archivo:** `sed_de_datos_NFD.py`

Este script:
- genera conjuntos aleatorios de distintos tamaños (por ejemplo: 1000, 5000, 10000, 15000, 30000, 50000),
- ejecuta el algoritmo NFD varias veces por tamaño y promedia,
- grafica los tiempos medidos contra una curva teórica escalada `n log n`.

**Ejecutar:**
```bash
python3 sed_de_datos_NFD.py
```

---

### Ejercicio 4 — Randomizado (gráfico “certeza vs repeticiones”)

**Archivo:** `ejercicio4_randomizado_grafico.py`

Grafica cómo crece la certeza en función de la cantidad de repeticiones `k` usando:
\[
\text{certeza}(k) = (1 - (0.5)^k)\cdot 100
\]

**Ejecutar:**
```bash
python3 ejercicio4_randomizado_grafico.py
```

---

## Estructura del proyecto (referencia)

```text
TDA-TP2/
├── Resultados/
│   ├── resultado_red_programacion_lineal.txt
├── src/
│   ├── Ejercicio1/
│   │   ├── ejercicio_1.py
│   ├── Ejercicio3/
│   │   ├── First_Fit_Decreasing.py
│   │   ├── Next_Fit_Decreasing.py
│   │   ├── sed_de_datos_NFD.py
│   ├── Ejercicio4/
│   │   ├── ejercicio4_randomizado_grafico.py
├── .gitignore
└── README.md
```

---

## Notas importantes

- Si `pulp` no encuentra un solver, normalmente se usa **CBC**. En caso de problemas, reinstalá:
  ```bash
  pip install --upgrade pulp
  ```
- Los scripts con `matplotlib` abren una ventana. Si estás en un entorno sin interfaz gráfica (ej. servidor), podés reemplazar el `plt.show()` por:
  ```python
  plt.savefig("grafico.png")
  ```
- Para replicar resultados comparables, conviene fijar una semilla en la generación aleatoria cuando aplique (por ejemplo, con `random.seed(...)` o `numpy.random.seed(...)`).

---