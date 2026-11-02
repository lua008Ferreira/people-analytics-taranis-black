import pandas as pd
import matplotlib.pyplot as plt


def carregar_dados_ficticios() -> pd.DataFrame:
    """Cria um conjunto de dados fictícios para análises de turnover."""
    return pd.DataFrame(
        {
            "satisfacao": [2, 3, 4, 1, 5, 2, 4, 3, 1, 5],
            "engajamento": [3, 4, 5, 2, 5, 2, 4, 4, 1, 5],
            "tempo_empresa_anos": [1, 2, 5, 1, 7, 2, 6, 4, 1, 8],
            "turnover": [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
            "motivo_saida": [
                "Remuneração",
                "N/A",
                "N/A",
                "Liderança",
                "N/A",
                "Carreira",
                "N/A",
                "N/A",
                "Ambiente",
                "N/A",
            ],
        }
    )


def gerar_grafico_correlacoes(df: pd.DataFrame, caminho_saida: str) -> None:
    correlacoes = df[["satisfacao", "engajamento", "tempo_empresa_anos", "turnover"]].corr()
    plt.figure(figsize=(8, 6))
    plt.imshow(correlacoes, cmap="Blues", interpolation="nearest")
    plt.colorbar(label="Correlação")
    plt.xticks(range(len(correlacoes.columns)), correlacoes.columns, rotation=45, ha="right")
    plt.yticks(range(len(correlacoes.index)), correlacoes.index)
    plt.title("Matriz de Correlações - People Analytics")
    plt.tight_layout()
    plt.savefig(caminho_saida)
    plt.close()


def gerar_grafico_motivos(df: pd.DataFrame, caminho_saida: str) -> None:
    motivos = df[df["turnover"] == 1]["motivo_saida"].value_counts()
    plt.figure(figsize=(8, 5))
    motivos.plot(kind="bar", color="#1f77b4")
    plt.title("Principais Motivos de Turnover")
    plt.xlabel("Motivo")
    plt.ylabel("Quantidade")
    plt.tight_layout()
    plt.savefig(caminho_saida)
    plt.close()


def main() -> None:
    df = carregar_dados_ficticios()
    gerar_grafico_correlacoes(df, "grafico_correlacoes.png")
    gerar_grafico_motivos(df, "grafico_turnover_motivos.png")
    print("Análise concluída. Gráficos gerados na pasta analise-dados.")


if __name__ == "__main__":
    main()
