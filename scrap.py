import pandas as pd
import requests
from bs4 import BeautifulSoup

#requests.get('https://www.ambitionbox.com/list-of-companies?page=1')
# Response 403


#requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text
#can deny access

# Define your headers dictionary
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/"
}
webpage = requests.get('https://www.ambitionbox.com/list-of-companies?page=1', headers=headers).text

soup = BeautifulSoup(webpage, 'lxml')
print(soup.prettify())

soup.find_all('h1')[0].text
len(soup.find_all('h2'))

for i in soup.find_all('h2'):
    print(i.text)
    print(i.text.strip())