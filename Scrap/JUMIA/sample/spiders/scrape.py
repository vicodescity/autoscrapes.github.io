#encoding utf-8
import scrapy

class NNU(scrapy.Spider):

 name = 'jumia'

 start_domain = ['www.jumia.com.ng']

 start_urls = ['https://www.jumia.com.ng/video-games/']

 def parse(self, response):

  title = response.css('.name::text').extract()
  price = response.css('span::attr(data-price)').extract()

  for item in zip(title, price):
   new = u"\u20A6" + item[1]
   info = {

     'name' : item[0],
     'price' : new,
   }
    
   yield info