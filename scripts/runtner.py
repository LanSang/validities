import os
import torch
import re
from urlextract import URLExtract
from tner import TransformersNER

extractor = URLExtract()

print("See emails from Andy on Jan 2, 2023")
print("unset LD_LIBRARY_PATH")
print("export LD_LIBRARY_PATH=/projects/abha4861/software/anaconda/envs/causaldsr/lib")
print("conda activate causaldsr")
print("python runtner.py")
print("to run vim again do unset LD_LIBRARY_PATH")

print("https://huggingface.co/tner/bertweet-base-tweetner7-2020")


def format_tweet(tweet):
    # mask web urls
    urls = extractor.find_urls(tweet)
    for url in urls:
        tweet = tweet.replace(url, "{{URL}}")
    # format twitter account
    tweet = re.sub(r"\b(\s*)(@[\S]+)\b", r'\1{\2@}', tweet)
    return tweet


# print(torch.cuda.is_available())
# os._exit(0)

text = "Get the all-analog Classic Vinyl Edition of `Takin' Off` Album from @herbiehancock via @bluenoterecords link below: http://bluenote.lnk.to/AlbumOfTheWeek"
text_format = format_tweet(text)
model = TransformersNER("tner/bertweet-base-tweetner7-2020")
model.predict([text_format])
