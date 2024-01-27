import duckdb
import os
import glob

# Caminhos para os diretórios contendo os arquivos CSV
csv_directories = ["./data/csv/", "./data/segundo_csv/"]

# Diretório de destino para os arquivos Parquet
parquet_directory = "./data/parquet/"

# Cria o diretório parquet se ele não existir
if not os.path.exists(parquet_directory):
    os.makedirs(parquet_directory)

# Conexão com DuckDB
conn = duckdb.connect()

for dir in csv_directories:
    # Lista todos os arquivos CSV no diretório atual
    csv_files = glob.glob(os.path.join(dir, "*.csv"))

    for csv_file in csv_files:
        # Extrai o nome base do arquivo e cria o caminho do arquivo Parquet no diretório de destino
        base_name = os.path.basename(os.path.splitext(csv_file)[0])
        parquet_file = os.path.join(parquet_directory, base_name + ".parquet")

        # Carrega CSV em uma tabela temporária
        conn.execute(
            f"CREATE TEMPORARY TABLE temp_csv AS SELECT * FROM read_csv_auto('{csv_file}')"
        )

        # Salva a tabela temporária como um arquivo Parquet
        conn.execute(f"COPY temp_csv TO '{parquet_file}' (FORMAT 'parquet')")

        # Limpa a tabela temporária
        conn.execute("DROP TABLE temp_csv")

        print(f"Arquivo convertido: {csv_file} para {parquet_file}")

conn.close()