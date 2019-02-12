from selenium import webdriver
import time
import random

profile = webdriver.FirefoxProfile()


profile.set_preference('permissions.default.image', 2)
work=webdriver.Firefox(firefox_profile=profile)
work.set_page_load_timeout(5000)
work.get("https://nnu.ng/login")
work.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/div[1]/div/label/input').send_keys('victordolls')
work.find_element_by_name('password').send_keys('Ihateuall1#')
work.find_element_by_xpath('/html/body/div/div/div/div/div/div/form/div[4]/div/button').click()
work.find_element_by_link_text("Front Page").click()
with open('nnupost.txt','r',encoding='utf-8') as fil:
 for b in fil.readlines()[65:-17]:
  t=b.strip()
  j=str(t)
  work.get(j)
  work.back()
fil.close()
time.sleep(20)
work.quit()
#graceonroli
#agb164468