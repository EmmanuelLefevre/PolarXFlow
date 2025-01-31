
  
  create view "file"."main_cleansed"."contents_cleaned__dbt_tmp" as (
    

SELECT
    name AS file_name,
    path AS file_path,
    type AS content_type,
    size AS file_size,
    html_url AS file_url
FROM "file"."main_raw"."contents"
WHERE type IN ('file', 'dir')
  );
