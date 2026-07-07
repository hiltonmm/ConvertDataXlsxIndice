import pandas as pd
import os
import glob


def processar_arquivos(coluna_alvo):
    pasta_atual = os.path.dirname(os.path.abspath(__file__))

    # Busca todos os arquivos .xlsx, excluindo os que já foram processados
    arquivos_excel = [f for f in glob.glob(os.path.join(pasta_atual, "*.xlsx")) if "_Formatado" not in f]

    if not arquivos_excel:
        print("Nenhum arquivo .xlsx novo encontrado.")
        return

    for arquivo in arquivos_excel:
        try:
            print(f"Processando: {os.path.basename(arquivo)}...")
            df = pd.read_excel(arquivo)

            # Verifica se a coluna existe (por nome ou índice)
            if coluna_alvo in df.columns:
                # Converte para data e formata para string YYYY-mm-dd
                df[coluna_alvo] = pd.to_datetime(df[coluna_alvo], dayfirst=True, errors='coerce')
                df[coluna_alvo] = df[coluna_alvo].dt.strftime('%Y-%m-%d')

                # Salva o arquivo
                nome_base = os.path.splitext(os.path.basename(arquivo))[0]
                caminho_saida = os.path.join(pasta_atual, f"{nome_base}_Formatado.xlsx")
                df.to_excel(caminho_saida, index=False)
                print(f"  -> Concluído: {os.path.basename(caminho_saida)}")
            else:
                print(f"  -> Erro: Coluna '{coluna_alvo}' não encontrada em {os.path.basename(arquivo)}.")

        except Exception as e:
            print(f"  -> Erro ao processar {arquivo}: {e}")


if __name__ == "__main__":
    # AQUI VOCÊ DEFINE A COLUNA QUE QUER PROCESSAR
    # Para Casamentos: 'Data de Registro'
    # Para Óbitos: coloque o nome exato da coluna G aqui
    COLUNA_A_CONVERTER = 'Data de Registro'  # <--- AJUSTE ESTE NOME SE FOR DIFERENTE

    processar_arquivos(COLUNA_A_CONVERTER)