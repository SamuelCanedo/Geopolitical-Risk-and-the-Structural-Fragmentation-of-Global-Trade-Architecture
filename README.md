# Empirical analysis evaluates 3 nested panel specifications:
- Pooled Ordinary Least Squares (OLS)
- Two-Way Fixed Effects (TWFE)
- Dynamic Panel Data framework.

# Geopolitical Risk and the Structural Fragmentation of Global Trade Architecture

This repository contains the data pipeline and econometric specifications for an empirical macroeconometrics study evaluating how geopolitical instability reshapes international trade integration.

---

## 📂 Project Structure

```text
├── data/
│   ├── control_variables.csv                  # Inflation and GDP growth (World Bank WDI)
│   └── data_gpr.xls - Sheet1.csv              # Caldara & Iacoviello Geopolitical Risk (GPR) Index
├── src/
│   ├── dataset_for_termpaper_econometrics.py  # Data cleaning, long-pivoting, and master merge
│   └── panel_data_gpr.py                      # Econometric estimation (Pooled OLS, TWFE, Dynamic Panel)
├── docs/
│   └── paper_term_int_econ.pdf                # Full Research Paper (PDF)
└── README.md
