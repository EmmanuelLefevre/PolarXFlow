{{ config(schema='application') }}

SELECT
    tag_name,
    commit_id,
    zipball_url,
    tarball_url
FROM {{ ref('tags_cleaned') }}
