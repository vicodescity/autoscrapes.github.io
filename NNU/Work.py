from selenium import webdriver
import time
import random

work = webdriver.Opera()
work.set_page_load_timeout(5000)
work.get("https://nnu.ng/login")
<<<<<<< HEAD:NNU/Work.py
work.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/div[1]/div/label/input').send_keys('username')
work.find_element_by_name('password').send_keys('password')
=======
work.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/div[1]/div/label/input').send_keys('#Username here')
work.find_element_by_name('password').send_keys('password here')
>>>>>>> ec97789c6f311101bd13c525dc79e131bda9a730:NNU/Automation/NNU_HACK.py
work.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/div[4]/div/button').click()
work.find_element_by_link_text("Front Page").click()

with open('nnupost.txt','r',encoding='utf-8') as fil:
 for b in fil.readlines():
  t = b.strip()
  j = str(t)
  work.get(j)
  work.back()
fil.close()
time.sleep(20)
work.quit()
