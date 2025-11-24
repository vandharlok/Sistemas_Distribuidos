import numpy as np
import matplotlib.pyplot as plt
import time

# ---------- PARÂMETROS ----------
N = 200          # tamanho da floresta (NxN)
p = 0.3          # probabilidade de propagação do fogo
steps = 50       # número de iterações da simulação

# ---------- ESTADOS ----------
EMPTY = 0
TREE = 1
BURNING = 2

# ---------- INICIALIZAÇÃO ----------
np.random.seed(42)
forest = np.random.choice([TREE, EMPTY], size=(N, N), p=[0.7, 0.3])
forest[N//2, N//2] = BURNING  # foco inicial do fogo

# ---------- FUNÇÃO DE ATUALIZAÇÃO ----------
def update_forest(forest):
    new_forest = forest.copy()
    for i in range(N):
        for j in range(N):
            if forest[i, j] == BURNING:
                new_forest[i, j] = EMPTY
                # vizinhos
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < N:
                            if forest[ni, nj] == TREE and np.random.rand() < p:
                                new_forest[ni, nj] = BURNING
    return new_forest

# ---------- EXECUÇÃO SEQUENCIAL ----------
start = time.time()
for step in range(steps):
    forest = update_forest(forest)
end = time.time()
tempo_seq = (end - start) * 1000

# ---------- SALVA RESULTADOS ----------
with open("tempoSimulacao.txt", "w") as f:
    f.write(f"Tempo sequencial: {tempo_seq:.2f} ms\n")

print(f"✅ Simulação sequencial concluída em {tempo_seq:.2f} ms")

# ---------- VISUALIZAÇÃO ----------
plt.imshow(forest, cmap='hot', interpolation='nearest')
plt.title("Forest Fire - Último passo (Sequencial)")
plt.show()
