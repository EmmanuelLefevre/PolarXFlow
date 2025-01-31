
  
  create view "file"."main_application"."dim_pull_requests__dbt_tmp" as (
    

SELECT
    pull_request_id,
    pull_request_number,
    author_name,
    pull_request_title,
    pull_request_status,
    creation_date,
    closure_date,
    pull_request_url
FROM "file"."main_cleansed"."pulls_cleaned"
  );
