ebikes.RC_2022-10.gz is a from `data/reddit` running the grep script on Dec 26, 2022 for "ebikes" and then filtering to just the ebike subreddit. Only using data from the 2022-10 file.

To take the initial sample on Dec 27, 2022 do the following:

`gunzip -c ebikes.RC_2022-10.gz| shuf | head -10 | jq .permalink | sed "s/^/https:\/\/www.reddit.com/g" | tr -d '"' > sample.txt`