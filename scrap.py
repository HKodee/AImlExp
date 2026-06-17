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

soup.find_all('p', class_='rating')

company = soup.find_all('div',class_='company-content-wrapper')

name=[]
rating=[]
reviews=[]
ctype=[]
hq=[]
age=[]
employees=[]


for i in company:
    name.append(i.find('h2').text.strip())
    rating.append(i.find('p', class_='rating').text.strip())
    reviews.append(i.find('a', class_='review-count').text.strip())
    ctype.append(i.find_all('p', class_='infoEntity')[0].text.strip())
    hq.append(i.find_all('p', class_='infoEntity')[1].text.strip())
    age.append(i.find_all('p', class_='infoEntity')[2].text.strip())
    employees.append(i.find_all('p', class_='infoEntity')[3].text.strip())

d = {'name':name, 'rating':rating, 'reviews':reviews, 'type':ctype, 'headquarter':hq, 'age':age, 'employees':employees}
df = pd.DataFrame(d)
print(df)