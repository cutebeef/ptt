import requests
from bs4 import BeautifulSoup

root_url = 'https://disp.cc/b'

r = requests.get('https://disp.cc/b/PttHot')
soup = BeautifulSoup(r.text, 'html.parser') #對字串解析

#for span in spans = soup.find_all('span', class_='listTitle') 
for span in soup.select('#list span.listTitle'):
    href = span.find('a').get('href')
    if href == 'PttHot/59l9':
        break

    url = root_url + href
    title = span.text
    print(f'{title}\n{url}')    