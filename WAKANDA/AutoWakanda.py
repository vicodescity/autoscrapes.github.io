from selenium import webdriver
import time
import Comments
import random 
import requests

driver = webdriver.Firefox()

driver.set_page_load_timeout(5000)

driver.get('https://wakanda.ng/login')

driver.find_element_by_name('email').send_keys('vicojeje25@gmail.com')

driver.find_element_by_name('password').send_keys('Ihateuall1#')

driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[4]/div/div/div[1]/div/div/form/div[4]/button').click()


with open('wakanda.txt', 'r', encoding = 'utf-8') as file:

 for post in file.readlines():
 

  words = random.choice(Comments.comments)
  
  time.sleep(10)

 
  driver.get(post)

  time.sleep(25)

  driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="edui1_iframeholder"]//iframe'))
   
  driver.find_element_by_xpath('/html/body').click() 

  driver.find_element_by_xpath('/html/body').send_keys(words)

  driver.switch_to.default_content()

  driver.find_element_by_xpath('//*[@id="ReplyButton"]').click()

  time.sleep(10)

  driver.back()

  driver.back()


file.close()

driver.quit()