import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplstereonet
from mplstereonet import parse_plunge_bearing

if len(sys.argv) < 2:
    print("Uso: python3 eigen_fish_meanvectors.py archivo.csv")
    sys.exit(1)

df = pd.read_csv(sys.argv[1])
strike = df['strike'].values
dip = df['dip'].values

# Eigenvectores (plunges, bearings y eigenvalores)
plu, bear, eigenvals = mplstereonet.eigenvectors(strike, dip)

print("Eigenvalores:", eigenvals)
print("Plunges:", plu)
print("Bearings:", bear)

#EMPEZAMOS EL MODULO DEL GRAFICO
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='stereonet')

poles_strike = []
poles_dip = []

for idx, row in df.iterrows():
    s, d = row['strike'], row['dip']
    poles_strike.append(s)
    poles_dip.append(d)
    ax.plane(s, d, color='black', linewidth=0.75)
    ax.pole(s, d, marker='o', color='black', markersize=3)
    if 'rake' in df.columns:
        ax.rake(s, d, row['rake'])

cax = ax.density_contourf(poles_strike, poles_dip, measurement='poles', cmap='Reds')
fig.colorbar(cax, ax=ax, label='Densidad', location='right', pad=0.1)

colors = ['red', 'green', 'blue']
labels = ['E₁', 'E₂', 'E₃']

# Graficar eigenvectores con diferente color y etiqueta
for i, (plunge, bearing) in enumerate(zip(plu, bear)):
    ax.line(
        plunge, bearing,
        marker='*',
        markersize=12,
        linestyle='',
        color=colors[i],
        markeredgecolor='black',
        markeredgewidth=0.5,
        label=labels[i]
    )

# Leyenda para los eigenvectores (abajo centrado)
ax.legend(loc='upper center', bbox_to_anchor=(1, 1), ncol=3, fontsize=11, frameon=True)

# Leyenda con los valores numéricos (abajo izquierda)
eig_text = "Valores Eigenvectores:\n"
for i, (val, p, b) in enumerate(zip(eigenvals, plu, bear)):
    eig_text += f"{labels[i]}: Val={val:.3f}, Plg={p:.1f}°, Az={b:.1f}°\n"
ax.text(-0.05, -0.25, eig_text, fontsize=9, ha='left', va='bottom', transform=ax.transAxes,
        bbox=dict(facecolor='white', alpha=0.75, edgecolor='gray'))

# Quitar la leyenda azimutal
ax.set_azimuth_ticks([])

ax.legend(
    loc='upper center',         # posición base (arriba centrado, pero la moveremos abajo)
    bbox_to_anchor=(1, 1), # (x, y): x=0.5 centrado horizontal, y negativo la mueve abajo
    fontsize=9,
    frameon=True                # (opcional) para ponerle marco a la leyenda
)
ax.grid()
plt.title("Planos, Polos, Eigenvectores")
plt.show()