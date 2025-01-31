{{ config(schema='application') }}

SELECT
    contributor_id,
    contributor_name,
    avatar_url,
    total_contributions
FROM {{ ref('contributors_cleaned') }}
