{{
    config(
        materialized = 'table'
    )
}}


WITH fato_transactions AS (
    SELECT * FROM {{ ref('fato_transactions')}}
)

SELECT store, COUNT(*) as total_sales
    FROM fato_transactions
    GROUP BY store
    ORDER BY total_sales DESC
    LIMIT 5