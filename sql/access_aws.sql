-- Abre Duckdb
duckdb
-- Abre o banco datawarehouse.duckdb
.open "datawarehouse.duckdb"
-- Instala extensões necessáriasInstall extensions
INSTALL httpfs;
LOAD httpfs;
-- Minimum configuration for loading S3 dataset if the bucket is public
SET s3_region='us-east-2';
SET s3_access_key_id='aws_key';
SET s3_secret_access_key='aws_secret';
-- Cria a tabela lendo dos arquivos parquet
DROP TABLE transactions;

CREATE TABLE transactions AS SELECT * FROM read_parquet('s3://datawarehouse-duckdb-alanceloth/sales/*.parquet');
FROM transactions;
SHOW transactions;

-- Mais venda
SELECT store, ROUND(SUM(price), 2) as total_margin
FROM transactions
GROUP BY store
ORDER BY total_margin DESC
LIMIT 1;

-- Top 5 Lojas com Mais Vendas
SELECT store, COUNT(*) as total_sales
FROM transactions
GROUP BY store
ORDER BY total_sales DESC
LIMIT 5;

-- Top 5 Lojas com Menos Vendas
SELECT store, COUNT(*) as total_sales
FROM transactions
GROUP BY store
ORDER BY total_sales
LIMIT 5;

-- 10 Produtos com mais receita
SELECT product_name, ROUND(SUM(price), 2) as total_revenue
FROM transactions
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 10;

-- Exportando uma query
COPY (SELECT product_name, ROUND(SUM(price), 2) as total_revenue
    FROM transactions
    GROUP BY product_name
    ORDER BY total_revenue DESC
    LIMIT 10)
TO 's3://datawarehouse-duckdb-alanceloth/sales/kpi.csv' WITH (FORMAT CSV, HEADER);


INSTALL httpfs;
LOAD httpfs;
-- Minimum configuration for loading S3 dataset if the bucket is public
SET s3_region='us-east-2';
SET s3_access_key_id='AWS_KEY_ID';
SET s3_secret_access_key='AWS_SECRET_KEY';

CREATE TABLE transactions_consolidado (
    transaction_id UUID,
    time_of_transaction TIMESTAMP,
    ean BIGINT,
    name_of_product VARCHAR(255),
    price DECIMAL(10, 2),
    store INTEGER,
    operator INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Define o valor padrão como o timestamp atual
    source_path VARCHAR
);

CREATE TEMPORARY TABLE temp_csv AS SELECT * FROM read_csv_auto('./data/csv/*.csv', filename=true);
COPY temp_csv TO './data/csv/daily_sales.parquet' (FORMAT 'parquet');

COPY temp_csv TO 's3://datawarehouse-duckdb-alanceloth/sales/daily_sales.parquet' (FORMAT 'parquet');


-- Carrega dados do arquivo CSV para a tabela temporária, incluindo o nome do arquivo
CREATE TABLE temp_table AS SELECT *, CURRENT_TIMESTAMP AS created_at FROM read_parquet('s3://datawarehouse-duckdb-alanceloth/sales/daily_sales.parquet');

SELECT * FROM temp_table;
-- Insere dados da tabela temporária para a tabela principal com nomes de colunas modificados
INSERT INTO transactions_consolidado (transaction_id, time_of_transaction, ean, name_of_product, price, store, operator, source_path)
SELECT transaction_id, transaction_time, ean, product_name, price, store, operator, filename FROM temp_table;

-- Remove a tabela temporária
DROP TABLE temp_table;

DROP TABLE transactions_consolidado;

-- Verifica os dados inseridos
SELECT * FROM transactions_consolidado;

-- Exportando uma tabela completa
COPY transactions_consolidado TO 's3://datawarehouse-duckdb-alanceloth/sales/consolidado/consolidado.parquet' (FORMAT 'parquet');

-- Drop table
DROP TABLE transactions;

EXPORT DATABASE './data/database.parquet' (FORMAT PARQUET);

