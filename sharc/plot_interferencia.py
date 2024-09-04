import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados do arquivo
dados = np.loadtxt('/home/rayssa/sharc/sharc/output/[SYS] CDF of system interference power from IMT DL.txt')

# Extrair as colunas necessárias
interferencia_dBW = dados[:,0] - 30
prob_interferencia = 1 - dados[:,1]

# Criar o gráfico
plt.figure(figsize=(10,5))
plt.plot(interferencia_dBW, prob_interferencia, label="50 km")
plt.title("IMT downlink - RAS adjacent-channel simulation results (CCDF)")
plt.legend(loc='lower left')
plt.xlabel("Interferência (dBW)")
plt.ylabel("Probabilidade de Interferência > X")
plt.yscale('log')

# Adicionar linhas de grade
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

# Salvar o gráfico como uma imagem (opcional)
plt.savefig('interferencia_plot.png')

# Mostrar o gráfico
plt.show()
