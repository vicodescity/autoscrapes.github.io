# Imports Scrapy Module
import scrapy

# Creates a new Spider class called Jumia
class Jumia(scrapy.Spider):

    # Assigns jumi as the name variable
    name = 'jumi'

    # Puts in the name of the domains that will be scraped from 
    allowed_domain = ['www.jumia.com.ng/']
     
    # The first url that the category links will be scraped from
    start_urls = ['https://www.jumia.com.ng/']

    # Created a function parse that will extract the href attributes of the main categories/subdomains
    def parse(self, response):
        # This locates the selctor path for extracting the href attributes
        for urls in response.css('ul.menu-items li.menu-item'):     
            url = urls.css('a.main-category::attr(href)').get()
            
            # Checks if href attribute scraped is = 1, if it is not it makes a new request to the attribute value and uses self.contain fuction as the callback function
            if url is not None:
               nextp = response.urljoin(url)
               yield scrapy.Request(nextp, callback = self.contin)
    
    # The callback function that will be used to get the required items from the response of the href attributes that we made a request to earlier
    def contin(self, response):
        # This locates the css selector path for the values we want to scrape
        for links in response.css('a.link'):
            # Finds the exact value and makes it a value to the dictionary keys below and returns/yield the item
            yield {
                'brand' : links.css('h2.title span.brand::text').get(),
                'title' : links.css('h2.title span.name::text').get(),
                'price' : u"\u20A6" + links.css('div.price-container.clearfix span.price-box.ri span.price span:nth-child(2)::text').get(),
            }
    # If you want other formats for the final output file when running the "scrapy crawl jumi" add the output command '-o' like so
    # 'scrapy crawl jumi -o example.json', 'scrapy crawl jumi -o example.xml'