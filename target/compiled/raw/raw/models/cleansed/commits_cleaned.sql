

SELECT
    sha AS commit_id,
    author.login AS author_name,
    commit.message AS commit_message,
    commit.author.date AS commit_date,
    html_url AS commit_url
FROM "file"."main_raw"."commits"
WHERE commit.author.date IS NOT NULL