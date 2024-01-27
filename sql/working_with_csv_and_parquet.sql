-- Cria uma tabela para armazenar os dados combinados
CREATE TABLE combined_data AS SELECT * FROM read_csv_auto('./data/csv/daily_sales_retail_1.csv');

-- Insere dados de outro arquivo CSV na tabela
INSERT INTO combined_data SELECT * FROM read_csv_auto('./data/csv/daily_sales_retail_1.csv');

-- Insere dados de um arquivo Parquet na tabela
INSERT INTO combined_data SELECT * FROM './data/csv/daily_sales_retail_0.parquet';

-- ler arquivos de tabela
SELECT * FROM combined_data;

-- salvando o schema
.mode markdown
FROM transaction LIMIT 3;
.output myfile.md