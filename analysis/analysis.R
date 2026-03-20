# analysis.R — Impacto Sanitario en Venezuela (2024–2025): Indicadores Clave, Factores y Datos de Enfermedades
# DOI: 10.5281/zenodo.18948118
# Author: de la Serna Tuya, Juan Moisés · ORCID: 0000-0002-8401-8018
# License: CC0 1.0

# ── SETUP ──────────────────────────────────────────────────────────────────
# Install required packages if needed:
# install.packages(c("readr","ggplot2","dplyr","tidyr"))

library(readr)
library(ggplot2)
library(dplyr)

# ── LOAD DATA ──────────────────────────────────────────────────────────────
# Download dataset from: https://doi.org/10.5281/zenodo.18948118
# df <- read_csv("dataset.csv")

# Example with synthetic data
set.seed(42)
years <- 2000:2023
df <- data.frame(
  year = years,
  
  stringsAsFactors = FALSE
)

cat("Dataset: Impacto Sanitario en Venezuela (2024–2025): Indica\n")
cat("DOI: 10.5281/zenodo.18948118\n")
cat("Dimensions:", nrow(df), "x", ncol(df), "\n\n")
print(head(df))
print(summary(df))

# ── VISUALIZATION ──────────────────────────────────────────────────────────
# Temporal trend
p1 <- df %>%
  tidyr::pivot_longer(-year, names_to="variable", values_to="value") %>%
  ggplot(aes(x=year, y=value, color=variable)) +
  geom_line(size=0.8) +
  geom_point(size=1.5) +
  labs(title="Impacto Sanitario en Venezuela (2024–2025): Indicadores",
       subtitle="DOI: 10.5281/zenodo.18948118",
       x="Year", y="Value",
       caption="de la Serna Tuya, Juan Moisés · 2026") +
  theme_minimal() +
  theme(legend.position="bottom")

ggsave("figures/analysis_output_r.png", p1, width=10, height=6, dpi=150)
cat("\nFigure saved: figures/analysis_output_r.png\n")

# ── CITATION ───────────────────────────────────────────────────────────────
cat("\nCitation:\n")
cat("de la Serna Tuya, Juan Moisés (2026). Impacto Sanitario en Venezuela (2024–2025): Indicadores Clave, Factore. Zenodo. https://doi.org/10.5281/zenodo.18948118\n")
