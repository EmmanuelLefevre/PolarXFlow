{{ config(schema='cleansed') }}

SELECT
    name AS tag_name,
    commit.sha AS commit_id,
    zipball_url,
    tarball_url
FROM {{ ref('tags') }}
