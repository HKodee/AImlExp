import pandas as pd
import requests
from bs4 import BeautifulSoup

#requests.get('https://www.ambitionbox.com/list-of-companies?page=1')
# Response 403


requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text
#can deny access