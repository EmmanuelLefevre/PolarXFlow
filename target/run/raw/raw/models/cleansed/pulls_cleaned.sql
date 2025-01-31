
  
  create view "file"."main_cleansed"."pulls_cleaned__dbt_tmp" as (
    

SELECT
    id AS pull_request_id,
    number AS pull_request_number,
    user.login AS author_name,
    title AS pull_request_title,
    state AS pull_request_status,
    created_at AS creation_date,
    closed_at AS closure_date,
    html_url AS pull_request_url
FROM "file"."main_raw"."pulls"
WHERE state IN ('open', 'closed')
  );
