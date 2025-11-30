import numpy as np
import matplotlib.pyplot as plt

k = np.arange(1, 21)

certeza = (1 - (0.5)**k) * 100

plt.figure(figsize=(6, 4))
plt.scatter(k, certeza)

plt.xlabel("Cantidad de repeticiones (k)")
plt.ylabel("Grado de certeza (%)")
plt.title("Certeza vs Repeticiones en la prueba de Zero-Knowledge con prover honesto")

plt.xticks(k)
plt.yticks(np.arange(50, 101, 5))
plt.grid(True)

plt.tight_layout()
plt.show()
