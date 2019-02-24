import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
import time

# This makes it to run the firefox driver headless and initialize it
options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_options=options)
driver.set_page_load_timeout(5000)

# This code gets the url, closes the ads and then open the category i provided
driver.get('https://www.jumia.com')
driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/i').click()
driver.find_element_by_xpath('/html/body/div[6]/header/div/nav/ul/li[2]/a').click()
# Gives it time for the new page to load
time.sleep(3)

# Opens a csv file, i know i'm doing this the old fashioned way
nfile = open('result.csv', 'w')
nwriter = csv.writer(nfile)
nwriter.writerow(['BRAND', 'TITLE', 'PRICE'])

# This parses the html of the category we selected
parse = BeautifulSoup(driver.page_source, 'lxml')

# This finds the all h2 tags with a class of title
# and then finds the the brand name from the span tag along with title
for bra in parse.find_all('h2', class_ = 'title'):
    brand = bra.span.text
    tit = bra.find('span', class_ = 'name')
    title = tit.text

    # This selects any div tag that has the css selector specified in the select method
    # And it then writes the brand, title and price to csv file we created
    for pri in parse.select('div.price-container.clearfix span[dir]'):
      pric = pri.text
      price = str(pric)
      nwriter.writerow([brand, title, price])

# This closes the file and then the selenium driver
nfile.close()
driver.quit()











