import matplotlib.pyplot as plt

# ---------- LER OS DADOS ----------
tempos = {}
with open("tempoSimulacao.txt", "r") as f:
    for linha in f:
        if ":" in linha:
            chave, valor = linha.strip().split(":")
            try:
                tempos[chave.strip()] = float(valor.strip().replace("ms", ""))
            except:
                pass

# ---------- EXIBIR NO TERMINAL ----------
print("\n📈 Resultados de desempenho:")
for chave, valor in tempos.items():
    print(f"{chave}: {valor:.2f} ms")

# ---------- GERAR GRÁFICO ----------
labels = list(tempos.keys())
values = list(tempos.values())

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, values, color=["#1f77b4", "#ff7f0e", "#2ca02c", "#9467bd"])
plt.title("Comparação de Desempenho - Forest Fire")
plt.ylabel("Tempo (ms)")
plt.grid(axis="y", linestyle="--", alpha=0.6)

# Adicionar valores nas barras
for bar, valor in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f"{valor:.1f} ms", ha='center', va='bottom', fontsize=10)

# Rotaciona os subtítulos e ajusta espaçamento
plt.xticks(rotation=15, ha="right")
plt.tight_layout()

plt.savefig("grafico_tempos.png", dpi=300)
plt.show()

print("\n✅ Gráfico salvo como 'grafico_tempos.png'")
