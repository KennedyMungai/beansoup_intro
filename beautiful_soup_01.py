"""A simple use case for beautiful soup"""
import requests
from bs4 import BeautifulSoup


URL = 'http://127.0.0.1:5500/web_content/index.html'

page = requests.get(URL, timeout=300)

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup.prettify())

# Finding an element by its ID
result = soup.find(id='page-heading')

# print(result.prettify())

# Finding an element by the css classes
result = soup.find_all("div", class_='row')

# print(result)

# for row in result:
#     # print(row.prettify(), end='\n\n'*4)
#     row_heading = row.find("h3", id='page-heading')

#     if row_heading is not None:
#         print(row_heading.text.lstrip())

h3_heading = soup.find("h3", string='Welcome to my NFT market place..!!')

h3_header = soup.find_all('h3', string=lambda text: "section" in text.lower())

for item in h3_header:
    print(item.text + '\n')
