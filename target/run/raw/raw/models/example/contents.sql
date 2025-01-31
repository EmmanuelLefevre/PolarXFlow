
  
  create view "file"."main_raw"."contents__dbt_tmp" as (
    

SELECT *
FROM read_parquet('data_frame/api_data_20250129_200743.parquet')
  );
