
  
  create view "file"."main_application"."dim_commits__dbt_tmp" as (
    

SELECT
    commit_id,
    author_name,
    commit_message,
    commit_date,
    commit_url
FROM "file"."main_cleansed"."commits_cleaned"
  );
