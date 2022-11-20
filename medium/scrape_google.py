import requests
import json
import urllib.parse
from tqdm import tqdm


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

def get_queries():

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

    with open("queries.txt", "w") as of:
        for query in round1 | round2 | {seed}:
            of.write(query + "\n")

if __name__ == "__main__":
    # get_queries()

    with open("queries.txt", "r") as inf:
        queries = [o.replace("\n", "") for o in inf]
        queries = [o for o in queries if o != "machine learning deployment tools"]

    pages = list(range(1, 11))

    '''
    with open("results.jsonl", "w") as of:
        for query in tqdm(queries, desc="queries"):
            for page in tqdm(pages, desc='pages'):
                query = f"site:towardsdatascience.com {query}" 
                response = send_request(query, page=page)

                for result in response["organic_results"]:
                    result["query"] = query
                    result["page"] = str(page)
                    of.write(json.dumps(result) + "\n")
    '''

    os.system("echo 'relevant,url' > review.csv")
    os.system("cat results.jsonl| jq .url | grep -v 'tagged' | sed 's/https//g' | awk -F'/' '{print $4}' | sed 's/^/0,/g' >> review.csv")


