import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ.get("EAACZCCHy6lfsBAPDiiWirvs6FHsffQv61EJBtTW3EZCinqOnqAyk5u1gLAawix3yT6ugLyHGhchfkDyjeHeZBagt0XWf4ZAJBweNO9tZCQZCsC3f6aT6Fr3pPt1wGzErQXR6oSH0MaC4V7W7rWWRGGfoKC7zNo1C1tGiHvDnsWkUezEQReTzOS")

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response.text
