import requests
from os import path, getcwd
from bs4 import BeautifulSoup

r = requests.get("https://laingame.net/index.php?site=0#l4")
soup = BeautifulSoup(r.text, 'html.parser')

anchors = [anchor['href'] for anchor in soup.find_all("a", href=True)][4:-4]
urls = ["https://laingame.net{}".format(anchor) for anchor in anchors]

paragraphs = []
for idx, url in enumerate(urls):
    url_soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    paragraph = "".join(line.strip() for line in url_soup.find(
        "div", {"class": "translation"}).text.split("\n"))
    paragraphs.append(paragraph)
    print(idx)

with open(path.join(getcwd(), "game_subtitles/subtitle_data/subs.txt"), "w+") as f:
        for line in paragraphs:
            f.write("%s\n" % line)