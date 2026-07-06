import pandas as pd
import os
import glob


def processar_todos_arquivos():
    # Define a pasta onde o script está rodando
    pasta_atual = os.path.dirname(os.path.abspath(__file__))

    # Busca todos os arquivos que terminam com .xlsx na pasta
    arquivos_excel = glob.glob(os.path.join(pasta_atual, "*.xlsx"))

    # Filtra para não processar os arquivos que já foram formatados (evita loop infinito)
    arquivos_para_processar = [f for f in arquivos_excel if "_Formatado" not in f]

    if not arquivos_para_processar:
        print("Nenhum arquivo .xlsx encontrado para processar.")
        return

    print(f"Encontrados {len(arquivos_para_processar)} arquivos. Iniciando processamento...\n")

    for arquivo in arquivos_para_processar:
        try:
            print(f"Processando: {os.path.basename(arquivo)}...")

            # 1. Carrega o arquivo
            df = pd.read_excel(arquivo)

            # 2. Verifica se a coluna existe (Data de Registro)
            coluna = 'Data de Registro'
            if coluna in df.columns:
                # Converte e formata
                df[coluna] = pd.to_datetime(df[coluna], dayfirst=True, errors='coerce')
                df[coluna] = df[coluna].dt.strftime('%Y-%m-%d')

                # 3. Salva o novo arquivo com o sufixo _Formatado
                nome_base = os.path.splitext(os.path.basename(arquivo))[0]
                caminho_saida = os.path.join(pasta_atual, f"{nome_base}_Formatado.xlsx")
                df.to_excel(caminho_saida, index=False)

                print(f"  -> Concluído: {os.path.basename(caminho_saida)}")
            else:
                print(f"  -> Pulei: Coluna '{coluna}' não encontrada neste arquivo.")

        except Exception as e:
            print(f"  -> Erro ao processar {arquivo}: {e}")

    print("\nProcessamento finalizado!")


if __name__ == "__main__":
    processar_todos_arquivos()