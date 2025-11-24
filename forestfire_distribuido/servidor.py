import socket
import pickle
import numpy as np
import time
import struct

HOST = "0.0.0.0"
PORT = 5000

# ---------- PARÂMETROS ----------
EMPTY = 0
TREE = 1
BURNING = 2
p = 0.3
steps = 50

def update_forest(forest, N):
    new_forest = forest.copy()
    for i in range(N):
        for j in range(N):
            if forest[i, j] == BURNING:
                new_forest[i, j] = EMPTY
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < N:
                            if forest[ni, nj] == TREE and np.random.rand() < p:
                                new_forest[ni, nj] = BURNING
    return new_forest

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print("🖥️ Servidor aguardando conexão...")

while True:
    conn, addr = server.accept()
    print(f"Conectado por {addr}")

    # Lê o tamanho dos dados
    data_len_bytes = conn.recv(8)
    data_len = struct.unpack('Q', data_len_bytes)[0]

    # Recebe os dados
    data = b""
    while len(data) < data_len:
        packet = conn.recv(4096)
        if not packet:
            break
        data += packet

    # Desempacota floresta e parâmetros
    forest, N = pickle.loads(data)

    # Processa simulação
    start = time.time()
    for _ in range(steps):
        forest = update_forest(forest, N)
    end = time.time()

    tempo_dist = (end - start) * 1000

    # Envia de volta floresta final e tempo
    response = pickle.dumps((forest, tempo_dist))
    conn.sendall(struct.pack('Q', len(response)) + response)

    conn.close()
    print("✅ Resultado enviado ao cliente.")
