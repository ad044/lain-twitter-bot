from os import listdir, path, getcwd
import subprocess
import natsort

EPISODE_DIR = path.join("/home/wmh/lain")


def extract_subs(input_file, output_file):
    args = ['ffmpeg', '-i', input_file, '-map', '0:s:0', output_file]
    subprocess.run(args, cwd=getcwd())


episode_files = natsort.natsorted(["{}/{}".format(EPISODE_DIR, f)
                                   for f in listdir(EPISODE_DIR)])

for idx, ep in enumerate(episode_files):
    extract_subs(ep, path.join(
        getcwd(), "anime_subtitles/subtitle_data/{}.srt".format(idx + 1)))
