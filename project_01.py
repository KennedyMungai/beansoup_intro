"""Some Project"""
import requests
from bs4 import BeautifulSoup

URL = 'http://127.0.0.1:5500/web_content/index.html'

page = requests.get(URL, timeout=300)

soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', class_='table')
# print(table.prettify())

table_head = table.find('thead')
# print(table_head)

table_body = table.find('tbody')
# print(table_body)

table_head_row = table_head.find('tr')
# print(table_head_row)

table_head_row_cells = table_head_row.find_all('th')

for cell in table_head_row_cells[1:]:
    print(cell.text.lstrip())
