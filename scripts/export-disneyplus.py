#!/bin/python3

import requests
import pprint
import json
import re

HTML_PATH = "castle.html"
SAVE_TO_FILE = True
FILE_PATH = "src/data/castle.json"

pp = pprint.PrettyPrinter()

season_ids = [
    "17fc7a43-08ae-4331-b339-f27beb4bd8cd",
    "f7098073-18aa-45d8-b165-f5f5162892e2",
    "9f14a6f0-7180-4951-85c4-a041c4b822e7",
    "418fd414-655f-4ce1-ad6c-ca8cc6794af7",
    "d93a4ef3-c4a3-4823-947f-082ba95ffba0",
    "b9b61ffc-02b6-40d8-8c4f-57641fe62208",
    "913b39ac-bad8-47a5-8305-11f042b24b2b",
    "91b8633e-7361-4d9c-9a07-576f52aa8fd0"
]

seasons = []
for i, uuid in enumerate(season_ids):
    episodes = []
    url = f"https://disney.content.edge.bamgrid.com/svc/content/DmcEpisodes/version/5.1/region/DE/audience/k-false,l-true/maturity/1850/language/en/seasonId/{uuid}/pageSize/15/page/1"
    res = requests.get(url)
    data = res.json()
    data = data["data"]["DmcEpisodes"]["videos"]
    for video in data:
        title = video["text"]["title"]["full"]["program"]["default"]["content"]
        episodes.append(dict(id=video["contentId"], title=title))
    seasons.append(episodes)

if __name__ == "__main__":
    if SAVE_TO_FILE:
        with open(FILE_PATH, "w") as f:
            f.write(json.dumps(seasons))
    else:
        pp.pprint(seasons)
