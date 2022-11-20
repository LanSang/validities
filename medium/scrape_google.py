import requests
import json
import urllib.parse


def send_request(search, page: int=1):
    ky = 'YF7YE0ZDWRP8SHXOQFMSCGJQDMQ2NMKC0GBYCXTNZD8W8MIYVRR5LRP3SA9UCBMG6Z6XNUGVNX1LIJV2'

    response = requests.get(
        url="https://app.scrapingbee.com/api/v1/store/google",
        params={
            "api_key": ky,
            "search": search,
            "page": page
        },

    )
    print('Response HTTP Status Code: ', response.status_code)
    # print('Response HTTP Response Body: ', response.content)
    return json.loads(response.content)

# search = "site:towardsdatascience.com machine learning deployment" 

seed = "machine learning deployment challenges"
response = send_request(seed)

round1 = set()
for query in response["related_queries"]:
    text = query["text"]
    round1.add(text)

round2 = set()
for query in round1:
    response = send_request(query)
    if 'related_queries' in response:
        for query in response["related_queries"]:
            round2.add(text)

with open("queries_round1.txt", "w") as of:
    for i in round1:
        of.write(i + "\n")

with open("queries_round2.txt", "w") as of:
    for i in round2:
        of.write(i + "\n")

#with open("tmp.json", "w") as of:
#    of.write(json.dumps(json.loads(response)))