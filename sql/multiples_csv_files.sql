-- lê todos os arquivos com nome terminando em ".csv" na pasta "./data/csv"
SELECT * FROM read_csv_auto('./data/csv/*.csv');

-- lê todos os arquivos com nome terminando em ".csv", em qualquer profundidade na pasta "./data"
SELECT * FROM read_csv_auto('./data/**/*.csv');

-- lê arquivos específicos de uma lista
SELECT * FROM read_csv_auto(['.//data/csv//daily_sales_retail_0.csv', './/data/csv//daily_sales_retail_7.csv']);

-- lê todos os arquivos com nome terminando em ".csv" na pasta "./data/csv"
SELECT * FROM read_csv_auto('.//data//csv//*.csv', filename=true);

-- Se deseja criar uma tabela com esses dados, pode fazer da seguinte forma:
CREATE TABLE transactions AS SELECT * FROM read_csv_auto('./data/csv/*.csv', filename=true);

SELECT COUNT(*) FROM transactions;

SELECT * FROM transactions WHERE filename = '.\data\csv\daily_sales_retail_14.csv';
-- Para exibir as tabelas existentes
show tables;

-- Para exibir as tabelas existentes
.open 'datawarehouse.duckdb'

-- Se quiser exportar nossa saída
COPY transactions TO 'output.csv' (HEADER, DELIMITER ',');