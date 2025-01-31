

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