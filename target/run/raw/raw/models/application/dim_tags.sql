
  
  create view "file"."main_application"."dim_tags__dbt_tmp" as (
    

SELECT
    tag_name,
    commit_id,
    zipball_url,
    tarball_url
FROM "file"."main_cleansed"."tags_cleaned"
  );
