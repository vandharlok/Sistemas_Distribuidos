import socket
import pickle
import numpy as np
import time
import struct

HOST = "127.0.0.1"  # alterar para IP do servidor, se estiver em outra máquina
PORT = 5000

# ---------- PARÂMETROS ----------
N = 200
p = 0.3
steps = 50
EMPTY = 0
TREE = 1
BURNING = 2

np.random.seed(42)
forest = np.random.choice([TREE, EMPTY], size=(N, N), p=[0.7, 0.3])
forest[N//2, N//2] = BURNING

# ---------- ENVIA PARA O SERVIDOR ----------
start_total = time.time()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = pickle.dumps((forest, N))
    s.sendall(struct.pack('Q', len(data)) + data)

    # Recebe tamanho dos dados
    data_len_bytes = s.recv(8)
    data_len = struct.unpack('Q', data_len_bytes)[0]

    # Recebe floresta processada
    data = b""
    while len(data) < data_len:
        packet = s.recv(4096)
        if not packet:
            break
        data += packet

forest_final, tempo_servidor = pickle.loads(data)

end_total = time.time()
tempo_total = (end_total - start_total) * 1000

# ---------- SALVA RESULTADOS ----------
with open("../tempoSimulacao.txt", "a") as f:
    f.write(f"Tempo distribuído (servidor): {tempo_servidor:.2f} ms\n")
    f.write(f"Tempo total (cliente + servidor): {tempo_total:.2f} ms\n")

print(f"✅ Simulação distribuída concluída!")
print(f"🕒 Tempo no servidor: {tempo_servidor:.2f} ms")
print(f"🌐 Tempo total (cliente+servidor): {tempo_total:.2f} ms")
