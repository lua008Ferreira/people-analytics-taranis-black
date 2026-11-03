import pandas as pd

# Base fictícia do desafio (colaboradores)
df = pd.read_excel("04_Base_Colaboradores_People_Analytics.xlsx", sheet_name="Base_Colaboradores")

desligados = df[df["Status"] == "Desligado"]
cedo = desligados[desligados["Dias até Desligamento"] <= 90]

n_cedo = len(cedo)
salario_medio = cedo["Salário Mensal (R$)"].mean()

# Premissas (hipóteses, a validar no piloto)
meses_custo_saida = 3          # custo de uma saída = 3 salários
turnover_atual, turnover_meta = 0.24, 0.17
custo_ia_ano = 20_000

custo_saida = meses_custo_saida * salario_medio
evitadas = round(n_cedo * (1 - turnover_meta / turnover_atual))
economia = evitadas * custo_saida
roi = (economia - custo_ia_ano) / custo_ia_ano

print(f"Desligados em ate 90 dias: {n_cedo}")
print(f"Salario medio: R$ {salario_medio:,.0f}")
print(f"Custo de uma saida (3 salarios): R$ {custo_saida:,.0f}")
print(f"Saidas evitadas por ano (meta 24% -> 17%): {evitadas}")
print(f"Economia anual: R$ {economia:,.0f}")
print(f"Custo estimado da IA: R$ {custo_ia_ano:,.0f}")
print(f"ROI: {roi:.0%}")
