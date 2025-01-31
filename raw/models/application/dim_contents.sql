{{ config(schema='application') }}

SELECT
    file_name,
    file_path,
    content_type,
    file_size,
    file_url
FROM {{ ref('contents_cleaned') }}
WHERE content_type IN ('file', 'dir')
