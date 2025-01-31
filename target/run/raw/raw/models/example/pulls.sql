
  
  create view "file"."main_raw"."pulls__dbt_tmp" as (
    

SELECT *
FROM read_parquet('data_frame/api_data_20250129_200708.parquet')
  );
