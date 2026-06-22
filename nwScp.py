import pandas as pd
import requests
from bs4 import BeautifulSoup

final = pd.DataFrame()

for j in range(1,11):

    url = 'https://www.ambitionbox.com/list-of-companies?page={}'.format()
    