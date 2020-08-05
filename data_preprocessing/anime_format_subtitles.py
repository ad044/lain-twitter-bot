from os import listdir, path, getcwd
from bs4 import BeautifulSoup
import natsort

SUBTITLE_DIR = path.join(getcwd(), "anime_subtitles/subtitle_data")


# extracts text from inside <font> tags, removes timestamps and indices
def format_subtitle_file(subtitle_file):
    with open(subtitle_file, "r") as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        return [line for line in filter(
            None, soup.text.splitlines()) if not line[0].isdigit()][16:-24]


subtitle_files = natsort.natsorted(["{}/{}".format(SUBTITLE_DIR, f)
                                    for f in listdir(SUBTITLE_DIR)])

for idx, sub in enumerate(subtitle_files):
    with open(path.join(getcwd(), "anime_subtitles/formatted_subtitle_data/{}.txt".format(idx + 1)), "w+") as f:
        for line in format_subtitle_file(sub):
            f.write("%s\n" % line)
