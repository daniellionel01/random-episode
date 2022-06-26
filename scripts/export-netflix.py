from bs4 import BeautifulSoup
import pprint
import json
import re

HTML_PATH = "b99.html"
SAVE_TO_FILE = True
FILE_PATH = "b99.json"

pp = pprint.PrettyPrinter()

seasons = []
with open(HTML_PATH) as f:
    content = f.read()
    soup = BeautifulSoup(content, "html.parser")

    container = soup.find("div", class_="episodeSelector-container")

    episodes = []
    for i, item in enumerate(container.children):
        classes = item.attrs["class"]

        if "episode-item" in classes:
            title = item.find("span", class_="titleCard-title_text")
            title = title.text

            tracker = item.find("div", class_="ptrack-content")
            context = tracker.get("data-ui-tracking-context")
            reg = re.compile("video_id%22:(\d+),")
            nid = reg.search(context)
            nid = nid.group(1)

            episodes.append(dict(id=nid, title=title))
        else: # title
            if i > 0:
                seasons.append(episodes)
            episodes = []

if __name__ == "__main__":
    if SAVE_TO_FILE:
        with open(FILE_PATH, "w") as f:
            f.write(json.dumps(seasons))
    else:
        pp.pprint(seasons)
