# panel_data_grp.py
# Samuel Canedo - Intemediate Econometrics - Term Paper

import pandas as pd
import numpy as np
import os
from linearmodels.panel import PooledOLS, PanelOLS
import statsmodels.api as sm

# Load the dataset
script_dir = os.path.dirname(__file__)  
file_path = os.path.join(script_dir, 'master_panel.csv')

df = pd.read_csv(file_path)

# Eliminate rows with missing values 
df_clean = df.dropna(subset=['trade', 'gpr', 'gdp_growth', 'inflation']).copy()

# Set the multi-index for panel data
df_clean['country_code'] = df_clean['country_code'].astype('category')
df_clean = df_clean.set_index(['country_code', 'year'])

# Define the independent variables and the dependent variable
exog_vars = ['gpr', 'gdp_growth', 'inflation']
Y = df_clean['trade']

# ------------------------------------------
# 1st model: Pooled OLS (Bias model)
# ------------------------------------------

X_pooled = sm.add_constant(df_clean[exog_vars])
model_pooled = PooledOLS(Y, X_pooled)
res_pooled = model_pooled.fit(cov_type='robust')

# ------------------------------------------
# 2nd model: Fixed Effects (FE) model / Inside groups (controlling for heterogeneity)
# ------------------------------------------
# Entity_effects=True activate the fixed effects by country 
X_fe = sm.add_constant(df_clean[exog_vars])
model_fe = PanelOLS(Y, X_fe, entity_effects=True, time_effects=True)
res_fe = model_fe.fit(cov_type='clustered', cluster_entity=True)

# ------------------------------------------
# 3rd model: Dynamic Panel Data Model (Arellano-Bond)
# ------------------------------------------
# Simulate the dynamic panel data model using the lag of the dependent variable as an instrument
# We include the lag of the dependent variable as an independent variable to capture the dynamic nature of the model
df_clean['trade_lag'] = df_clean.groupby(level=0)['trade'].shift(1)

# We clean again the dataset to eliminate the first year for each country (since it will have NaN in the lagged variable)
df_dynamic = df_clean.dropna(subset=['trade_lag'].copy())

X_dynamic = sm.add_constant(df_dynamic[['trade_lag'] + exog_vars])
model_dynamic = PanelOLS(df_dynamic['trade'], X_dynamic, entity_effects=True, time_effects=True)
res_dynamic = model_dynamic.fit(cov_type='clustered', cluster_entity=True)

# -------------------------------------------
# Print the results 
# -------------------------------------------
print('------- POOLED OLS RESULTS -------')
print(res_pooled.summary.tables[1])

print("\n------- FIXED EFFECTS RESULTS -------")
print(res_fe.summary.tables[1])

print("\n------- DYNAMIC PANEL DATA RESULTS -------")
print(res_dynamic.summary.tables[1])

## Tabla for the paper with the empirical results
from stargazer.stargazer import Stargazer

# group the 3 models in the Stargazer object
stargazer = Stargazer([res_pooled, res_fe, res_dynamic])

# Set the title and the covariates names
stargazer.custom_columns(['Pooled OLS', 'Fixed Effects', 'Dynamic Panel'], [1, 1, 1])

# We name the variables for the formatting
stargazer.rename_covariates({
    'const': 'Constant',
    'gpr': 'Geopolitical Risk Index (GPR)',
    'trade_lag': 'Trade Openness (t-1)',
    'gdp_growth': 'GDP Growth (annual %)',
    'inflation': 'Inflation, consumer prices (%)'
})

# Order the variables 
stargazer.covariate_order(['trade_lag', 'gpr', 'gdp_growth', 'inflation', 'const'])

# Add the indicators of the FE model
stargazer.add_custom_notes([
    'Data Sources: Caldara & Iacoviello GPR Index Archive (2026); World Bank World Development Indicators (2026).',
    "Notes: Robust standard errors are reported in parentheses. Significance levels: *p<0.1; **p<0.05; ***p<0.01.",
    "The panel is unbalanced due to listwise deletion of missing values (e.g., Argentina 2010-2017) and institutional omissions (Taiwan)."
])

# Print the table in console
print('\n' + '='*60)
print('TABLE: IMPACT OF GEOPOLITICAL RISK ON TRADE OPENNESS')
print('='*60)
try:
    print(stargazer.render_text())
except AttributeError:
    print(str(stargazer))

# Export 
html_file = "tabla_resultados_paper.html"
with open(html_file, "w", encoding="utf-8") as f:
    f.write(stargazer.render_html())

print(f"\n[Finished!] Table saved as: '{html_file}'")
