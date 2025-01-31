

SELECT
    name AS tag_name,
    commit.sha AS commit_id,
    zipball_url,
    tarball_url
FROM "file"."main_raw"."tags"