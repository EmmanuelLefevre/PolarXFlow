{{ config(schema='application') }}

SELECT
    commit_id,
    author_name,
    commit_message,
    commit_date,
    commit_url
FROM {{ ref('commits_cleaned') }}
