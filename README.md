
# people-analytics-taranis
Consultoria estratégica de IA e People Analytics para redução de turnover (Challenge ONE + Alura)
# IA no RH da Taranis Black

Proposta de consultoria de IA para reduzir o turnover e recuperar o clima de uma empresa fictícia, com **decisão final sempre humana** e conformidade com a LGPD.

> Projeto educacional desenvolvido no **Challenge Taranis Black** (Rota 3: RH e People Analytics), parte da Imersão Agentes de IA para Negócios da **Oracle Next Education (ONE) + Alura**. A empresa, os colaboradores e todos os dados são **fictícios**.

## O problema

A Taranis Black, empresa fictícia de ergonomia corporativa com 280 colaboradores, enfrenta **24% de turnover nos primeiros 90 dias** e queda do eNPS de **+62 para +28**. A causa mais citada: líderes recém-promovidos com dificuldade para conduzir feedbacks difíceis.

## A solução em uma frase

Três iniciativas de IA no RH, priorizadas por esforço e impacto, com supervisão humana, métricas de adoção e uma política de IA responsável.

| # | Iniciativa | Tipo de IA | Posição na matriz |
|---|---|---|---|
| 1 | Alerta de risco de turnover | Preditiva | Alto impacto, baixo esforço (vitória rápida) |
| 2 | Simulador de feedback para líderes (modelo SBI) | Generativa | Alto impacto, alto esforço (aposta estratégica) |
| 3 | Mapeamento de perfis de liderança | Tradicional / ML | Baixo impacto, baixo esforço (melhoria contínua) |

## Resultados em destaque

- **Meta proposta:** turnover de 90 dias de 24% para 17% em dois trimestres; eNPS de +28 para +45 em 12 meses.
- **ROI estimado:** cerca de **314%**. Na base fictícia, 13 pessoas saíram em até 90 dias, com salário médio de R$ 6.908. Com 3 salários como custo de saída (hipótese), a meta evita cerca de 4 saídas por ano, uma economia de R$ 82.900 contra um custo estimado de R$ 20.000.
- **Governança:** princípios de IA responsável, matriz de riscos, regras de uso, conformidade com a LGPD (incluindo o art. 20 sobre decisões automatizadas), Comitê de IA e auditoria periódica.

As premissas (custo de saída, custo da IA e horas economizadas) são hipóteses, declaradas no documento e a validar em um piloto.

## O que contém este repositório

| Entrega | Situação | Onde |
|---|---|---|
| Rota 0: AI Canvas, casos de uso, matriz, métricas, plano de mudança e política de IA | Concluída | [`docs/`](docs/) |
| Simulador de feedback (4 personas, prompt de sistema, sessões A e B com SBI, avaliação 2,0 vs 9,8) | Concluída | [`simulador-feedback/`](simulador-feedback/) |
| Análise de People Analytics (turnover, motivos, eNPS, correlações, clima) | Concluída | [`analise-people-analytics/`](analise-people-analytics/) |
| Prints e evidências | Concluída | [`evidencias/`](evidencias/) |
| Cálculo de ROI em Python | Concluída | [`roi/`](roi/) |
| Vídeo de apresentação (até 5 min) | A gravar | [link a adicionar] |

## Como foi feito

- **AI Canvas** da STARSE para estruturar problema, solução com e sem IA, públicos, dados e ferramentas.
- **ChatGPT** para o simulador de feedback.
- **Python (pandas, matplotlib)** para o ROI e para a análise de People Analytics.
- **Google Docs** como entrega final do challenge.

## Princípios do projeto

1. A IA apoia a decisão e nunca decide sobre pessoas.
2. Nenhum dado pessoal real é usado.
3. Atributos sensíveis (gênero, idade, salário) ficam fora dos modelos.
4. A IA não monitora conversas reais.

## Sobre mim

**Luana Ferreira de Sousa**, estudante de Ciência de Dados com experiência em governança de dados e suporte de TI, em transição para dados e IA.

- LinkedIn: [link]
- Portfólio: [link]

---
*Projeto educacional. Empresa, pessoas e dados fictícios. Nenhuma informação real é usada neste repositório.*
