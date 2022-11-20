from scrapingbee import ScrapingBeeClient
from tqdm import tqdm

from bs4 import BeautifulSoup
from pathlib import Path

key = 'YF7YE0ZDWRP8SHXOQFMSCGJQDMQ2NMKC0GBYCXTNZD8W8MIYVRR5LRP3SA9UCBMG6Z6XNUGVNX1LIJV2'
client = ScrapingBeeClient(key)


# pbpaste | tr -d '"' | sort | uniq > medium_posts.txt 
# copy and paste the ones marked 1 in the number sheet 

total = sum(1 for i in open("medium_posts.txt", "r"))

with open("medium_posts.txt", "r") as inf:
    for article in tqdm(inf, total=total):
        article = article.replace('\n', '')
        url = "https://towardsdatascience.com/" + article

        save_here = f"articles/{article}"

        my_file = Path(save_here)
        if not my_file.is_file():

            response = client.get(url, params={'render_js': 'False'})

            if response.status_code == 200:
                content = response.content
                with open(save_here, "wb") as of:
                    of.write(content)
        else:
            print(f"already got {save_here}")


    # if you just open the articles themselves medium will redirect you somehow
    # even if you are just opening locally. So this code creates .html versions
    # that you can open here
    for j in dir_.iterdir():
        if str(j)[-5:] != ".html":
            with open(j, "r") as inf:
                html_doc = inf.read()
                soup = BeautifulSoup(html_doc, 'html.parser')
                name = j.name + ".html"
                article = str(soup.find_all('article')[0])
                with open("articles/" + name, "w") as of:
                    of.write(article)