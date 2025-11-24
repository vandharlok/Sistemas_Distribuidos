import numpy as np
import time
import threading
import  matplotlib.pyplot as plt
# ---------- PARÂMETROS ----------
N = 200
p = 0.3
steps = 50
num_threads = 4  # número de threads usadas

EMPTY = 0
TREE = 1
BURNING = 2

np.random.seed(42)
forest = np.random.choice([TREE, EMPTY], size=(N, N), p=[0.7, 0.3])
forest[N//2, N//2] = BURNING

# ---------- FUNÇÃO DE ATUALIZAÇÃO (PARCIAL) ----------
def process_section(start_row, end_row, forest, new_forest):
    for i in range(start_row, end_row):
        for j in range(N):
            if forest[i, j] == BURNING:
                new_forest[i, j] = EMPTY
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < N:
                            if forest[ni, nj] == TREE and np.random.rand() < p:
                                new_forest[ni, nj] = BURNING

# ---------- EXECUÇÃO PARALELA ----------
start = time.time()

for step in range(steps):
    new_forest = forest.copy()
    threads = []
    rows_per_thread = N // num_threads

    for t in range(num_threads):
        start_row = t * rows_per_thread
        end_row = (t + 1) * rows_per_thread if t != num_threads - 1 else N
        thread = threading.Thread(target=process_section,
                                  args=(start_row, end_row, forest, new_forest))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    forest = new_forest.copy()

end = time.time()
tempo_paralelo = (end - start) * 1000

# ---------- SALVA RESULTADOS ----------
with open("tempoSimulacao.txt", "a") as f:
    f.write(f"Tempo paralelo ({num_threads} threads): {tempo_paralelo:.2f} ms\n")

print(f"✅ Simulação paralela concluída com {num_threads} threads em {tempo_paralelo:.2f} ms")


plt.imshow(forest, cmap='hot', interpolation='nearest')
plt.title(f"Forest Fire - Último passo ({num_threads} threads)")
plt.show()
