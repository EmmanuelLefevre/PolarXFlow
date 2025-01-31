

SELECT
    name AS file_name,
    path AS file_path,
    type AS content_type,
    size AS file_size,
    html_url AS file_url
FROM "file"."main_raw"."contents"
WHERE type IN ('file', 'dir')