CREATE TABLE workshop AS SELECT 'duckdb+dbtcore' AS name, 3 AS number;
SHOW tables;
SELECT name, number FROM workshop;
SELECT * FROM workshop;
FROM workshop;
.open 'meu_banco.duckdb'
.exit