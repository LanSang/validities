import os
import torch
import re
from urlextract import URLExtract
from tner import TransformersNER

extractor = URLExtract()


def format_tweet(tweet):
    # mask web urls
    urls = extractor.find_urls(tweet)
    for url in urls:
        tweet = tweet.replace(url, "{{URL}}")
    # format twitter account
    tweet = re.sub(r"\b(\s*)(@[\S]+)\b", r'\1{\2@}', tweet)
    return tweet


print(torch.cuda.is_available())
os._exit(0)

text = "Get the all-analog Classic Vinyl Edition of `Takin' Off` Album from @herbiehancock via @bluenoterecords link below: http://bluenote.lnk.to/AlbumOfTheWeek"
text_format = format_tweet(text)
model = TransformersNER("tner/bertweet-base-tweetner7-2020")
model.predict([text_format])
