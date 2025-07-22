import matplotlib.pyplot as plt
import numpy as np

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
consumo_original = [1450, 1420, 1380, 1300, 1250, 1200, 1350, 1400, 1380, 1420, 1450, 1500]
consumo_economizado = [1100, 1080, 1050, 950, 900, 850, 1000, 1050, 1020, 1070, 1100, 1150]
bandeiras = ["Verde"]*7 + ["Vermelha"]*4 + ["Verde"]  # Jan-Jul: Verde | Ago-Nov: Vermelha | Dez: Verde

# Cores baseadas na bandeira
cores_bandeira = ["green" if b == "Verde" else "red" for b in bandeiras]

# Gráfico de comparação
plt.figure(figsize=(14, 6))
bar_width = 0.35
x = np.arange(len(meses))

plt.bar(x - bar_width/2, consumo_original, width=bar_width, color="gray", label="Consumo Original")
plt.bar(x + bar_width/2, consumo_economizado, width=bar_width, color="lightgreen", label="Com Economia")

# Destacar bandeiras
for i, (orig, econ) in enumerate(zip(consumo_original, consumo_economizado)):
    plt.text(i - bar_width/2, orig + 20, f"R$ {orig*0.6:.0f}", ha="center", fontsize=8 if bandeiras[i] == "Verde" else 9, color="black")
    plt.text(i + bar_width/2, econ + 20, f"R$ {econ*0.6:.0f}", ha="center", fontsize=8, color="black")
    if bandeiras[i] == "Vermelha":
        plt.text(i - bar_width/2, orig + 70, f"+R$ {orig*8.5:.0f}", ha="center", fontsize=8, color="red")

plt.title("Comparação de Consumo: Original vs. Economizado (Brasília - Bandeiras Verde/Vermelha)", fontsize=14)
plt.xlabel("Mês")
plt.ylabel("Consumo (kWh)")
plt.xticks(x, meses)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()