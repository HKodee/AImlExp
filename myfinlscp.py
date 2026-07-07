import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from yt_dlp import YoutubeDL
import time

url = "https://www.youtube.com/playlist?list=PLxCzCOWd7aiFAN6I8CuViBuCdJgiOkT2Y"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

base = "https://www.youtube.com"

video_links = []

for a in soup.find_all("a", href=True):

    href = a["href"]

    if href.startswith("/watch"):

        full_link = urljoin(base, href)

        # Remove duplicate links
        if full_link not in video_links:
            video_links.append(full_link)

print(f"Found {len(video_links)} links")

for i, link in enumerate(video_links, start=1):
    print(i, link)
    
    

ydl_opts = {
    "format": "bestvideo+bestaudio/best",
    "merge_output_format": "mp4",
    "continuedl": True,
    "download_archive": "downloaded.txt",
    "overwrites": False,
}

with YoutubeDL(ydl_opts) as ydl:

    for i, link in enumerate(video_links[100:], start=101):

        while True:

            try:
                print(f"Downloading {i}")
                ydl.download([link])
                break

            except Exception as e:

                print(e)
                print("Retrying in 30 seconds...")
                time.sleep(30)