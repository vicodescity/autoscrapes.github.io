import requests
from bs4 import BeautifulSoup

page = requests.get("https://nnu.ng/").text
soup = BeautifulSoup(page,'lxml')

with open('nnupost.txt','w',encoding='utf-8') as fil:
 for t in soup.find_all('a'):

    a = t.get('href')
    fil.write(a+'\n')

fil.close()
