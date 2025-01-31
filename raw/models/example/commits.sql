{{ config(schema='raw') }}

SELECT *
FROM read_parquet('data_frame/api_data_20250129_200653.parquet')
