
  
  create view "file"."main_application"."dim_contributors__dbt_tmp" as (
    

SELECT
    contributor_id,
    contributor_name,
    avatar_url,
    total_contributions
FROM "file"."main_cleansed"."contributors_cleaned"
  );
