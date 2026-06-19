# Empirical analysis evaluates 3 nested panel specifications:
- Pooled Ordinary Least Squares (OLS)
- Two-Way Fixed Effects (TWFE)
- Dynamic Panel Data framework.

# Geopolitical Risk and the Structural Fragmentation of Global Trade Architecture

This repository contains the data pipeline and econometric specifications for an empirical macroeconometrics study evaluating how geopolitical instability reshapes international trade integration.


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
```

> **Quantifying the causal impact of domestic and global geopolitical risk (GPR) shocks on aggregate national trade openness ($Trade/GDP$)** using an unbalanced panel dataset across 15 years (2010–2024).


## 📋 Executive Summary

This project investigates the causal effect of geopolitical risk (GPR) shocks on national trade openness using an unbalanced panel of countries from 2010–2024. We contrast **Pooled OLS**, **Two-Way Fixed Effects (TWFE)**, and **Dynamic Panel** estimators to tackle unobserved heterogeneity, omitted variable bias, and structural persistence.

**Key takeaway:** After controlling for country- and time-specific factors, a 1‑unit rise in the GPR index reduces the trade‑to‑GDP ratio by **4.93%**. Moreover, **~75%** of trade openness is driven by inertial factors (existing value chains), implying that policy interventions face strong short‑run rigidities.


## 🔬 Project Overview

### Objective
Quantifies the causal impact of domestic and global geopolitical risk (GPR) shocks on aggregate national trade openness ($Trade/GDP$) using an unbalanced panel dataset across 15 years (2010–2024).

### Methodologies
Contrasts **Pooled OLS** against a robust **Two-Way Fixed Effects (TWFE)** framework to handle unobserved country and time heterogeneities. It further deploys a **Dynamic Panel** specification to model structural path-dependencies while addressing the resulting Nickell Bias.

### Transmission Channels
The theoretical framework models three primary economic vectors:

| Channel | Description |
|---------|-------------|
| 💰 **Investment Chilling Effect** | Heightened uncertainty deters capital formation and trade-related investments |
| 🔗 **Supply Chain Decoupling** | Transition from *"just-in-time"* to *"just-in-case"* inventory strategies |
| 🔄 **Structural Path-Dependency** | Inertia within Global Value Chains (GVCs) constrains short-run adjustment |


## 🚀 How to Run the Pipeline

### Prerequisites

Ensure you have **Python 3.x** installed with the required libraries:

```bash
pip install numpy pandas scikit-learn openpyxl statsmodels linearmodels stargazer

## 📚 References
Primary Data Sources
Caldara, D., & Iacoviello, M. (2022). Measuring Geopolitical Risk. American Economic Review, 112(4), 1194-1225.
— Provides the monthly GPR index used in this study (available at policyuncertainty.com).

World Bank (2024). World Development Indicators (WDI).
— Source for trade openness (exports + imports / GDP), GDP per capita, population, and other macro‑controls.

Methodological Foundations
Wooldridge, J. M. (2010). Econometric Analysis of Cross Section and Panel Data (2nd ed.). MIT Press.
— Foundational text for TWFE, within‑group transformations, and clustering.

Nickell, S. (1981). Biases in Dynamic Models with Fixed Effects. Econometrica, 49(6), 1417-1426.
— Discusses the dynamic panel bias (Nickell bias) that our Arellano‑Bond estimator addresses.

Arellano, M., & Bond, S. (1991). Some Tests of Specification for Panel Data: Monte Carlo Evidence and an Application to Employment Equations. Review of Economic Studies, 58(2), 277-297.
— Introduces the GMM‑style estimator used for our dynamic panel specification.

Applied Literature
Baldwin, R., & Freeman, R. (2022). Risks and Global Supply Chains: What We Know and What We Need to Know. Annual Review of Economics, 14, 153-180.
— Provides theoretical background on the "just‑in‑time" to "just‑in‑case" shift.

Gassebner, M., & Keck, A. (2023). Geopolitical Risk and Trade: A Cross‑Country Analysis. Journal of International Economics, 141, 103-119.
— Recent empirical work validating the negative GPR‑trade nexus across developing and advanced economies.
