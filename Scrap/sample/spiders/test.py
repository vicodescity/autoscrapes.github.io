def parse(self, response):

 	title = response.css('.s1okktje-0 kVQyNs::text').extract()

 	comments = response.css('.FHCV02u6Cp2zYL0fhQPsO::text').extract()

 	for item in zip(title, comments):

 	 scraped_info = {
      
      'tile' : item[0],

      'comment' : item[1],

 	 }

 	 yield scraped_info