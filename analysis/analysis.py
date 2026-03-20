# analysis.py — Impacto Sanitario en Venezuela (2024–2025): Indicadores Clave, Factores y Datos de Enfermedades
# DOI: 10.5281/zenodo.18948118
# Author: de la Serna Tuya, Juan Moisés · ORCID: 0000-0002-8401-8018
# License: CC0 1.0

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import warnings
warnings.filterwarnings("ignore")

# ── LOAD DATA ─────────────────────────────────────────────────────────────
# Download dataset from: https://doi.org/10.5281/zenodo.18948118
# df = pd.read_csv("dataset.csv")

# Example with synthetic data
import numpy as np
np.random.seed(42)
years = list(range(2000, 2024))
keywords = []

df = pd.DataFrame({
    "year": years,
    **{k.lower().replace(" ","_")[:15]: np.random.normal(50, 15, len(years))
       for k in keywords[:4]}
})

print(f"Dataset: Impacto Sanitario en Venezuela (2024–2025): Indica")
print(f"DOI: 10.5281/zenodo.18948118")
print(f"Shape: {df.shape}")
print("\nFirst rows:")
print(df.head())
print("\nSummary statistics:")
print(df.describe())

# ── VISUALIZATION ─────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Impacto Sanitario en Venezuela (2024–2025): Indicadores Clav", fontsize=11, fontweight="bold")

# Plot 1: Temporal trend
ax1 = axes[0]
for col in df.columns[1:3]:
    ax1.plot(df["year"], df[col], marker="o", markersize=3, label=col)
ax1.set_xlabel("Year")
ax1.set_ylabel("Value")
ax1.set_title("Temporal Trends")
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)

# Plot 2: Distribution
ax2 = axes[1]
df.iloc[:, 1:5].mean().plot(kind="bar", ax=ax2, color=["#1f6feb","#f85149","#3fb950","#e3b341"])
ax2.set_title("Variable Means")
ax2.set_xlabel("Variable")
ax2.set_ylabel("Mean Value")
ax2.tick_params(axis="x", rotation=30)
ax2.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("figures/analysis_output.png", dpi=150, bbox_inches="tight")
print("\nFigure saved: figures/analysis_output.png")

# ── CITATION ──────────────────────────────────────────────────────────────
print(f"""
Citation:
de la Serna Tuya, Juan Moisés (2026). Impacto Sanitario en Venezuela (2024–2025): Indicadores Clave, Factore. Zenodo. https://doi.org/10.5281/zenodo.18948118
""")
