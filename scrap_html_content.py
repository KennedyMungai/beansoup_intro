"""A simple script mean to scrap the data off of a static web page"""
import requests

URL = 'http://127.0.0.1:5500/web_content/index.html'

page = requests.get(URL, timeout=300)

print(page.text)
