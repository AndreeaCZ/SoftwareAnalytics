-- this is how we create the filtered_data table

create table filtered_data as
SELECT *
FROM
    new_pullreq
WHERE
    (src_churn > 5 OR test_churn > 5 OR num_commits > 2) AND
    mergetime_minutes > 2 AND mergetime_minutes < 60 * 24 * 60 AND
    sloc > 1000 AND
    team_size > 2 AND
    acc_commit_num > 5 AND
    first_pr = 0 AND
    account_creation_days > 14 AND
    prior_review_num > 5 AND
    prior_interaction > 3 AND
    project_age > 90 AND
    description_length > 5 AND
    contrib_country IS NOT NULL AND
    contrib_country != '' AND
    inte_country IS NOT NULL AND
    inte_country != ''
;

DELETE FROM filtered_data
WHERE reponame NOT IN (
    SELECT reponame
    FROM filtered_data
    GROUP BY reponame
    HAVING COUNT(*) >= 10
);