
  
  create view "file"."main_cleansed"."contributors_cleaned__dbt_tmp" as (
    

SELECT
    id AS contributor_id,
    login AS contributor_name,
    avatar_url,
    contributions AS total_contributions
FROM "file"."main_raw"."contributors"
WHERE contributions > 0
  );
