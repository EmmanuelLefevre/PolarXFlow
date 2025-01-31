{{ config(schema='cleansed') }}

SELECT
    id AS contributor_id,
    login AS contributor_name,
    avatar_url,
    contributions AS total_contributions
FROM {{ ref('contributors') }}
WHERE contributions > 0