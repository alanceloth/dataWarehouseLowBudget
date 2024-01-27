-- Alterar o nome da time_of_transaction e name_of_product
-- Remover colunas não importantes
-- Adicionar colunas de rastreabilidade

CREATE TABLE transactions (
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

-- Carrega dados do arquivo CSV para a tabela temporária, incluindo o nome do arquivo
CREATE TABLE temp_table AS SELECT *, CURRENT_TIMESTAMP AS created_at FROM read_csv_auto('./data/csv/*.csv', filename=true);


-- Insere dados da tabela temporária para a tabela principal com nomes de colunas modificados
INSERT INTO transactions (transaction_id, time_of_transaction, ean, name_of_product, price, store, operator, source_path)
SELECT transaction_id, transaction_time, ean, product_name, price, store, operator, filename FROM temp_table;

-- Remove a tabela temporária
DROP TABLE temp_table;

-- Verifica os dados inseridos
SELECT * FROM transactions;

-- Exportando uma tabela completa
COPY transactions TO 's3://workshop03-salesrecord/vendas/consolidado.parquet';


-- Drop table
DROP TABLE transactions;