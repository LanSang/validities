import requests
import json
import urllib.parse


def send_request():
    ky = 'YF7YE0ZDWRP8SHXOQFMSCGJQDMQ2NMKC0GBYCXTNZD8W8MIYVRR5LRP3SA9UCBMG6Z6XNUGVNX1LIJV2'
    
    encoded_url = "site:towardsdatascience.com machine learning"

    response = requests.get(
        url="https://app.scrapingbee.com/api/v1/store/google",
        params={
            "api_key": ky,
            "search": encoded_url
        },

    )
    print('Response HTTP Status Code: ', response.status_code)
    print('Response HTTP Response Body: ', response.content)
    with open("tmp.json", "w") as of:
        of.write(json.dumps(json.loads(response.content)))

send_request()