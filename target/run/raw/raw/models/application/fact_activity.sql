
  
  create view "file"."main_application"."fact_activity__dbt_tmp" as (
    

SELECT
    c.contributor_id,
    c.contributor_name,
    COUNT(DISTINCT commits.commit_id) AS total_commits,
    COUNT(DISTINCT pr.pull_request_id) AS total_pull_requests,
    COUNT(DISTINCT tags.tag_name) AS total_tags,
    SUM(contents.file_size) AS total_file_size
FROM "file"."main_application"."dim_contributors" c
LEFT JOIN "file"."main_application"."dim_commits" commits ON c.contributor_id = commits.author_name
LEFT JOIN "file"."main_application"."dim_pull_requests" pr ON c.contributor_id = pr.author_name
LEFT JOIN "file"."main_application"."dim_tags" tags ON commits.commit_id = tags.commit_id
LEFT JOIN "file"."main_application"."dim_contents" contents ON c.contributor_id = contents.file_url
GROUP BY c.contributor_id, c.contributor_name
  );
