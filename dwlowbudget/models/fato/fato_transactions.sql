{{
    config(
        materialized = 'table'
    )
}}

WITH src_transactions AS (
    SELECT * FROM {{ ref('src_transactions')}}
)

SELECT
    transaction_id,
    time_of_transaction,
    ean as ean_of_product,
    store,
    price,
    CASE
        WHEN price > 20 THEN TRUE
        ELSE FALSE
    END AS price_greater_than_20,
    CASE
        WHEN EXTRACT(HOUR FROM time_of_transaction) >= 0 AND EXTRACT(HOUR FROM time_of_transaction) <= 6 THEN 'Dawn'
        WHEN EXTRACT(HOUR FROM time_of_transaction) > 6 AND EXTRACT(HOUR FROM time_of_transaction) <= 12 THEN 'Morning'
        WHEN EXTRACT(HOUR FROM time_of_transaction) > 12 AND EXTRACT(HOUR FROM time_of_transaction) <= 18 THEN 'Afternoon'
        WHEN EXTRACT(HOUR FROM time_of_transaction) > 18 AND EXTRACT(HOUR FROM time_of_transaction) <= 23 THEN 'Night'
        ELSE 'Unknown'
    END AS period
FROM
    src_transactions

{% if is_incremental() %}
    WHERE time_of_transaction > (SELECT MAX(time_of_transaction) FROM {{ this }})
{% endif %}