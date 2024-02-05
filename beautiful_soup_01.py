"""A simple use case for beautiful soup"""
import requests
from bs4 import BeautifulSoup


URL = 'http://127.0.0.1:5500/web_content/index.html'

page = requests.get(URL, timeout=300)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
