
  
  create view "file"."main_cleansed"."tags_cleaned__dbt_tmp" as (
    

SELECT
    name AS tag_name,
    commit.sha AS commit_id,
    zipball_url,
    tarball_url
FROM "file"."main_raw"."tags"
  );
