ebikes.RC_2022-10.gz is a from `data/reddit` running the grep script on Dec 26, 2022 for "ebikes" and then filtering to just the ebike subreddit. Only using data from the 2022-10 file.

To take the initial sample on Dec 27, 2022 do the following:

`gunzip -c ebikes.RC_2022-10.gz| shuf | head -10 | jq .permalink | sed "s/^/https:\/\/www.reddit.com/g" | tr -d '"' > sample.txt`

Why ebikes? it is a booming industry.

#### Step 1

`make prelims`

- To create the corpus, one researcher from our team reviewed 500 comments from the Reddit forum r/ebikes drawn from 346 Reddit threads. Threads on Reddit include titles. The researcher reviewed thread titles to identify threads where the original poster was asking for an ebike recommendation. In most cases, it was possible to identify such posts from the thread title alone. In a few cases, the researcher looked at the body of the thread to identify if the post was asking for ebike recommendation. 

`gunzip -c ebikes.RC_2022-10.gz| shuf | head -500 | jq .permalink | sed "s/^/https:\/\/www.reddit.com/g" > sample.csv`

This identified 20 reddit threads from October, 2022 where posters were asking for ebike recommendations. 

# cat sample.csv | grep ",1" | awk -F"/" '{print $8}' | wc -l
# cat sample.csv | grep ",1" | awk -F"/" '{print $8}' > recs.txt

We exclude posts where the person will DIY their own bike. We also exclude posts where people ask for advice on a specific bike: https://www.reddit.com/r/ebikes/comments/y98lok/zoomo_ebikes_any_opinions_on_sale_for_699_at_my/it4u887/ or about a comparison https://www.reddit.com/r/ebikes/comments/xsvcde/super73_zx_vs_ariel_rider_xclass_52/iqpg6ho/

We then identified 499 Reddit comments from the 20 titled threads.

We passed these to MTurk. We asked turkers to identify the first 3 ebikes on the comment. We had turkers extract the exact string from the comment that referenced an ebike. To make the turk file, we did 

`$ echo "url" > turk.csv && cat recs.txt >> turk.csv`

From there, we can compute P/R etc. for each of these models. This is $\phi^P_p$.

#### Step 2

Turk information extraction. We have a second round of turk information extraction where we ask turkers, hey what are the reasons the person is recommending this ebike. Copy and paste as many reasons as you can.

#### Step 3 

Make a simple interface that allows people to review 


#### Step 4 

This helps write ads. Write blog posts. 

If you Google "Social media listening" "value proposition" you will find many tutorials on how to do social media listening to help discover your value proposition.
- https://blog.digimind.com/en/insight-driven-marketing/3-ways-social-media-listening-is-paving-the-way-for-deep-customer-personalization
- https://brand24.com/blog/what-is-social-listening/
- https://www.meltycone.com/blog/importance-of-social-listening-in-video-marketing
- https://www.convinceandconvert.com/social-media/how-to-use-social-listening-for-lead-generation/




`cat sample.csv | awk -F"/" '{print $8}' | sort | uniq  | wc -l`
`cat sample.csv | grep ",1" | awk -F"/" '{print $8}' > recs.txt`
`gunzip ebikes.RC_2022-10.gz -c | grep -f recs.txt`

Blog post + reddit ads. Measure click thru.
Reddit ads. Realistic stuff. A/B test different value props. See which value props they find.

They have to choose from the list. Or have to choose based on the social media posts. Then you can run A/B on all of them and pick the best one. If the recall is bad the person may miss it.

#### What is the task?

- Limit to threads in which a person asks for a recommendation for a bike. Use only the title of the thread.

- For comments that mention a bike, ask people: extract all of the reasons why the person is recommending a bike. "Beefy motor," "battery performance," "quality base," "massive battery."

Ask Turkers: why are people recommending this? 

Validation: go to the product page.