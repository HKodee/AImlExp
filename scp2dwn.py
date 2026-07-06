import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}

webpage = requests.get('https://www.youtube.com/playlist?list=PLxCzCOWd7aiFAN6I8CuViBuCdJgiOkT2Y', headers=headers).text

soup = BeautifulSoup(webpage, 'lxml')

# for link in soup.find_all("a", href=True):
#     base="https://www.youtube.com"
#     mlink= urljoin(base, a["href"])
#     print(mlink)


print("watch?v=" in webpage)