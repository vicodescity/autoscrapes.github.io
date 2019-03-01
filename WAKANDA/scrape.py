from bs4 import BeautifulSoup
import requests

url = 'https://wakanda.ng'

page = requests.get(url)

with open('wakanda.txt', 'w', encoding = 'utf-8') as file:
 parse = BeautifulSoup(page.text, 'lxml')
 
 for post in parse.find_all('h2', class_ = 'listTitle entry-title td-module-title'):
   posts = post.a
   url = posts.get('href')
   ul = url + '\n'
   file.write(ul)


file.close()

