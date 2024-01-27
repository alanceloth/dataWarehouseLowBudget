-- Carrega o primeiro arquivo CSV na tabela temporária
CREATE TEMPORARY TABLE temp_csv AS SELECT * FROM read_csv_auto('./data/csv/daily_sales_retail_0.csv');

-- Salva a tabela temporária como um arquivo Parquet
COPY temp_csv TO './data/csv/daily_sales_retail_0.parquet' (FORMAT 'parquet');

-- Limpa a tabela temporária para o próximo arquivo
DROP TABLE temp_csv;

-- Carrega o segundo arquivo CSV na tabela temporária
CREATE TEMPORARY TABLE temp_csv AS SELECT * FROM read_csv_auto('./data/csv/daily_sales_retail_1.csv');

CREATE TEMPORARY TABLE temp_csv AS SELECT * FROM read_csv_auto('./data/csv/*.csv', filename=true);
COPY temp_csv TO './data/csv/daily_sales.parquet' (FORMAT 'parquet');

-- Limpa a tabela temporária após o uso
DROP TABLE temp_csv;

SHOW tables;

SELECT * FROM transactions;