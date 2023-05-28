import urllib.request
import re


def yt_url(title) -> str:
    # print(title)
    if " " in title:
        title = title.replace(" ", "+")
    html = urllib.request.urlopen(
        "https://www.youtube.com/results?search_query="+title)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    # print(video_ids)
    return "https://www.youtube.com/watch?v="+video_ids[0]
