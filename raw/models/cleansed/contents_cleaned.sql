{{ config(schema='cleansed') }}

SELECT
    name AS file_name,
    path AS file_path,
    type AS content_type,
    size AS file_size,
    html_url AS file_url
FROM {{ ref('contents') }}
WHERE type IN ('file', 'dir')
