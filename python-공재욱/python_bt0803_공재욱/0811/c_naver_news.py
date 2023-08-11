### 네이버 규스 해드라인 크롤링 ###

import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/031/0000765174?sid=105'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

headline = soup.select('.media_end_head_headline')
print(headline) 